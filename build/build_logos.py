"""20 logo concepts for Shi Mizu Dojo, as a contact sheet page: site/logos/index.html
Run: python build/build_logos.py"""
import math
from pathlib import Path

OUT = Path(__file__).resolve().parent.parent / "site" / "logos" / "index.html"
BLUE, DEEP, KIN, RED, INK = "#0556A8", "#033E78", "#EEE9DD", "#C8402A", "#141618"
MINCHO = "Shippori Mincho B1, serif"
BRUSH = "Yuji Boku, Shippori Mincho B1, serif"
SANS = "Archivo, sans-serif"


def svg(body, vb="0 0 200 200"):
    return f'<svg viewBox="{vb}" xmlns="http://www.w3.org/2000/svg">{body}</svg>'


def t(x, y, s, size, fill, font=MINCHO, weight=800, anchor="middle", extra=""):
    return (f'<text x="{x}" y="{y}" font-family="{font}" font-size="{size}" font-weight="{weight}" '
            f'fill="{fill}" text-anchor="{anchor}" {extra}>{s}</text>')


def seal2x2(fill, ink, rx=12, font=MINCHO, size=50):
    return (f'<rect x="20" y="20" width="160" height="160" rx="{rx}" fill="{fill}"/>'
            f'<rect x="31" y="31" width="138" height="138" rx="{max(rx-6,2)}" fill="none" stroke="{ink}" stroke-width="3.5"/>'
            + t(136, 95, "清", size, ink, font) + t(136, 160, "水", size, ink, font)
            + t(64, 95, "道", size, ink, font) + t(64, 160, "場", size, ink, font))


def ring_text(text, r, size, fill, start=-90, spread=360):
    out = []
    n = len(text)
    for i, ch in enumerate(text):
        a = math.radians(start + spread * i / n)
        x, y = 100 + r * math.cos(a), 100 + r * math.sin(a)
        rot = start + spread * i / n + 90
        out.append(f'<text x="{x:.2f}" y="{y:.2f}" font-family="{SANS}" font-size="{size}" font-weight="800" fill="{fill}" '
                   f'text-anchor="middle" dominant-baseline="central" transform="rotate({rot:.2f} {x:.2f} {y:.2f})">{ch}</text>')
    return "".join(out)


def arc_bottom(text, r, size, fill, span=110):
    """Text along the bottom of a circle, upright and reading left to right."""
    out, n = [], len(text)
    for i, ch in enumerate(text):
        ang = 90 + span / 2 - span * i / (n - 1)
        a = math.radians(ang)
        x, y = 100 + r * math.cos(a), 100 + r * math.sin(a)
        out.append(f'<text x="{x:.2f}" y="{y:.2f}" font-family="{SANS}" font-size="{size}" font-weight="800" fill="{fill}" '
                   f'text-anchor="middle" dominant-baseline="central" transform="rotate({ang - 90:.2f} {x:.2f} {y:.2f})">{ch}</text>')
    return "".join(out)


C = []  # (name, idea, svg)

C.append(("Hanko", "The four kanji 清水道場 in a square vermilion seal: the classic stamp on scrolls and certificates.", svg(seal2x2(RED, KIN))))

C.append(("Round seal", "清水 stacked in a round seal. Reads well tiny, as a stamp on posters and belts.",
          svg(f'<circle cx="100" cy="100" r="84" fill="{RED}"/><circle cx="100" cy="100" r="72" fill="none" stroke="{KIN}" stroke-width="3"/>'
              + t(100, 100, "清", 58, KIN) + t(100, 158, "水", 58, KIN))))

C.append(("Ensō 柔", "A single brushed circle around 柔 (jū, “gentle”), the root of both judo and jiu jitsu.",
          svg(f'<path d="M154 62 A66 66 0 1 0 160 118" fill="none" stroke="{BLUE}" stroke-width="16" stroke-linecap="round"/>'
              f'<path d="M150 56 A66 66 0 0 1 162 96" fill="none" stroke="{BLUE}" stroke-width="7" stroke-linecap="round" opacity=".7"/>'
              + t(100, 124, "柔", 76, INK, BRUSH, 400))))

