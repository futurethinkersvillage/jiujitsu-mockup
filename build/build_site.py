"""Builds the three homepage versions (tenugui, stone, stripe) from one shared structure.
Run:  python build/build_site.py   (writes site/<theme>/index.html)
Content marked TBC needs confirming with the instructor."""
import json
import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent / "site"
MARKS = json.loads(subprocess.run(["node", str(Path(__file__).with_name("brand_dump.js"))],
                                  capture_output=True, text=True, encoding="utf-8", check=True).stdout)
LEARN = [("counting", "Counting to ten"), ("judo-belts", "Judo belt ranks"),
         ("bjj-belts", "Jiu jitsu belt ranks"), ("two-names", "Same move, two names")]
CTA = "Book your first class"
CLUB, CLUB_SUB = "Shimizu Dojo", "Clearwater Martial Arts"   # from Ernst's banner drafts (TBC)

# Ernst's photos from his Alberta club (site/assets/photos). name: (width, height, alt)
PHOTOS = {
    "koshi-guruma": (876, 1280, "A judoka in a blue gi throws a partner in white over the hip in koshi-guruma."),
    "o-uchi-gari": (1102, 1280, "Two judoka with green belts mid-throw: a major inner reap, o-uchi-gari."),
    "juji-gatame-guard": (1280, 1011, "From her back, a grappler in blue controls her partner's arm from guard."),
    "groundwork-pin": (1280, 1064, "A judoka in blue pins her partner on the mat and controls his arm."),
    "youth-throw": (640, 409, "A young judoka with a yellow belt is thrown mid-air during practice."),
    "grading-group": (480, 562, "Five judoka in gis, kneeling and standing in front of the dojo wall after a grading."),
}
GALLERY = ["o-uchi-gari", "juji-gatame-guard", "groundwork-pin", "koshi-guruma", "youth-throw"]
SCROLLS = [
    ("seiryoku-zenyo", 121, 190, "精力善用", "Seiryoku zen'yō", "Maximum efficiency. Use your energy in the best possible way: technique over strength."),
    ("jita-kyoei", 122, 183, "自他共栄", "Jita kyōei", "Mutual welfare and benefit. You and your partner both get better, or neither of you does."),
    ("ju-yoku-go-o-seisu", 216, 520, "柔能制剛", "Jū yoku gō o seisu", "Softness controls hardness. Give way to force, then redirect it."),
]


def img(name, cls="", lazy=True):
    w, h, alt = PHOTOS[name]
    load = ' loading="lazy" decoding="async"' if lazy else ' fetchpriority="high"'
    return f'<img class="{cls}" src="../assets/photos/{name}.webp" width="{w}" height="{h}" alt="{alt}"{load}>'

FONTS = ("https://fonts.googleapis.com/css2?family=Archivo:wdth,wght@62..125,100..900"
         "&family=Figtree:wght@400;600;700;800&family=Shippori+Mincho+B1:wght@400;700;800"
         "&family=Zen+Kaku+Gothic+New:wght@400;500;700;900&family=Yuji+Boku&family=Zen+Antique&display=swap")

THEMES = {
    "tenugui": {
        "label": "Tenugui",
        "color": "#1B2A47",
        "h1": "The gentle way,<br>in Clearwater.",
        "kicker": "柔 · jū — gentleness that overcomes force",
        "lede": "Judo and Brazilian jiu jitsu for kids, teens and adults. Both arts grew from the same Japanese idea: give way to force, then turn it. We teach it on one mat at 52 Ridge.",
        "hero_art": '<div class="hero-art"><div class="vert" lang="ja">柔の道</div><figure class="hero-photo">{photo:koshi-guruma}</figure></div>',
        "hero_photo": "koshi-guruma",
        "two_title": "Two arts, one root",
    },
    "stone": {
        "label": "Stone & Water",
        "color": "#141618",
        "h1": "Soft as water.<br>Steady as stone.",
        "kicker": "",
        "lede": "Judo and Brazilian jiu jitsu for kids, teens and adults in the Clearwater Valley. Ernst Bergmann teaches both arts on one mat at 52 Ridge. No experience needed.",
        "hero_art": '<div class="hero-bg" aria-hidden="true"><img src="../assets/photos/falls-stone.webp" alt="" width="640" height="349" fetchpriority="high"></div>',
        "hero_photo": "",
        "two_title": "Two arts, one source",
    },
    "stripe": {
        "label": "Stripe",
        "color": "#16161A",
        "h1": "Every black belt<br>started as a white belt.",
        "kicker": "Brazilian jiu jitsu + judo · Clearwater, BC",
        "lede": "A new club for kids, teens and adults who want to learn to grapple, properly and safely. First class: wear what you'd wear to the gym.",
        "hero_art": '<figure class="hero-photo">{photo:o-uchi-gari}</figure><div class="hero-belt" aria-hidden="true"><span class="hb-bar"><i></i><i></i><i></i><i></i></span></div>',
        "hero_photo": "o-uchi-gari",
        "two_title": "Judo or jiu jitsu? Both.",
    },
}

