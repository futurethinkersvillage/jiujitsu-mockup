"""Logo round 2: 18 concepts growing out of round 1's #14 (Clear line) and #17 (Belt tip).
Run: python build/build_logos2.py  -> site/logos/round-2/index.html"""
from pathlib import Path

OUT = Path(__file__).resolve().parent.parent / "site" / "logos" / "round-2" / "index.html"
BLUE, DEEP, KIN, RED, INK, W = "#0556A8", "#033E78", "#EEE9DD", "#C8402A", "#141618", "#FFFFFF"
MINCHO, BRUSH, SANS = "Shippori Mincho B1, serif", "Yuji Boku, serif", "Archivo, sans-serif"
WAVE = "M-10 110 Q45 84 100 110 T210 110"           # the round-1 wave, extended past the frame


def svg(body):
    return f'<svg viewBox="0 0 200 200" xmlns="http://www.w3.org/2000/svg">{body}</svg>'


def t(x, y, s, size, fill, font=MINCHO, weight=800, extra=""):
    return f'<text x="{x}" y="{y}" font-family="{font}" font-size="{size}" font-weight="{weight}" fill="{fill}" text-anchor="middle" {extra}>{s}</text>'


def stripes(x, y, h, n=4, w=6, gap=12, fill=W):
    return "".join(f'<rect x="{x + i*gap}" y="{y}" width="{w}" height="{h}" fill="{fill}"/>' for i in range(n))


def circle_clip(i, inner, r=80, stroke=6, color=BLUE):
    return (f'<clipPath id="k{i}"><circle cx="100" cy="100" r="{r}"/></clipPath><g clip-path="url(#k{i})">{inner}</g>'
            f'<circle cx="100" cy="100" r="{r}" fill="none" stroke="{color}" stroke-width="{stroke}"/>')


REF = [
    ("14 · Clear line", circle_clip(0, f'<rect width="200" height="200" fill="{W}"/><path d="{WAVE} V210 H-10 Z" fill="{BLUE}"/>')),
    ("17 · Belt tip", f'<rect x="10" y="74" width="180" height="52" fill="{BLUE}"/><rect x="104" y="74" width="62" height="52" fill="{INK}"/>' + stripes(112, 74, 52)),
]

C = []
# ---- From the wave circle (14) ----
C.append(("Clear line 清水", "The wave circle with 清水 set in the clear air above the water.",
          circle_clip(1, f'<rect width="200" height="200" fill="{W}"/><path d="M-10 128 Q45 104 100 128 T210 128 V210 H-10 Z" fill="{BLUE}"/>'
                      + t(100, 96, "清水", 50, INK))))
C.append(("Two currents", "Two waves inside the circle: one darker, one lighter, like deep and shallow water.",
          circle_clip(2, f'<rect width="200" height="200" fill="{W}"/><path d="M-10 96 Q45 72 100 96 T210 96 V210 H-10 Z" fill="#7FA9D8"/>'
                      f'<path d="M-10 124 Q45 100 100 124 T210 124 V210 H-10 Z" fill="{BLUE}"/>')))
C.append(("Seal wave", "The same wave in a rounded-square seal, so it sits like a stamp.",
          f'<clipPath id="k3"><rect x="22" y="22" width="156" height="156" rx="30"/></clipPath><g clip-path="url(#k3)">'
          f'<rect width="200" height="200" fill="{W}"/><path d="{WAVE} V210 H-10 Z" fill="{BLUE}"/></g>'
          f'<rect x="22" y="22" width="156" height="156" rx="30" fill="none" stroke="{BLUE}" stroke-width="6"/>'
          f'<rect x="140" y="40" width="20" height="20" rx="3" fill="{RED}"/>'))
C.append(("Falls into the line", "A waterfall drops from the top of the circle into the water.",
          circle_clip(4, f'<rect width="200" height="200" fill="{W}"/><path d="M20 58 H96 V112 H20 Z" fill="{BLUE}"/>'
                      f'<path d="M100 58 V118 M110 58 V118 M120 58 V118" stroke="{BLUE}" stroke-width="5" stroke-linecap="round"/>'
                      f'<path d="{WAVE} V210 H-10 Z" fill="{BLUE}"/><path d="M60 140 Q100 128 140 140" fill="none" stroke="{W}" stroke-width="4" stroke-linecap="round"/>')))
C.append(("Reverse", "Blue circle, with the wave as a white band of clear water through it.",
          circle_clip(5, f'<rect width="200" height="200" fill="{BLUE}"/><path d="M-10 100 Q45 76 100 100 T210 100 V124 Q155 148 100 124 T-10 124 Z" fill="{W}"/>', stroke=0)))