C.append(("Drop", "A drop of clear water with 清 (clear) inside. Simple enough for a patch or a favicon.",
          svg(f'<path d="M100 18 C130 62 160 92 160 126 A60 60 0 0 1 40 126 C40 92 70 62 100 18 Z" fill="{BLUE}"/>'
              + t(100, 156, "清", 72, KIN))))

C.append(("Seigaiha", "Three stacked wave arcs (the seigaiha pattern) over a quiet wordmark.",
          svg("".join(f'<circle cx="{cx}" cy="112" r="{r}" fill="none" stroke="{BLUE}" stroke-width="5"/>' for cx in (64, 136) for r in (36, 24, 12))
              + f'<rect x="0" y="112" width="200" height="88" fill="#fff"/>'
              + "".join(f'<circle cx="100" cy="124" r="{r}" fill="#fff" stroke="{BLUE}" stroke-width="5"/>' for r in (40,))
              + "".join(f'<circle cx="100" cy="124" r="{r}" fill="none" stroke="{BLUE}" stroke-width="5"/>' for r in (28, 16))
              + f'<rect x="0" y="124" width="200" height="76" fill="#fff"/>'
              + t(100, 160, "SHI MIZU", 26, INK, SANS, 800, extra='letter-spacing="3"') + t(100, 182, "DOJO", 14, BLUE, SANS, 700, extra='letter-spacing="8"'))))

C.append(("Obi knot", "A tied belt seen front-on: the one object every student shares.",
          svg(f'<rect x="18" y="78" width="164" height="30" rx="4" fill="{BLUE}"/>'
              f'<path d="M86 96 L58 168 L82 172 L100 112 Z" fill="{BLUE}"/><path d="M114 96 L142 168 L118 172 L100 112 Z" fill="{DEEP}"/>'
              f'<rect x="80" y="70" width="40" height="46" rx="6" fill="{DEEP}"/><rect x="80" y="70" width="40" height="46" rx="6" fill="none" stroke="{KIN}" stroke-width="2.5"/>'
              f'<rect x="132" y="78" width="30" height="30" fill="{INK}"/>')))

C.append(("SM monogram", "S and M in a square seal over a red belt line, for when the kanji are too small to read.",
          svg(f'<rect x="20" y="20" width="160" height="160" rx="10" fill="{BLUE}"/>'
              + t(66, 132, "S", 82, KIN, MINCHO, 800) + t(124, 132, "M", 82, KIN, MINCHO, 800)
              + f'<rect x="40" y="146" width="120" height="4" fill="{RED}"/>')))

C.append(("Ripple crest", "A family-crest (kamon) circle of ripples from a single drop.",
          svg(f'<circle cx="100" cy="100" r="86" fill="{BLUE}"/>'
              + "".join(f'<circle cx="100" cy="100" r="{r}" fill="none" stroke="{KIN}" stroke-width="{w}"/>' for r, w in ((64, 4), (46, 5), (28, 6)))
              + f'<circle cx="100" cy="100" r="10" fill="{KIN}"/>')))

C.append(("Falls", "Mountain and waterfall in one continuous line, for the valley the club trains in.",
          svg(f'<circle cx="100" cy="100" r="82" fill="none" stroke="{BLUE}" stroke-width="6"/>'
              f'<path d="M30 132 L74 74 L96 100 L120 62 L170 132" fill="none" stroke="{BLUE}" stroke-width="6" stroke-linejoin="round"/>'
              f'<path d="M100 92 L100 150 M110 96 L110 150" stroke="{BLUE}" stroke-width="4" stroke-linecap="round"/>'
              f'<path d="M60 160 Q100 148 140 160" fill="none" stroke="{BLUE}" stroke-width="5" stroke-linecap="round"/>')))

C.append(("Nobori", "A tall dojo banner (nobori) with 清水: works as a vertical sign or a shirt print.",
          svg(f'<rect x="58" y="14" width="6" height="176" fill="{INK}"/><rect x="64" y="22" width="80" height="160" fill="{BLUE}"/>'
              f'<rect x="64" y="22" width="80" height="14" fill="{RED}"/>' + t(104, 96, "清", 54, KIN) + t(104, 160, "水", 54, KIN))))