PROGRAMS = [
    ("Little grapplers", "Ages 5–8 (TBC)", "Balance, breakfalls, animal movements and games that sneak in real technique. Short classes, lots of laughing."),
    ("Kids & youth", "Ages 9–14 (TBC)", "Judo throws, jiu jitsu basics, belt grading and how to train hard with a partner without anyone getting hurt."),
    ("Adult jiu jitsu", "Teens 15+ and adults", "Positions, escapes, sweeps and submissions, in the gi and without it. Live rolling at the end, always optional for beginners."),
    ("Adult judo", "Teens 15+ and adults", "How to fall, how to throw and how to pin. Builds balance and timing that carries straight into the ground game."),
    ("Women's self-defence", "Teens and adults (TBC)", "Practical escapes, grips and getting back to your feet, built on judo and jiu jitsu. Ernst ran this program at his Alberta club."),
]

SCHEDULE = [  # sample layout only
    ("Mon", [("5:00 pm", "Kids"), ("6:15 pm", "Adult jiu jitsu")]),
    ("Tue", []),
    ("Wed", [("5:00 pm", "Kids"), ("6:15 pm", "Adult judo")]),
    ("Thu", []),
    ("Fri", [("6:00 pm", "Open mat")]),
    ("Sat", [("10:00 am", "Family class")]),
]

FIRST = [
    ("Send us a message", "Tell us who's coming and which class. We'll confirm the time and send the waiver."),
    ("Arrive ten minutes early", "Sign the waiver, meet the coach, see where to change. Parents are welcome to stay and watch."),
    ("Wear gym clothes", "T-shirt, shorts or track pants with no zips or buttons. Bring water and sandals for off the mat. No gi needed yet."),
    ("Train", "Bow in, warm up, learn to fall, learn one technique, then try it with a partner at your own pace."),
]

FAQ = [
    ("Do I need to be fit or have any experience?", "No. Most people start out of shape and with no experience. You'll get fitter by training, and you'll always train at your own pace."),
    ("What's the difference between judo and jiu jitsu?", "Judo is mostly standing: throws, then pins. Brazilian jiu jitsu is mostly on the ground: control and submissions. Jiu jitsu grew out of judo about a hundred years ago, so they fit together naturally."),
    ("Is it safe?", "Everyone learns to fall before they learn to throw, and everyone learns to tap. Coaches supervise every round and pair people by size and experience."),
    ("How young can kids start?", "Around five, depending on the child (TBC with the instructor). Kids classes are about coordination, confidence and respect first."),
    ("Do I need to buy a gi?", "Not to start. After a few classes we'll help you choose one. A judo gi works for both arts."),
    ("Can I drop in while visiting Wells Gray?", "Yes. Visitors, seasonal workers and crews in town for the summer are welcome. Message us before you come."),
]

PRICES = [
    ("Drop-in", "Single class, any program"),
    ("Adult monthly", "Unlimited classes"),
    ("Kids monthly", "Kids & youth classes"),
    ("Family", "Two or more on one plan"),
]