C.append(("Drop line", "The wave inside a water drop instead of a circle.",
          f'<clipPath id="k6"><path d="M100 16 C132 62 160 92 160 126 A60 60 0 0 1 40 126 C40 92 68 62 100 16 Z"/></clipPath>'
          f'<g clip-path="url(#k6)"><rect width="200" height="200" fill="{W}"/><path d="M-10 124 Q45 100 100 124 T210 124 V210 H-10 Z" fill="{BLUE}"/></g>'
          f'<path d="M100 16 C132 62 160 92 160 126 A60 60 0 0 1 40 126 C40 92 68 62 100 16 Z" fill="none" stroke="{BLUE}" stroke-width="6"/>'))
C.append(("Line + name", "The wave circle beside the name, for signs, letterheads and the website header.",
          f'<clipPath id="k7"><circle cx="44" cy="100" r="30"/></clipPath><g clip-path="url(#k7)"><rect width="200" height="200" fill="{W}"/>'
          f'<path d="M0 104 Q22 94 44 104 T88 104 V200 H0 Z" fill="{BLUE}"/></g><circle cx="44" cy="100" r="30" fill="none" stroke="{BLUE}" stroke-width="4"/>'
          f'<text x="84" y="100" font-family="{MINCHO}" font-size="24" font-weight="800" fill="{INK}">Shi Mizu</text>'
          f'<text x="87" y="118" font-family="{SANS}" font-size="10" font-weight="700" fill="{BLUE}" letter-spacing="5">DOJO</text>'))
C.append(("Sun and water", "Clear air, water, and one small red seal where the sun would be.",
          circle_clip(8, f'<rect width="200" height="200" fill="{W}"/><path d="{WAVE} V210 H-10 Z" fill="{BLUE}"/>'
                      f'<rect x="118" y="52" width="22" height="22" rx="3" fill="{RED}"/>')))
C.append(("Ripple line", "The wave repeated as three thin lines: lighter, more like a crest (kamon).",
          f'<circle cx="100" cy="100" r="80" fill="none" stroke="{BLUE}" stroke-width="6"/>'
          + "".join(f'<path d="M{24 + i*6} {104 + i*18} Q62 {84 + i*18} 100 {104 + i*18} T{176 - i*6} {104 + i*18}" fill="none" stroke="{BLUE}" stroke-width="7" stroke-linecap="round"/>' for i in range(3))))

# ---- From the belt tip (17) ----
C.append(("Belt ring", "The belt wrapped into a circle, with the rank bar and stripes at the top.",
          f'<circle cx="100" cy="100" r="68" fill="none" stroke="{BLUE}" stroke-width="26"/>'
          f'<path d="M72 40 A68 68 0 0 1 128 40" fill="none" stroke="{INK}" stroke-width="26"/>'
          + "".join(f'<rect x="{84 + i*10}" y="19" width="5" height="28" fill="{W}"/>' for i in range(4)) + t(100, 118, "清", 46, INK)))
C.append(("Standing belt", "The belt tip on its end, with 清水 down the black rank bar.",
          f'<rect x="74" y="12" width="52" height="176" fill="{BLUE}"/><rect x="74" y="54" width="52" height="96" fill="{INK}"/>'
          + t(100, 96, "清", 34, KIN) + t(100, 138, "水", 34, KIN)
          + "".join(f'<rect x="74" y="{158 + i*7}" width="52" height="3.5" fill="{W}"/>' for i in range(3))))
C.append(("Wave-cut belt", "The belt tip, with its end cut as the water line from #14. Both ideas in one.",
          f'<path d="M10 74 H150 Q164 86 150 100 T150 126 H10 Z" fill="{BLUE}"/><rect x="88" y="74" width="50" height="52" fill="{INK}"/>'
          + stripes(96, 74, 52, gap=10)))
C.append(("Water bar", "The belt tip, with the four stripes drawn as small waves.",
          f'<rect x="10" y="74" width="180" height="52" fill="{BLUE}"/><rect x="104" y="74" width="62" height="52" fill="{INK}"/>'
          + "".join(f'<path d="M110 {84 + i*11} Q122 {78 + i*11} 135 {84 + i*11} T160 {84 + i*11}" fill="none" stroke="{W}" stroke-width="3.5" stroke-linecap="round"/>' for i in range(4))))
C.append(("Belt in the circle", "The belt runs across the wave circle, so the stripes sit just above the water.",
          circle_clip(14, f'<rect width="200" height="200" fill="{W}"/><path d="M-10 128 Q45 108 100 128 T210 128 V210 H-10 Z" fill="{BLUE}"/>'
                      f'<rect x="-10" y="70" width="220" height="38" fill="{BLUE}"/><rect x="108" y="70" width="46" height="38" fill="{INK}"/>' + stripes(114, 70, 38, w=5, gap=9))))
C.append(("Crossed belts", "A blue belt over a white one: judo and jiu jitsu, the two arts on one mat.",
          f'<g transform="rotate(-28 100 100)"><rect x="6" y="80" width="188" height="40" fill="{W}" stroke="{INK}" stroke-width="3"/><rect x="128" y="80" width="40" height="40" fill="{INK}"/></g>'
          f'<g transform="rotate(28 100 100)"><rect x="6" y="80" width="188" height="40" fill="{BLUE}"/><rect x="128" y="80" width="40" height="40" fill="{INK}"/>{stripes(133, 80, 40, w=4, gap=8)}</g>'))
