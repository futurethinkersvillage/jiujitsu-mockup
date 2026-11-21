"""Builds the club's subscribable events calendar.

Inputs (committed):
  build/events/club.json      our own events, including the weekly classes (recurring)
  build/events/external.json  judo / BJJ events in BC and Alberta (refreshed monthly)
Outputs:
  site/events.ics             iCalendar feed: subscribe from Google / Apple / Outlook
  site/events/index.html      full list
  (build_site.py imports upcoming() for the homepage Events section)

Run: python build/build_events.py
"""
import html
import json
from datetime import date, datetime, timedelta, timezone
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent / "site"
SITE = "https://clearwatermma.ca"
FEED = f"{SITE}/events.ics"
CAL_NAME = "Shi Mizu Dojo · BC & Alberta judo and jiu jitsu events"
TZ = "America/Vancouver"
GOOGLE_SUB = "https://calendar.google.com/calendar/r?cid=" + "webcal%3A%2F%2Fclearwatermma.ca%2Fevents.ics"
WEBCAL = "webcal://clearwatermma.ca/events.ics"

VTIMEZONE = """BEGIN:VTIMEZONE
TZID:America/Vancouver
X-LIC-LOCATION:America/Vancouver
BEGIN:DAYLIGHT
TZOFFSETFROM:-0800
TZOFFSETTO:-0700
TZNAME:PDT
DTSTART:19700308T020000
RRULE:FREQ=YEARLY;BYMONTH=3;BYDAY=2SU
END:DAYLIGHT
BEGIN:STANDARD
TZOFFSETFROM:-0700
TZOFFSETTO:-0800
TZNAME:PST
DTSTART:19701101T020000
RRULE:FREQ=YEARLY;BYMONTH=11;BYDAY=1SU
END:STANDARD
END:VTIMEZONE"""


def load(name):
    p = HERE / "events" / name
    return json.loads(p.read_text(encoding="utf-8")) if p.exists() else []


def esc(s):
    return (s or "").replace("\\", "\\\\").replace(";", "\\;").replace(",", "\\,").replace("\n", "\\n")


def fold(line):
    """RFC 5545: lines longer than 75 octets are folded with CRLF + space."""
    out, b = [], line.encode("utf-8")
    while len(b) > 75:
        cut = 75
        while cut > 0 and (b[cut] & 0xC0) == 0x80:  # don't split a UTF-8 character
            cut -= 1
        out.append(b[:cut].decode("utf-8"))
        b = b" " + b[cut:]
    out.append(b.decode("utf-8"))
    return "\r\n".join(out)


def uid(e):
    base = f"{e.get('start')}-{e.get('title')}".lower()
    return "".join(c if c.isalnum() else "-" for c in base)[:90] + "@jiujitsu.designspore.co"


def where(e):
    return ", ".join(x for x in [e.get("venue"), e.get("city"), e.get("province")] if x)


def vevent(e, stamp):
    lines = ["BEGIN:VEVENT", f"UID:{uid(e)}", f"DTSTAMP:{stamp}"]
    if e.get("time_start"):  # timed event in local time
        d = e["start"].replace("-", "")
        lines += [f"DTSTART;TZID={TZ}:{d}T{e['time_start'].replace(':', '')}00",
                  f"DTEND;TZID={TZ}:{d}T{e['time_end'].replace(':', '')}00"]
        if e.get("rrule"):
            lines.append(f"RRULE:{e['rrule']}")
    else:  # all-day (DTEND is exclusive)
        s = date.fromisoformat(e["start"])
        en = date.fromisoformat(e["end"]) if e.get("end") else s
        lines += [f"DTSTART;VALUE=DATE:{s:%Y%m%d}", f"DTEND;VALUE=DATE:{en + timedelta(days=1):%Y%m%d}"]
    tag = "Shi Mizu Dojo" if e.get("club") else f"{e.get('discipline', '').upper()} {e.get('type', '')}".strip()
    tentative = "" if e.get("club") or e.get("confidence") == "confirmed" else " [tentative]"
    lines.append(f"SUMMARY:{esc(e['title'])}" + (f" ({esc(tag)})" if tag and not e.get("club") else "") + tentative)
    if where(e):
        lines.append(f"LOCATION:{esc(where(e))}")
    tent = "" if e.get("club") or e.get("confidence") == "confirmed" else "Date not yet confirmed by the organiser; check before you travel."
    desc = " · ".join(x for x in [e.get("organiser"), tent, e.get("notes"), e.get("url")] if x)
    if desc:
        lines.append(f"DESCRIPTION:{esc(desc)}")
    if e.get("url"):
        lines.append(f"URL:{e['url']}")
    lines.append("END:VEVENT")
    return [fold(x) for x in lines]


def all_events():
    club = [dict(e, club=True) for e in load("club.json")]
    ext = load("external.json")
    return club, ext


def build_ics():
    club, ext = all_events()
    stamp = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")
    out = ["BEGIN:VCALENDAR", "VERSION:2.0", "PRODID:-//Shi Mizu Dojo//Events//EN", "CALSCALE:GREGORIAN",
           "METHOD:PUBLISH", fold(f"X-WR-CALNAME:{esc(CAL_NAME)}"), f"X-WR-TIMEZONE:{TZ}",
           fold("X-WR-CALDESC:" + esc("Shi Mizu Dojo classes and events, plus judo and jiu jitsu tournaments, seminars and courses in BC and Alberta. Updated monthly.")),
           "REFRESH-INTERVAL;VALUE=DURATION:P1D", "X-PUBLISHED-TTL:P1D"]
    out += VTIMEZONE.split("\n")
    for e in club + ext:
        out += vevent(e, stamp)
    out.append("END:VCALENDAR")
    (ROOT / "events.ics").write_text("\r\n".join(out) + "\r\n", encoding="utf-8", newline="")
    return len(club), len(ext)