def page(theme):
    t = THEMES[theme]
    others = [k for k in THEMES if k != theme]
    progs = "".join(f'<li class="prog"><h3>{n}</h3><p class="prog-age">{a}</p><p>{d}</p></li>' for n, a, d in PROGRAMS)
    sched = "".join(
        f'<div class="day"><h3>{d}</h3>' + ("".join(f'<p><b>{tm}</b>{c}</p>' for tm, c in cls) or '<p class="rest">Rest day</p>') + "</div>"
        for d, cls in SCHEDULE)
    first = "".join(f'<li><h3>{h}</h3><p>{p}</p></li>' for h, p in FIRST)
    faq = "".join(f'<details><summary>{q}</summary><p>{a}</p></details>' for q, a in FAQ)
    prices = "".join(f'<li><h3>{n}</h3><p class="price">$ TBC</p><p>{d}</p></li>' for n, d in PRICES)
    learn = "".join(
        f'<a class="learn-card" href="../posters/?theme={theme}&amp;p={pid}">'
        f'<img src="../posters/thumbs/{theme}-{pid}.webp" width="600" height="800" loading="lazy" decoding="async" alt="{title} poster"></a>'
        for pid, title in LEARN)
    hero_art = t['hero_art']
    if t['hero_photo']:
        hero_art = hero_art.replace('{photo:' + t['hero_photo'] + '}', img(t['hero_photo'], lazy=False))
    kicker = f'<p class="kicker">{t["kicker"]}</p>' if t['kicker'] else ''
    gallery = "".join(f'<li>{img(n)}</li>' for n in [g for g in GALLERY if g != t['hero_photo']][:4])
    scrolls = "".join(
        f'<li><div class="scroll-paper"><img src="../assets/photos/scroll-{f}.png" width="{w}" height="{h}" alt="Brush calligraphy: {k}" loading="lazy"></div>'
        f'<h3 lang="ja">{k}</h3><p class="sc-r">{r}</p><p>{d}</p></li>'
        for f, w, h, k, r, d in SCROLLS)
    asanoha_attr = MARKS['asanoha'].replace('"', '&quot;')
    root_style = f' style="--asanoha: {asanoha_attr}"' if theme == 'tenugui' else ''
    nav_mark, foot_mark = MARKS[theme]['nav'], MARKS[theme]['foot']
    switch = " ".join(f'<a href="../{k}/">{THEMES[k]["label"]}</a>' for k in others)

    NAV = '<a href="#programs">Programs</a><a href="#schedule">Schedule</a><a href="#pricing">Pricing</a><a href="#first">First class</a><a href="#learn">Learn</a><a href="#visit">Find us</a>'
    return f"""<!doctype html>
<html lang="en"{root_style}>
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{CLUB} · {CLUB_SUB} · {t['label']} direction</title>
<meta name="robots" content="noindex">
<meta name="description" content="Brazilian jiu jitsu and judo for kids, teens and adults at 52 Ridge, Clearwater Valley Resort, Clearwater BC. No experience needed.">
<meta name="theme-color" content="{t['color']}">
<meta property="og:title" content="{CLUB} · {CLUB_SUB}">
<meta property="og:description" content="Jiu jitsu and judo for kids, teens and adults in Clearwater, BC.">
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="{FONTS}" rel="stylesheet">
<link rel="stylesheet" href="../assets/site-base.css">
<link rel="stylesheet" href="style.css">
<script type="application/ld+json">{{"@context":"https://schema.org","@type":"SportsActivityLocation","name":"{CLUB}","sport":["Brazilian jiu jitsu","Judo"],"address":{{"@type":"PostalAddress","streetAddress":"373 Clearwater Valley Rd","addressLocality":"Clearwater","addressRegion":"BC","addressCountry":"CA"}}}}</script>
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
    {kicker}
    <h1>{t['h1']}</h1>
    <p class="lede">{t['lede']}</p>
    <div class="ctas"><a class="btn" href="#contact">{CTA}</a><a class="btn btn-ghost" href="#programs">See kids classes</a></div>
    <p class="where">52 Ridge · Clearwater Valley Resort · Clearwater, BC</p>
  </div>
  {hero_art}
</section>

<section class="sec programs" id="programs">
  <div class="sec-head"><h2>Classes for every age</h2><p>Four programs, one mat. Ages and times are being finalized with the instructor.</p></div>
  <ul class="prog-list">{progs}</ul>
</section>

<section class="sec gallery" id="mat">
  <div class="sec-head"><h2>On the mat</h2><p>Training at Ernst's previous club in Rocky Mountain House, Alberta. Photos from Clearwater are coming.</p></div>
  <ul class="gallery-list">{gallery}</ul>
</section>

<section class="sec two" id="arts">
  <div class="sec-head"><h2>{t['two_title']}</h2></div>
  <div class="two-grid">
    <div class="art"><p class="art-jp" lang="ja">柔道</p><h3>Judo</h3><p>“The gentle way.” Founded in Tokyo in 1882 by Jigorō Kanō. You learn to fall safely, to break someone's balance and to throw, then to pin. An Olympic sport since 1964.</p></div>
    <div class="art"><p class="art-jp" lang="ja">柔術</p><h3>Brazilian jiu jitsu</h3><p>“The gentle art.” Judo master Mitsuyo Maeda taught it to the Gracie family in Brazil around 1917, and they built it into a complete ground game. Smaller people control bigger people with leverage.</p></div>
    <p class="two-note">Same root, 柔 (jū): yield to force, then redirect it. Training both makes you better at each.</p>
  </div>
</section>

<section class="sec scrolls" id="scrolls">
  <div class="sec-head"><h2>The scrolls on our wall</h2><p>Three brushed maxims from Ernst's dojo in Alberta. Judo's founder, Jigorō Kanō, built the art on the first two.</p></div>
  <ul class="scroll-list">{scrolls}</ul>
</section>

<section class="sec schedule" id="schedule">
  <div class="sec-head"><h2>Weekly schedule</h2><p class="flag">Sample layout. Real times are coming soon.</p></div>
  <div class="week">{sched}</div>
  <p class="small"><a href="../posters/?theme={theme}">Printable posters</a> · schedule PDF coming with the final times</p>
</section>

<section class="sec pricing" id="pricing">
  <div class="sec-head"><h2>Simple pricing</h2><p>No contracts, no hidden fees. Final prices are TBC.</p></div>
  <ul class="price-list">{prices}</ul>
  <p class="fund">Cost shouldn't stop a kid from training. BC families can apply to <a href="https://kidsportcanada.ca/british-columbia/" rel="noopener">KidSport BC</a> or <a href="https://jumpstart.canadiantire.ca/" rel="noopener">Canadian Tire Jumpstart</a> for help with fees.</p>
</section>

<section class="sec first" id="first">
  <div class="sec-head"><h2>Your first class</h2><p>Nervous is normal. Here's exactly what happens.</p></div>
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
  <div class="sec-head"><h2>The dojo library</h2><p>The posters on our walls, free to read here: counting in Japanese, belt ranks, dojo words, throws, groundwork and where it all came from.</p></div>
  <div class="learn-grid">{learn}</div>
  <a class="btn" href="../posters/?theme={theme}">See all twelve posters</a>
</section>

<section class="sec visit" id="visit">
  <div class="visit-text">
    <h2>Find us</h2>
    <p class="addr"><b>52 Ridge · Clearwater Valley Resort</b><br>373 Clearwater Valley Rd, Clearwater, BC</p>
    <p>On Clearwater Valley Road, the road into Wells Gray Park.</p>
    <p>Training with us from Birch Island, Vavenby, Blackpool or Little Fort? Ask about carpooling. In winter, check <a href="https://www.drivebc.ca/" rel="noopener">DriveBC</a> before you head out.</p>
    <a class="btn btn-ghost" href="https://www.google.com/maps/search/?api=1&query=Clearwater+Valley+Resort+373+Clearwater+Valley+Rd+Clearwater+BC" rel="noopener">Open in Maps</a>
  </div>
  <div class="visit-card">
    <h3>Visiting Wells Gray?</h3>
    <p>Staying at the resort, working a season or here with a fire crew? Drop in for a class. Bring a gi if you have one; if not, gym clothes are fine.</p>
  </div>
</section>

<section class="sec faq" id="faq">
  <div class="sec-head"><h2>Questions</h2></div>
  <div class="faq-list">{faq}</div>
</section>

<section class="sec contact" id="contact">
  <h2>{CTA}</h2>
  <p>Message the club to book a class or ask anything. Parents are welcome to come and watch first.</p>
  <p class="contact-flag">Contact details are being confirmed with the instructor and will appear here.</p>
  <dl class="contact-row"><div><dt>Email</dt><dd>[TBC]</dd></div><div><dt>Phone / text</dt><dd>[TBC]</dd></div><div><dt>Instagram</dt><dd>[TBC]</dd></div></dl>
</section>
</main>

<footer class="foot">
  <span class="foot-mark" aria-hidden="true">{foot_mark}</span>
  <p><b>{CLUB} · {CLUB_SUB}</b><br>52 Ridge · Clearwater Valley Resort · Clearwater, BC</p>
  <p class="small">Temporary site · {t['label']} design direction · <a href="../posters/?theme={theme}">Posters</a></p>
</footer>

<script>
  // Close the phone menu after a section link is chosen.
  const menu = document.querySelector(".menu");
  menu.addEventListener("click", (e) => {{ if (e.target.closest("a")) menu.open = false; }});
</script>
</body>
</html>
"""


for theme in THEMES:
    out = ROOT / theme / "index.html"
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(page(theme), encoding="utf-8")
    print("wrote", out.relative_to(ROOT))
