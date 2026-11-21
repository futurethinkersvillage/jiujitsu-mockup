"""Logo round 3: "Belt falls". A blue belt hanging vertically, its stripes running down its length like falling water.
Run: python build/build_logos3.py  -> site/logos/round-3/index.html"""
from pathlib import Path

OUT = Path(__file__).resolve().parent.parent / "site" / "logos" / "round-3" / "index.html"
BLUE, DEEP, KIN, RED, INK, W = "#0556A8", "#033E78", "#EEE9DD", "#C8402A", "#141618", "#FFFFFF"
MINCHO, SANS = "Shippori Mincho B1, serif", "Archivo, sans-serif"


def svg(body):
    return f'<svg viewBox="0 0 200 200" xmlns="http://www.w3.org/2000/svg">{body}</svg>'


def t(x, y, s, size, fill, font=MINCHO, weight=800, extra="", anchor="middle"):
    return f'<text x="{x}" y="{y}" font-family="{font}" font-size="{size}" font-weight="{weight}" fill="{fill}" text-anchor="{anchor}" {extra}>{s}</text>'


def streaks(x0, tops, lengths, w=5, gap=11, fill=W):
    """Vertical rounded streaks: the belt's rank stripes turned lengthwise, so they read as falling water."""
    if isinstance(tops, (int, float)):
        tops = [tops] * len(lengths)
    return "".join(f'<rect x="{x0 + i*gap}" y="{y}" width="{w}" height="{h}" rx="{w/2}" fill="{fill}"/>'
                   for i, (y, h) in enumerate(zip(tops, lengths)))


def wave_cut(x1, x2, y, amp=7):
    """Belt end cut as a small wave, right to left, for closing a path."""
    m = (x1 + x2) / 2
    return f"V{y} Q{(x2 + m)/2} {y - amp} {m} {y} T{x1} {y}"


def pool(cx, y, half=46, color=BLUE, sw=5):
    return (f'<path d="M{cx-half} {y} Q{cx-half/2} {y-8} {cx} {y} T{cx+half} {y}" fill="none" stroke="{color}" '
            f'stroke-width="{sw}" stroke-linecap="round"/>')


def belt_falls(belt=BLUE, bar=INK, stripe=W, water=BLUE, gapline=False):
    """The core mark: belt tip turned on end. Black rank bar at the top like the dark lip of the falls,
    the four white stripes pouring down out of it."""
    s = f'<path d="M74 18 H126 {wave_cut(74, 126, 160)} Z" fill="{belt}"/>'
    s += f'<rect x="74" y="18" width="52" height="38" fill="{bar}"/>'
    if gapline:
        s += f'<rect x="74" y="56" width="52" height="3" fill="{W}"/>'
    s += streaks(81, 18, [132, 100, 120, 84], fill=stripe)
    return s + pool(100, 182, color=water)


REF = [
    ("14 · Clear line", f'<clipPath id="r0"><circle cx="100" cy="100" r="80"/></clipPath><g clip-path="url(#r0)"><rect width="200" height="200" fill="{W}"/>'
                        f'<path d="M-10 110 Q45 84 100 110 T210 110 V210 H-10 Z" fill="{BLUE}"/></g><circle cx="100" cy="100" r="80" fill="none" stroke="{BLUE}" stroke-width="6"/>'),
    ("17 · Belt tip", f'<rect x="10" y="74" width="180" height="52" fill="{BLUE}"/><rect x="104" y="74" width="62" height="52" fill="{INK}"/>'
                      + "".join(f'<rect x="{112 + i*12}" y="74" width="6" height="52" fill="{W}"/>' for i in range(4))),
]

C = []
C.append(("Belt falls", "The belt tip stood on end. The black rank bar is the lip of the falls and the four stripes pour down out of it into the pool.",
          belt_falls()))
