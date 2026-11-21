"""Builds the three homepage versions (tenugui, stone, stripe) from one shared structure.
Run:  python build/build_site.py   (writes site/<theme>/index.html; needs node for the logo marks)"""
import json
import subprocess
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import build_events  # noqa: E402

ROOT = Path(__file__).resolve().parent.parent / "site"
MARKS = json.loads(subprocess.run(["node", str(Path(__file__).with_name("brand_dump.js"))],
                                  capture_output=True, text=True, encoding="utf-8", check=True).stdout)
LEARN = [("counting", "Counting to ten"), ("judo-belts", "Judo belt ranks"),
         ("bjj-belts", "Jiu jitsu belt ranks"), ("two-names", "Same move, two names")]

CLUB, CLUB_SUB = "Shi Mizu Dojo", "Clearwater Martial Arts"
CTA = "Book your first class"
EMAIL = "clearwaterjiujitsu@icloud.com"
PHONE, PHONE_TEL = "+1 (780) 720-1705", "+17807201705"
WHATSAPP = "https://chat.whatsapp.com/CLJdBec0hAzFXTIkviskQX"
VENUE, ADDRESS = "52 Ridge · Clearwater Valley Resort", "373 Clearwater Valley Rd, Clearwater, BC"
MAP_EMBED = "https://www.google.com/maps?q=Clearwater+Valley+Resort,+373+Clearwater+Valley+Rd,+Clearwater,+BC&z=14&output=embed"
MAP_LINK = "https://www.google.com/maps/search/?api=1&query=Clearwater+Valley+Resort+373+Clearwater+Valley+Rd+Clearwater+BC"

FONTS = ("https://fonts.googleapis.com/css2?family=Archivo:wdth,wght@62..125,100..900"
         "&family=Figtree:wght@400;600;700;800&family=Shippori+Mincho+B1:wght@400;700;800"
         "&family=Zen+Kaku+Gothic+New:wght@400;500;700;900&family=Yuji+Boku&family=Zen+Antique&display=swap")

# Ernst's photos from his Alberta club (site/assets/photos). name: (width, height, alt)
PHOTOS = {
    "koshi-guruma": (876, 1280, "A judoka in a blue gi throws a partner in white over the hip in koshi-guruma."),
    "o-uchi-gari": (1102, 1280, "Two judoka with green belts mid-throw: a major inner reap, o-uchi-gari."),
    "juji-gatame-guard": (1280, 1011, "From her back, a grappler in blue controls her partner's arm from guard."),
    "groundwork-pin": (1280, 1064, "A judoka in blue pins her partner on the mat and controls his arm."),
    "youth-throw": (640, 409, "A young judoka with a yellow belt is thrown mid-air during practice."),
    "grading-group": (480, 562, "Five judoka in gis, kneeling and standing in front of the dojo wall after a grading."),
}
GALLERY = ["koshi-guruma", "o-uchi-gari", "juji-gatame-guard", "groundwork-pin", "youth-throw"]

# The hero uses the generated canyon loop; its first frame shows when motion is reduced or before it loads.
HERO_VIDEO = True


def img(name, lazy=True):
    w, h, alt = PHOTOS[name]
    load = ' loading="lazy" decoding="async"' if lazy else ' fetchpriority="high"'
    return f'<img src="../assets/photos/{name}.webp" width="{w}" height="{h}" alt="{alt}"{load}>'


THEMES = {
    "tenugui": {
        "label": "Tenugui",
        "color": "#0556A8",
        "h1": "Clearwater Mixed Martial Arts",
        "lede": "Judo and Brazilian jiu jitsu for kids and adults, every Tuesday and Thursday at 52 Ridge, Clearwater Valley Resort. Taught by Ernst Bergmann. Beginners welcome.",
    },
    "stone": {
        "label": "Stone & Water",
        "color": "#141618",
        "h1": "Clearwater Mixed Martial Arts",
        "lede": "Judo and Brazilian jiu jitsu in Clearwater, BC. Kids at 5 pm and adults from 6 to 7:30 pm, every Tuesday and Thursday at 52 Ridge.",
    },
    "stripe": {
        "label": "Stripe",
        "color": "#16161A",
        "h1": "Clearwater Mixed<br>Martial Arts",
        "lede": "Judo and Brazilian jiu jitsu on Tuesdays and Thursdays at 52 Ridge, Clearwater Valley Resort. Kids class at 5 pm, adults from 6 to 7:30 pm. $100 a month.",
    },
}