C.append(("Grip", "Two interlocking hooks, like two partners gripping (kumikata). One blue, one red.",
          svg(f'<path d="M40 40 H120 V80 H80 V160 H40 Z" fill="{BLUE}"/><path d="M160 160 H80 V120 H120 V40 H160 Z" fill="{RED}"/>')))

C.append(("Lapel", "The crossed collar of a gi, closed by the belt line.",
          svg(f'<path d="M40 30 L100 120 L160 30" fill="none" stroke="{BLUE}" stroke-width="22" stroke-linejoin="miter"/>'
              f'<path d="M60 30 L100 92 L140 30" fill="none" stroke="#fff" stroke-width="5"/>'
              f'<rect x="30" y="132" width="140" height="22" fill="{INK}"/><rect x="92" y="126" width="16" height="34" fill="{INK}"/>')))

C.append(("水 brush", "One brushed character, 水 (water), with a small red seal. Quiet and confident.",
          svg(t(96, 150, "水", 130, BLUE, BRUSH, 400) + f'<rect x="146" y="150" width="20" height="20" rx="2" fill="{RED}"/>')))

C.append(("Clear line", "A circle split by one wave: water below, clear air above.",
          svg(f'<clipPath id="c14"><circle cx="100" cy="100" r="80"/></clipPath>'
              f'<g clip-path="url(#c14)"><rect width="200" height="200" fill="#fff"/>'
              f'<path d="M0 110 Q50 86 100 110 T200 110 V200 H0 Z" fill="{BLUE}"/></g>'
              f'<circle cx="100" cy="100" r="80" fill="none" stroke="{BLUE}" stroke-width="6"/>')))

C.append(("Kikkō", "A tortoiseshell hexagon (endurance in Japanese pattern language) around 清.",
          svg('<polygon points="100,22 168,61 168,139 100,178 32,139 32,61" fill="none" stroke="%s" stroke-width="6"/>' % BLUE
              + '<polygon points="100,38 154,69 154,131 100,162 46,131 46,69" fill="none" stroke="%s" stroke-width="2.5"/>' % BLUE
              + t(100, 128, "清", 70, INK))))

C.append(("River stone", "A smooth stone carved with the four kanji: steady, local, a little rugged.",
          svg(f'<path d="M96 14 C142 12 184 40 188 90 C192 142 158 186 104 190 C50 194 12 160 12 108 C12 56 48 16 96 14 Z" fill="{DEEP}"/>'
              + t(132, 96, "清", 54, KIN, BRUSH, 400) + t(132, 160, "水", 54, KIN, BRUSH, 400)
              + t(68, 96, "道", 54, KIN, BRUSH, 400) + t(68, 160, "場", 54, KIN, BRUSH, 400)
              + f'<rect x="150" y="160" width="12" height="12" rx="2" fill="{RED}"/>')))

C.append(("Belt tip", "The end of a blue belt with its rank bar and four stripes of tape.",
          svg(f'<rect x="10" y="74" width="180" height="52" fill="{BLUE}"/><rect x="104" y="74" width="62" height="52" fill="{INK}"/>'
              + "".join(f'<rect x="{112 + i*12}" y="74" width="6" height="52" fill="#fff"/>' for i in range(4)))))

C.append(("Ripple wordmark", "The name set plainly, with three ripple lines under it.",
          svg(t(100, 96, "Shi Mizu", 40, INK, MINCHO, 800) + t(100, 122, "DOJO · CLEARWATER", 11, BLUE, SANS, 700, extra='letter-spacing="3"')
              + "".join(f'<path d="M{100-w} {140+i*10} Q100 {132+i*10} {100+w} {140+i*10}" fill="none" stroke="{BLUE}" stroke-width="3" stroke-linecap="round"/>' for i, w in enumerate((60, 44, 28))))))