C.append(("Plain falls", "Just the blue belt and its streams, no rank bar. Softer and more about the water.",
          f'<path d="M74 18 H126 {wave_cut(74, 126, 160)} Z" fill="{BLUE}"/>'
          + streaks(81, [30, 22, 40, 26], [112, 84, 100, 70]) + pool(100, 182)))
C.append(("Falls in the circle", "Round 1's #14 circle with the belt falling into its water line.",
          f'<clipPath id="k3"><circle cx="100" cy="100" r="80"/></clipPath><g clip-path="url(#k3)"><rect width="200" height="200" fill="{W}"/>'
          f'<path d="M-10 146 Q45 122 100 146 T210 146 V210 H-10 Z" fill="{BLUE}"/>'
          f'<rect x="76" y="-10" width="48" height="160" fill="{BLUE}"/><rect x="76" y="-10" width="48" height="58" fill="{INK}"/>'
          + streaks(81, -10, [138, 112, 128, 100])
          + f'<path d="M40 156 Q70 146 100 156 T160 156" fill="none" stroke="{W}" stroke-width="4" stroke-linecap="round"/></g>'
          f'<circle cx="100" cy="100" r="80" fill="none" stroke="{BLUE}" stroke-width="6"/>'))
C.append(("Over the edge", "The belt runs flat, rank bar first, then bends over the edge and drops, and its stripes turn into falling water.",
          f'<path d="M20 40 H120 A40 40 0 0 1 160 80 {wave_cut(120, 160, 164, 6)} V80 H20 Z" fill="{BLUE}"/>'
          f'<rect x="20" y="40" width="30" height="40" fill="{INK}"/>'
          + "".join(f'<rect x="{24 + i*6.5}" y="40" width="3" height="40" fill="{W}"/>' for i in range(4))
          + streaks(127, 84, [70, 52, 64], w=4, gap=10) + pool(140, 182, half=36)))
C.append(("Tied belt", "A tied belt: the knot at the waist and two tails hanging down, streaked like two falls.",
          f'<rect x="20" y="34" width="160" height="18" fill="{BLUE}"/>'
          f'<clipPath id="k5"><path d="M76 58 H98 L94 172 L70 166 Z M102 58 H124 L130 166 L106 172 Z"/></clipPath>'
          f'<path d="M76 58 H98 L94 172 L70 166 Z M102 58 H124 L130 166 L106 172 Z" fill="{BLUE}"/>'
          f'<g clip-path="url(#k5)" stroke="{W}" stroke-width="4" stroke-linecap="round">'
          f'<path d="M82 66 L78 150"/><path d="M91 66 L88 128"/><path d="M109 66 L112 128"/><path d="M118 66 L122 150"/></g>'
          f'<rect x="72" y="26" width="56" height="34" fill="{BLUE}" stroke="{W}" stroke-width="3"/>'
          f'<path d="M80 58 L120 28" stroke="{DEEP}" stroke-width="6"/>'))
C.append(("Mist", "The streams run off the end of the belt and break into drops, like spray at the bottom of the falls.",
          f'<rect x="74" y="18" width="52" height="38" fill="{INK}"/><rect x="74" y="56" width="52" height="82" fill="{BLUE}"/>'
          + streaks(81, 18, [112, 112, 112, 112])
          + streaks(81, [146, 140, 150, 144], [14, 10, 12, 8], fill=BLUE)
          + streaks(81, [168, 158, 170, 160], [5, 5, 5, 5], fill=BLUE)))
C.append(("Falls tile", "The mark on a rounded blue square, for an app icon, a profile picture or a patch.",
          f'<clipPath id="k7"><rect x="20" y="20" width="160" height="160" rx="30"/></clipPath><g clip-path="url(#k7)">'
          f'<rect x="20" y="20" width="160" height="160" fill="{BLUE}"/><rect x="20" y="20" width="160" height="36" fill="{INK}"/>'
          + streaks(69, 20, [110, 82, 100, 70], w=8, gap=18)
          + f'<path d="M40 156 Q70 144 100 156 T160 156" fill="none" stroke="{W}" stroke-width="7" stroke-linecap="round"/></g>'))