SCHEDULE = [("Tuesday", [("5:00 pm", "Kids"), ("6:00 – 7:30 pm", "Adults")]),
            ("Thursday", [("5:00 pm", "Kids"), ("6:00 – 7:30 pm", "Adults")])]

FIRST = [
    ("Send us a message", "Tell us who's coming and which class. We'll confirm and send the waiver."),
    ("Arrive ten minutes early", "Sign the waiver, meet Ernst and see where to change. Parents are welcome to stay and watch."),
    ("Wear gym clothes", "T-shirt, shorts or track pants with no zips or buttons. Bring water and sandals for off the mat. No gi needed yet."),
    ("Train", "Bow in, warm up, learn to fall, learn one technique, then try it with a partner at your own pace."),
]

FAQ = [
    ("Do I need to be fit or have any experience?", "No. Most people start with no experience. You'll get fitter by training, and you always train at your own pace."),
    ("What's the difference between judo and jiu jitsu?", "Judo is mostly standing: throws, then pins. Brazilian jiu jitsu is mostly on the ground: control and submissions. Jiu jitsu grew out of judo about a hundred years ago, so they fit together naturally."),
    ("Is it safe?", "Everyone learns to fall before they learn to throw, and everyone learns to tap. Rounds are supervised and partners are matched by size and experience."),
    ("How much does it cost?", "$100 a month. Family discounts are available; ask us."),
    ("Do I need a gi, and where can I buy one?", "Not to start: gym clothes are fine for your first few classes. When you're ready, one plain white gi works for both arts while you're learning; a single-weave judo gi is fine for jiu jitsu. Expect about $90–160 for an adult gi and $40–90 for a child's. Canadian sellers avoid duty and cross-border shipping surprises: "
     '<a href="https://www.fushida.ca" rel="noopener">Fushida</a> (Vancouver), <a href="https://bushido.ca" rel="noopener">Bushido</a> (Langley), <a href="https://matsuru.ca" rel="noopener">Matsuru</a>, '
     '<a href="https://www.kingzkimonos.ca" rel="noopener">Kingz Canada</a> and <a href="https://stonebelt.ca" rel="noopener">Stonebelt</a>. '
     "Cotton gis shrink 3–5%, so use the brand's size chart, size up if you're between sizes, wash cold and hang to dry. Ask Ernst before you buy and he'll help with sizing."),
    ("Can I drop in while visiting Wells Gray?", "Yes. Visitors, seasonal workers and crews in town for the summer are welcome. Message us before you come."),
]


def hero_band():
    """Generated canyon loop (stabilized, seamless) over its first frame, with 清水 set as text
    where the characters sat in the original image. The SVG uses the same 1280x720 frame and
    'slice' scaling as the video's object-fit: cover, so the text stays locked to the picture."""
    video = ('<video muted loop playsinline preload="none" poster="../assets/video/canyon-poster.webp">'
             '<source src="../assets/video/canyon-loop-v2.mp4" type="video/mp4"></video>') if HERO_VIDEO else ''
    pause = '<button class="hero-pause" type="button" hidden>Pause video</button>' if HERO_VIDEO else ''
    kanji = ('<svg class="hero-kanji" viewBox="0 0 1280 720" preserveAspectRatio="xMidYMid slice" aria-hidden="true">'
             '<defs><filter id="kshadow" x="-20%" y="-20%" width="140%" height="140%"><feDropShadow dx="0" dy="3" stdDeviation="7" flood-color="#000" flood-opacity=".35"/></filter></defs>'
             '<g filter="url(#kshadow)" text-anchor="middle" dominant-baseline="central" font-family="Yuji Boku, Shippori Mincho B1, serif" font-size="262">'
             '<text x="1123" y="225">清</text><text x="1123" y="480">水</text></g></svg>')
    return ('<div class="hero-band"><div class="hero-media" aria-hidden="true">'
            '<img src="../assets/video/canyon-poster.webp" width="1280" height="720" alt="" fetchpriority="high">'
            f'{video}</div>{kanji}{pause}</div>')