C.append(("Belt square", "The belt tip in a square tile, with 清水 above it. Works as an app icon.",
          f'<rect x="20" y="20" width="160" height="160" rx="18" fill="{KIN}"/>' + t(100, 92, "清水", 46, INK)
          + f'<rect x="20" y="116" width="160" height="34" fill="{BLUE}"/><rect x="104" y="116" width="44" height="34" fill="{INK}"/>' + stripes(110, 116, 34, w=5, gap=9)))
C.append(("Four stripes", "Just the black rank bar and its four white stripes. The most minimal version.",
          f'<rect x="56" y="40" width="88" height="120" rx="4" fill="{INK}"/>' + stripes(70, 40, 120, w=10, gap=18)
          + f'<rect x="56" y="160" width="88" height="14" fill="{BLUE}"/><rect x="56" y="26" width="88" height="14" fill="{BLUE}"/>'))
C.append(("Belt + name", "The belt tip as an underline for the name: a simple, readable lockup.",
          t(100, 92, "Shi Mizu", 38, INK) + t(100, 114, "DOJO · CLEARWATER", 10.5, BLUE, SANS, 700, 'letter-spacing="3"')
          + f'<rect x="30" y="128" width="140" height="22" fill="{BLUE}"/><rect x="112" y="128" width="40" height="22" fill="{INK}"/>' + stripes(117, 128, 22, w=4, gap=8)))

ref_html = "".join(f'<figure class="ref"><div class="art">{svg(s)}</div><figcaption><b>{n}</b><span>Round 1 favourite</span></figcaption></figure>' for n, s in REF)
cards = "".join(
    f'<figure><div class="art">{svg(s)}</div><div class="mini">{svg(s)}</div>'
    f'<figcaption><b>{i:02d} · {n}</b><span>{d}</span></figcaption></figure>'
    for i, (n, d, s) in enumerate(C, 21))

OUT.parent.mkdir(parents=True, exist_ok=True)
OUT.write_text(f"""<!doctype html>
<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">
<title>Logo Round 2 · Shi Mizu Dojo</title><meta name="robots" content="noindex">
<link href="https://fonts.googleapis.com/css2?family=Archivo:wdth,wght@62..125,100..900&family=Shippori+Mincho+B1:wght@400;800&family=Yuji+Boku&display=swap" rel="stylesheet">
<style>
  * {{ box-sizing: border-box; }}
  body {{ margin: 0; background: #EDEBE6; color: {INK}; font: 400 15px/1.45 Archivo, system-ui, sans-serif; }}
  header {{ max-width: 1400px; margin: 0 auto; padding: 32px 24px 8px; }}
  h1 {{ margin: 0 0 6px; font-size: 30px; font-stretch: 115%; font-weight: 800; letter-spacing: -0.02em; }}
  header p {{ margin: 0; color: #55555B; max-width: 62rem; }}
  .refs {{ max-width: 1400px; margin: 0 auto; padding: 16px 24px 0; display: grid; grid-template-columns: repeat(6, 1fr); gap: 16px; }}
  .sheet {{ max-width: 1400px; margin: 0 auto; padding: 16px 24px 48px; display: grid; grid-template-columns: repeat(6, 1fr); gap: 16px; }}
  figure {{ margin: 0; background: #fff; border: 1px solid rgba(0,0,0,.08); display: grid; grid-template-rows: auto auto 1fr; }}
  figure.ref {{ background: #F7F6F2; border: 2px dashed rgba(5,86,168,.35); grid-template-rows: auto 1fr; }}
  .art {{ padding: 20px 26px 6px; }}
  .art svg {{ display: block; width: 100%; height: auto; }}
  .mini {{ display: flex; justify-content: flex-end; padding: 0 10px; height: 30px; }}
  .mini svg {{ width: 30px; height: 30px; }}
  figcaption {{ padding: 9px 12px 12px; border-top: 1px solid rgba(0,0,0,.07); }}
  figcaption b {{ display: block; font-size: 13.5px; }}
  figcaption span {{ font-size: 12px; color: #55555B; }}
  @media (max-width: 1100px) {{ .sheet, .refs {{ grid-template-columns: repeat(3, 1fr); }} }}
  @media (max-width: 640px) {{ .sheet, .refs {{ grid-template-columns: repeat(2, 1fr); }} }}
</style></head><body>
<header><h1>Shi Mizu Dojo · logo round 2</h1>
<p>18 new concepts grown from round 1's favourites, #14 Clear line and #17 Belt tip (dashed, top left). #21–29 develop the wave circle, #30–38 the belt tip, and a few combine the two. Numbering continues from round 1.</p></header>
<section class="refs">{ref_html}</section>
<main class="sheet">{cards}</main>
</body></html>
""", encoding="utf-8")
print("wrote", OUT, len(C), "concepts")