def upcoming(limit=None, today=None):
    """One-off events (not the weekly classes) from today on, soonest first."""
    today = today or date.today()
    club, ext = all_events()
    items = [e for e in club + ext if not e.get("rrule") and date.fromisoformat(e.get("end") or e["start"]) >= today]
    items.sort(key=lambda e: e["start"])
    return items[:limit] if limit else items


def when(e):
    s = date.fromisoformat(e["start"])
    if e.get("end") and e["end"] != e["start"]:
        en = date.fromisoformat(e["end"])
        return f"{s:%b} {s.day}–{en.day}, {s.year}" if s.month == en.month else f"{s:%b} {s.day} – {en:%b} {en.day}, {en.year}"
    return f"{s:%a %b} {s.day}, {s.year}"


def row_html(e):
    t = html.escape(e["title"])
    title = f'<a href="{html.escape(e["url"])}" rel="noopener">{t}</a>' if e.get("url") else t
    meta = " · ".join(html.escape(x) for x in [where(e), e.get("organiser") if not e.get("club") else "Shi Mizu Dojo"] if x)
    kind = "Club event" if e.get("club") else " ".join(x for x in [{"bjj": "BJJ"}.get((e.get("discipline") or "").lower(), (e.get("discipline") or "").capitalize()), e.get("type")] if x)
    if not e.get("club") and e.get("confidence") != "confirmed":
        kind += " · date tentative"
    return (f'<li><time datetime="{e["start"]}">{when(e)}</time><div><b>{title}</b>'
            f'<span>{html.escape(kind)}{(" · " + meta) if meta else ""}</span></div></li>')


def subscribe_html():
    return (f'<div class="sub"><a class="btn" href="{GOOGLE_SUB}" rel="noopener">Add to Google Calendar</a>'
            f'<a class="btn btn-ghost" href="{WEBCAL}">Apple / Outlook</a>'
            f'<a class="btn btn-ghost" href="../events.ics">Download .ics</a></div>')


def build_page():
    items = upcoming()
    groups, cur = [], None
    for e in items:
        m = date.fromisoformat(e["start"]).strftime("%B %Y")
        if m != cur:
            groups.append((m, []))
            cur = m
        groups[-1][1].append(e)
    body = "".join(f"<h2>{m}</h2><ul class=\"ev\">{''.join(row_html(e) for e in es)}</ul>" for m, es in groups) \
        or "<p>No upcoming events listed yet.</p>"
    page = f"""<!doctype html>
<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">
<title>Events · Shi Mizu Dojo</title>
<meta name="description" content="Judo and Brazilian jiu jitsu events in BC and Alberta, plus Shi Mizu Dojo classes. Subscribe in Google, Apple or Outlook calendar.">
<meta name="robots" content="noindex">
<link href="https://fonts.googleapis.com/css2?family=Archivo:wdth,wght@62..125,100..900&display=swap" rel="stylesheet">
<link rel="stylesheet" href="../assets/doc.css">
<style>
  .sub {{ display: flex; flex-wrap: wrap; gap: .6rem; margin: 1.2rem 0 .4rem; }}
  .btn {{ display: inline-flex; align-items: center; min-height: 44px; padding: .6rem 1rem; font-weight: 700; text-decoration: none; background: var(--ink); color: var(--bg); border: 2px solid var(--ink); }}
  .btn-ghost {{ background: transparent; color: var(--ink); }}
  .ev {{ list-style: none; padding: 0; margin: 0; }}
  .ev li {{ display: grid; grid-template-columns: 9.5rem 1fr; gap: 1rem; padding: .8rem 0; border-bottom: 1px solid var(--line); }}
  .ev time {{ font-weight: 700; }}
  .ev b {{ display: block; }}
  .ev span {{ color: var(--mut); font-size: .92rem; }}
  @media (max-width: 560px) {{ .ev li {{ grid-template-columns: 1fr; gap: .2rem; }} }}
</style></head>
<body><div class="wrap">
<a class="back" href="../">← Shi Mizu Dojo</a>
<h1>Events</h1>
<p class="lede">Judo and jiu jitsu tournaments, seminars and courses in BC and Alberta, plus our own club events. Subscribe once and new events show up in your calendar automatically. The list is updated monthly; always check the organiser's page before you travel.</p>
<p><b>Weekly classes</b> (in the calendar too): Tuesdays and Thursdays at 52 Ridge, Clearwater Valley Resort. Kids 5:00 pm, adults 6:00–7:30 pm.</p>
{subscribe_html()}
{body}
<p class="mut" style="margin-top:2rem">Know of an event we're missing? Email <a href="mailto:clearwaterjiujitsu@icloud.com">clearwaterjiujitsu@icloud.com</a>.</p>
</div></body></html>
"""
    out = ROOT / "events" / "index.html"
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(page, encoding="utf-8")
    return len(items)


if __name__ == "__main__":
    c, x = build_ics()
    n = build_page()
    print(f"events.ics: {c} club + {x} external entries; events page lists {n} upcoming")