def page(theme):
    t = THEMES[theme]
    others = [k for k in THEMES if k != theme]
    sched = "".join(
        f'<div class="day"><h3>{d}</h3>' + "".join(f'<p><span class="cls">{c}</span><b>{tm}</b></p>' for tm, c in cls) + "</div>"
        for d, cls in SCHEDULE)
    first = "".join(f'<li><h3>{h}</h3><p>{p}</p></li>' for h, p in FIRST)
    faq = "".join(f'<details><summary>{q}</summary><p>{a}</p></details>' for q, a in FAQ)
    learn = "".join(
        f'<a class="learn-card" href="../posters/?theme={theme}&amp;p={pid}">'
        f'<img src="../posters/thumbs/{theme}-{pid}.webp" width="600" height="800" loading="lazy" decoding="async" alt="{title} poster"></a>'
        for pid, title in LEARN)
    gallery = "".join(f'<li>{img(n)}</li>' for n in GALLERY)
    asanoha_attr = MARKS['asanoha'].replace('"', '&quot;')
    root_style = f' style="--asanoha: {asanoha_attr}"' if theme == 'tenugui' else ''
    nav_mark, foot_mark = MARKS[theme]['nav'], MARKS[theme]['foot']
    switch = " ".join(f'<a href="../{k}/">{THEMES[k]["label"]}</a>' for k in others)
    ev = build_events.upcoming(6)
    ev_list = ''.join(build_events.row_html(e) for e in ev) or '<li class="ev-empty">New events are added every month.</li>'
    NAV = ('<a href="#schedule">Schedule</a><a href="#events">Events</a><a href="#pricing">Pricing</a><a href="#first">First class</a>'
           '<a href="#coach">Coach</a><a href="#learn">Learn</a><a href="#visit">Find us</a>')

    return f"""<!doctype html>
<html lang="en"{root_style}>
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{CLUB} · {CLUB_SUB} · {t['label']} direction</title>
<meta name="robots" content="noindex">
<meta name="description" content="Judo and Brazilian jiu jitsu for kids and adults at 52 Ridge, Clearwater Valley Resort, Clearwater BC. Tuesdays and Thursdays.">
<meta name="theme-color" content="{t['color']}">
<meta property="og:title" content="{CLUB} · {CLUB_SUB}">
<meta property="og:description" content="Judo and Brazilian jiu jitsu in Clearwater, BC. Tuesdays and Thursdays at 52 Ridge.">
<meta property="og:image" content="https://jiujitsu.designspore.co/assets/generated/falls-shimizu-1000.webp">
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="{FONTS}" rel="stylesheet">
<link rel="stylesheet" href="../assets/site-base.css">
<link rel="stylesheet" href="style.css">
<script type="application/ld+json">{{"@context":"https://schema.org","@type":"SportsActivityLocation","name":"{CLUB}","sport":["Brazilian jiu jitsu","Judo"],"email":"{EMAIL}","telephone":"{PHONE_TEL}","address":{{"@type":"PostalAddress","streetAddress":"373 Clearwater Valley Rd","addressLocality":"Clearwater","addressRegion":"BC","addressCountry":"CA"}}}}</script>
</head>
<body class="th-{theme}">
<a class="skip" href="#main">Skip to content</a>
<div class="proto">Design direction: <b>{t['label']}</b> · also see {switch} · <a href="../">compare all</a></div>
<header class="nav">
  <a class="brand" href="#top" aria-label="{CLUB}, {CLUB_SUB}, home"><span class="brand-mark" aria-hidden="true">{nav_mark}</span><span class="brand-word"><b>{CLUB}</b><span>{CLUB_SUB}</span></span></a>
  <nav class="nav-links" aria-label="Main">{NAV}</nav>
  <a class="btn btn-nav" href="#contact">{CTA}</a>
  <details class="menu"><summary aria-label="Open section menu"><span aria-hidden="true">Menu</span></summary><nav aria-label="Sections">{NAV}</nav></details>
</header>

<main id="main">
<section class="hero" id="top">
  <div class="hero-text">
    <h1>{t['h1']}</h1>
    <p class="lede">{t['lede']}</p>
    <div class="ctas"><a class="btn" href="#contact">{CTA}</a><a class="btn btn-ghost" href="#schedule">See the schedule</a></div>
  </div>
  {hero_band()}
  {'<div class="hero-belt" aria-hidden="true"><span class="hb-bar"><i></i><i></i><i></i><i></i></span></div>' if theme == 'stripe' else ''}
</section>

<section class="sec schedule" id="schedule">
  <div class="sec-head"><h2>Schedule</h2><p>Every week at {VENUE}.</p></div>
  <div class="week">{sched}</div>
</section>

<section class="sec events" id="events">
  <div class="sec-head"><h2>Events</h2><p>Judo and jiu jitsu tournaments, seminars and courses in BC and Alberta, plus our own club events. Subscribe and they show up in your calendar.</p></div>
  <ul class="ev">{ev_list}</ul>
  {build_events.subscribe_html().replace('../events.ics', '../events.ics')}
  <p class="small"><a href="../events/">All events</a></p>
</section>

<section class="sec gallery" id="mat">
  <div class="sec-head"><h2>On the mat</h2><p>Photos from Ernst's previous club in Rocky Mountain House, Alberta.</p></div>
  <ul class="gallery-list">{gallery}</ul>
</section>

<section class="sec two" id="arts">
  <div class="sec-head"><h2>Judo and jiu jitsu</h2></div>
  <div class="two-grid">
    <div class="art"><p class="art-jp" lang="ja">柔道</p><h3>Judo</h3><p>“The gentle way.” Founded in Tokyo in 1882 by Jigorō Kanō. You learn to fall safely, to break someone's balance and to throw, then to pin. An Olympic sport since 1964.</p></div>
    <div class="art"><p class="art-jp" lang="ja">柔術</p><h3>Brazilian jiu jitsu</h3><p>“The gentle art.” Judo master Mitsuyo Maeda taught it to the Gracie family in Brazil around 1917, and they built it into a complete ground game, where leverage lets a smaller person control a bigger one.</p></div>
    <p class="two-note">Both share the same root, 柔 (jū): give way to force, then redirect it.</p>
  </div>
</section>

<section class="sec pricing" id="pricing">
  <div class="sec-head"><h2>Pricing</h2></div>
  <div class="price-card"><p class="price">$100<span> / month</span></p><p>Family discounts are available. Ask us about them.</p></div>
  <p class="fund">BC families can apply to <a href="https://kidsportcanada.ca/british-columbia/" rel="noopener">KidSport BC</a> or <a href="https://jumpstart.canadiantire.ca/" rel="noopener">Canadian Tire Jumpstart</a> for help with fees.</p>
</section>

<section class="sec first" id="first">
  <div class="sec-head"><h2>Your first class</h2></div>
  <ol class="steps">{first}</ol>
</section>

<section class="sec coach" id="coach">
  <figure class="coach-photo">{img("grading-group")}<figcaption>Grading day at Kuroi Ishi Judo &amp; Jiu Jitsu, Rocky Mountain House, Alberta.</figcaption></figure>
  <div class="coach-text">
    <h2>Your coach</h2>
    <p class="coach-name">Ernst Bergmann · [ranks TBC]</p>
    <p>Ernst taught judo and Brazilian jiu jitsu at Kuroi Ishi (<span lang="ja">黒い石</span>, “black stone”) in Rocky Mountain House, Alberta, including self-defence for women and private lessons. He now lives in the Upper Clearwater Valley.</p>
    <p class="small">[A few words in Ernst's own voice, his ranks and lineage, and certifications to come.]</p>
  </div>
</section>

<section class="sec learn" id="learn">
  <div class="sec-head"><h2>The dojo library</h2><p>The posters on our walls: counting in Japanese, belt ranks, dojo words, throws, groundwork and where it all came from.</p></div>
  <div class="learn-grid">{learn}</div>
  <a class="btn" href="../posters/?theme={theme}">See all twelve posters</a>
</section>

<section class="sec visit" id="visit">
  <div class="visit-text">
    <h2>Find us</h2>
    <p class="addr"><b>{VENUE}</b><br>{ADDRESS}</p>
    <p>On Clearwater Valley Road, the road into Wells Gray Park.</p>
    <p>Coming from Birch Island, Vavenby, Blackpool or Little Fort? Ask about carpooling. In winter, check <a href="https://www.drivebc.ca/" rel="noopener">DriveBC</a> before you head out.</p>
    <a class="btn btn-ghost" href="{MAP_LINK}" rel="noopener">Open in Google Maps</a>
  </div>
  <iframe class="map" title="Map of {VENUE}, {ADDRESS}" src="{MAP_EMBED}" loading="lazy" referrerpolicy="no-referrer-when-downgrade" allowfullscreen></iframe>
</section>

<section class="sec faq" id="faq">
  <div class="sec-head"><h2>Questions</h2></div>
  <div class="faq-list">{faq}</div>
</section>

<section class="sec contact" id="contact">
  <h2>Contact</h2>
  <p>Message us to book a first class or ask a question. Parents are welcome to come and watch.</p>
  <dl class="contact-row">
    <div><dt>Email</dt><dd><a href="mailto:{EMAIL}">{EMAIL}</a></dd></div>
    <div><dt>Phone or text</dt><dd><a href="tel:{PHONE_TEL}">{PHONE}</a></dd></div>
    <div><dt>WhatsApp</dt><dd><a href="{WHATSAPP}" rel="noopener">Join the club group</a></dd></div>
  </dl>
</section>
</main>

<footer class="foot">
  <span class="foot-mark" aria-hidden="true">{foot_mark}</span>
  <p><b>{CLUB} · {CLUB_SUB}</b><br>{VENUE} · Clearwater, BC</p>
  <p class="small"><a href="mailto:{EMAIL}">{EMAIL}</a> · <a href="tel:{PHONE_TEL}">{PHONE}</a> · <a href="../posters/?theme={theme}">Posters</a></p>
</footer>

<script>
  // Close the phone menu after a section link is chosen.
  const menu = document.querySelector(".menu");
  menu.addEventListener("click", (e) => {{ if (e.target.closest("a")) menu.open = false; }});
  // Hero video: plays over the still only when motion is allowed, with a pause control.
  const media = document.querySelector(".hero-media"), video = media && media.querySelector("video"), pause = document.querySelector(".hero-pause");
  if (video && !matchMedia("(prefers-reduced-motion: reduce)").matches) {{
    video.preload = "auto";
    video.play().then(() => {{ media.classList.add("is-video"); pause.hidden = false; }}).catch(() => {{}});
    pause.addEventListener("click", () => {{
      if (video.paused) {{ video.play(); pause.textContent = "Pause video"; }} else {{ video.pause(); pause.textContent = "Play video"; }}
    }});
  }}
</script>
</body>
</html>
"""


for theme in THEMES:
    out = ROOT / theme / "index.html"
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(page(theme), encoding="utf-8")
    print("wrote", out.relative_to(ROOT))