C.append(("Badge", "A round badge: the full name around 清水. Good for patches and the back of a gi.",
          svg(f'<circle cx="100" cy="100" r="94" fill="{BLUE}"/><circle cx="100" cy="100" r="62" fill="{KIN}"/>'
              + ring_text("SHI MIZU DOJO", 77, 13, KIN, start=-145, spread=110 * 13 / 12)
              + arc_bottom("CLEARWATER BC", 85, 12, KIN)
              + f'<circle cx="26" cy="104" r="3" fill="{KIN}"/><circle cx="174" cy="104" r="3" fill="{KIN}"/>'
              + t(100, 98, "清", 46, BLUE) + t(100, 146, "水", 46, BLUE))))

C.append(("Tatami", "A square of tatami laid in the traditional pattern, with 清 on the centre mat.",
          svg(f'<rect x="24" y="24" width="152" height="152" fill="{KIN}" stroke="{BLUE}" stroke-width="6"/>'
              f'<path d="M24 74 H126 M126 24 V126 M74 126 V176 M126 126 H176" stroke="{BLUE}" stroke-width="5"/>'
              f'<rect x="74" y="74" width="52" height="52" fill="{BLUE}"/>' + t(100, 116, "清", 40, KIN))))

cards = "".join(
    f'<figure><div class="art">{s}</div><div class="mini">{s}</div>'
    f'<figcaption><b>{i:02d} · {n}</b><span>{d}</span></figcaption></figure>'
    for i, (n, d, s) in enumerate(C, 1))

OUT.parent.mkdir(parents=True, exist_ok=True)
OUT.write_text(f"""<!doctype html>
<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">
<title>Logo Concepts · Shi Mizu Dojo</title><meta name="robots" content="noindex">
<link href="https://fonts.googleapis.com/css2?family=Archivo:wdth,wght@62..125,100..900&family=Shippori+Mincho+B1:wght@400;800&family=Yuji+Boku&display=swap" rel="stylesheet">
<style>
  * {{ box-sizing: border-box; }}
  body {{ margin: 0; background: #EDEBE6; color: {INK}; font: 400 15px/1.45 Archivo, system-ui, sans-serif; }}
  header {{ max-width: 1400px; margin: 0 auto; padding: 32px 24px 8px; }}
  h1 {{ margin: 0 0 6px; font-size: 30px; font-stretch: 115%; font-weight: 800; letter-spacing: -0.02em; }}
  header p {{ margin: 0; color: #55555B; max-width: 60rem; }}
  .sheet {{ max-width: 1400px; margin: 0 auto; padding: 20px 24px 48px; display: grid; grid-template-columns: repeat(5, 1fr); gap: 16px; }}
  figure {{ margin: 0; background: #fff; border: 1px solid rgba(0,0,0,.08); display: grid; grid-template-rows: auto auto 1fr; }}
  .art {{ padding: 22px 30px 8px; }}
  .art svg {{ display: block; width: 100%; height: auto; }}
  .mini {{ display: flex; justify-content: flex-end; padding: 0 12px; height: 32px; }}
  .mini svg {{ width: 32px; height: 32px; }}
  figcaption {{ padding: 10px 14px 14px; border-top: 1px solid rgba(0,0,0,.07); }}
  figcaption b {{ display: block; font-size: 14px; }}
  figcaption span {{ font-size: 12.5px; color: #55555B; }}
  @media (max-width: 1100px) {{ .sheet {{ grid-template-columns: repeat(3, 1fr); }} }}
  @media (max-width: 640px) {{ .sheet {{ grid-template-columns: repeat(2, 1fr); }} }}
</style></head><body>
<header><h1>Shi Mizu Dojo · 20 logo concepts</h1>
<p>Judo-gi blue {BLUE}, vermilion {RED}, cotton {KIN}. The small mark at the bottom right of each card is the same logo at 32 px, to show how it holds up as an app icon or favicon. Pick a few favourites and we'll refine them.</p></header>
<main class="sheet">{cards}</main>
</body></html>
""", encoding="utf-8")
print("wrote", OUT, len(C), "concepts")