C.append(("Falls + 清水", "The belt falls beside 清水 (shi mizu, clear water) set vertically.",
          f'<path d="M40 24 H84 {wave_cut(40, 84, 166, 6)} Z" fill="{BLUE}"/><rect x="40" y="24" width="44" height="30" fill="{INK}"/>'
          + streaks(45, 24, [126, 98, 114, 84], w=4, gap=10) + pool(62, 184, half=30, sw=4)
          + t(136, 96, "清", 54, INK) + t(136, 160, "水", 54, INK)))
C.append(("Lockup", "The mark beside the name, for signs, the website header and letterheads.",
          f'<path d="M22 54 H52 {wave_cut(22, 52, 140, 4)} Z" fill="{BLUE}"/><rect x="22" y="54" width="30" height="20" fill="{INK}"/>'
          + streaks(25.5, 54, [76, 58, 70, 50], w=3, gap=6.8)
          + t(64, 100, "Shi Mizu", 30, INK, anchor="start")
          + t(65, 117, "CLEARWATER", 8.5, BLUE, SANS, 700, 'letter-spacing="2.4"', anchor="start")
          + t(65, 129, "MIXED MARTIAL ARTS", 8.5, BLUE, SANS, 700, 'letter-spacing="2.4"', anchor="start")))
C.append(("One colour", "Belt falls in a single ink, for embroidery, stamps, vinyl cutting and engraving.",
          belt_falls(belt=INK, bar=INK, stripe=W, water=INK, gapline=True)))

ref_html = "".join(f'<figure class="ref"><div class="art">{svg(s)}</div><figcaption><b>{n}</b><span>Round 1 favourite</span></figcaption></figure>' for n, s in REF)
cards = "".join(
    f'<figure><div class="art">{svg(s)}</div><div class="mini">{svg(s)}</div>'
    f'<figcaption><b>{i:02d} · {n}</b><span>{d}</span></figcaption></figure>'
    for i, (n, d, s) in enumerate(C, 39))

OUT.parent.mkdir(parents=True, exist_ok=True)
OUT.write_text(f"""<!doctype html>
<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">
<title>Logo Round 3 · Shi Mizu Dojo</title><meta name="robots" content="noindex">
<link href="https://fonts.googleapis.com/css2?family=Archivo:wdth,wght@62..125,100..900&family=Shippori+Mincho+B1:wght@400;800&display=swap" rel="stylesheet">
<style>
  * {{ box-sizing: border-box; }}
  body {{ margin: 0; background: #EDEBE6; color: {INK}; font: 400 15px/1.45 Archivo, system-ui, sans-serif; }}
  header {{ max-width: 1400px; margin: 0 auto; padding: 32px 24px 8px; }}
  h1 {{ margin: 0 0 6px; font-size: 30px; font-stretch: 115%; font-weight: 800; letter-spacing: -0.02em; }}
  header p {{ margin: 0; color: #55555B; max-width: 62rem; }}
  .refs, .sheet {{ max-width: 1400px; margin: 0 auto; display: grid; grid-template-columns: repeat(6, 1fr); gap: 16px; }}
  .refs {{ padding: 16px 24px 0; }}
  .sheet {{ padding: 16px 24px 48px; }}
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
<header><h1>Shi Mizu Dojo · logo round 3 · belt falls</h1>
<p>A blue belt hanging on end, its rank stripes running down its length like falling water. #39 is the core idea; the rest try it in the circle, over an edge, tied, as an icon, with 清水, as a lockup and in one colour. Round 1 favourites shown dashed for reference.</p></header>
<section class="refs">{ref_html}</section>
<main class="sheet">{cards}</main>
</body></html>
""", encoding="utf-8")
print("wrote", OUT, len(C), "concepts")
