"""Builds the three homepage versions (tenugui, wellsgray, stripe) from one shared structure.
Run:  python build/build_site.py   (writes site/<theme>/index.html)
Content marked TBC needs confirming with the instructor."""
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent / "site"

FONTS = ("https://fonts.googleapis.com/css2?family=Archivo:wdth,wght@62..125,100..900"
         "&family=Figtree:wght@400;600;700;800&family=Shippori+Mincho+B1:wght@400;700;800"
         "&family=Zen+Kaku+Gothic+New:wght@400;500;700;900&family=Zilla+Slab:wght@500;700&display=swap")

THEMES = {
    "tenugui": {
        "label": "Tenugui",
        "color": "#1B2A47",
        "mark": "seal",
        "h1": "The gentle way,<br>in Clearwater.",
        "kicker": "柔 · jū — gentleness that overcomes force",
        "lede": "Judo and Brazilian jiu jitsu for kids, teens and adults. Both arts grew from the same Japanese idea: give way to force, then turn it. We teach it on one mat at 52 Ridge.",
        "hero_art": '<div class="hero-art"><div class="vert" lang="ja">柔の道</div><div class="img-slot" data-prompt="H1"><span>Photo to come · prompt H1</span></div></div>',
        "two_title": "Two arts, one root",
    },
    "wellsgray": {
        "label": "Wells Gray",
        "color": "#1F3D3A",
        "mark": "badge",
        "h1": "Grappling in<br>Wells Gray country.",
        "kicker": "Jiu jitsu · Judo · Clearwater, BC",
        "lede": "Throws, holds and the ground game, taught on one mat at 52 Ridge, Clearwater Valley Resort. Kids, teens and adults. No experience and no special kit needed.",
        "hero_art": '<div class="hero-land" id="heroLand"></div>',
        "two_title": "Two arts on one mat",
    },
    "stripe": {
        "label": "Stripe",
        "color": "#16161A",
        "mark": "belttip",
        "h1": "Every black belt<br>started as a white belt.",
        "kicker": "Brazilian jiu jitsu + judo · Clearwater, BC",
        "lede": "A new club for kids, teens and adults who want to learn to grapple, properly and safely. First class: wear what you'd wear to the gym.",
        "hero_art": '<div class="hero-belt" aria-hidden="true"><span class="hb-bar"><i></i><i></i><i></i><i></i></span></div>',
        "two_title": "Judo or jiu jitsu? Both.",
    },
}

PROGRAMS = [
    ("Little grapplers", "Ages 5–8 (TBC)", "Balance, breakfalls, animal movements and games that sneak in real technique. Short classes, lots of laughing."),
    ("Kids & youth", "Ages 9–14 (TBC)", "Judo throws, jiu jitsu basics, belt grading and how to train hard with a partner without anyone getting hurt."),
    ("Adult jiu jitsu", "Teens 15+ and adults", "Positions, escapes, sweeps and submissions, in the gi and without it. Live rolling at the end, always optional for beginners."),
    ("Adult judo", "Teens 15+ and adults", "How to fall, how to throw and how to pin. Builds balance and timing that carries straight into the ground game."),
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

def mark_js(theme):
    return {"seal": "BRAND.seal()", "badge": "BRAND.badge()", "belttip": "BRAND.beltTip({bg:'none'})"}[THEMES[theme]["mark"]]


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
    switch = " ".join(f'<a href="../{k}/">{THEMES[k]["label"]}</a>' for k in others)

    return f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Clearwater Jiu Jitsu & Judo · {t['label']} direction</title>
<meta name="description" content="Brazilian jiu jitsu and judo for kids, teens and adults at 52 Ridge, Clearwater Valley Resort, Clearwater BC. No experience needed.">
<meta name="theme-color" content="{t['color']}">
<meta property="og:title" content="Clearwater Jiu Jitsu & Judo">
<meta property="og:description" content="Jiu jitsu and judo for kids, teens and adults in Clearwater, BC.">
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="{FONTS}" rel="stylesheet">
<link rel="stylesheet" href="../assets/site-base.css">
<link rel="stylesheet" href="../posters/poster.css">
<link rel="stylesheet" href="style.css">
<script type="application/ld+json">{{"@context":"https://schema.org","@type":"SportsActivityLocation","name":"Clearwater Jiu Jitsu & Judo","sport":["Brazilian jiu jitsu","Judo"],"address":{{"@type":"PostalAddress","streetAddress":"373 Clearwater Valley Rd","addressLocality":"Clearwater","addressRegion":"BC","addressCountry":"CA"}}}}</script>
</head>
<body class="th-{theme}">
<a class="skip" href="#main">Skip to content</a>
<div class="proto">Design direction: <b>{t['label']}</b> · also see {switch} · <a href="../">compare all</a></div>
<header class="nav">
  <a class="brand" href="#top" aria-label="Clearwater Jiu Jitsu and Judo, home"><span class="brand-mark" data-mark></span><span class="brand-word"><b>Clearwater</b><span>Jiu Jitsu &amp; Judo</span></span></a>
  <nav aria-label="Main"><a href="#programs">Programs</a><a href="#schedule">Schedule</a><a href="#first">First class</a><a href="#learn">Learn</a><a href="#visit">Find us</a></nav>
  <a class="btn btn-nav" href="#contact">Book a first class</a>
</header>

<main id="main">
<section class="hero" id="top">
  <div class="hero-text">
    <p class="kicker">{t['kicker']}</p>
    <h1>{t['h1']}</h1>
    <p class="lede">{t['lede']}</p>
    <div class="ctas"><a class="btn" href="#contact">Book an adult class</a><a class="btn btn-ghost" href="#contact">Book a kids class</a></div>
    <p class="where">52 Ridge · Clearwater Valley Resort · Clearwater, BC</p>
  </div>
  {t['hero_art']}
</section>

<section class="sec programs" id="programs">
  <div class="sec-head"><h2>Classes for every age</h2><p>Four programs, one mat. Ages and times are being finalized with the instructor.</p></div>
  <ul class="prog-list">{progs}</ul>
</section>

<section class="sec two" id="arts">
  <div class="sec-head"><h2>{t['two_title']}</h2></div>
  <div class="two-grid">
    <div class="art"><p class="art-jp" lang="ja">柔道</p><h3>Judo</h3><p>“The gentle way.” Founded in Tokyo in 1882 by Jigorō Kanō. You learn to fall safely, to break someone's balance and to throw, then to pin. An Olympic sport since 1964.</p></div>
    <div class="art"><p class="art-jp" lang="ja">柔術</p><h3>Brazilian jiu jitsu</h3><p>“The gentle art.” Judo master Mitsuyo Maeda taught it to the Gracie family in Brazil around 1917, and they built it into a complete ground game. Smaller people control bigger people with leverage.</p></div>
    <p class="two-note">Same root, 柔 (jū): yield to force, then redirect it. Training both makes you better at each.</p>
  </div>
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
  <div class="img-slot" data-prompt="H3"><span>Coach portrait to come · prompt H3</span></div>
  <div class="coach-text">
    <h2>Your coach</h2>
    <p class="coach-name">[Instructor name] · [rank, e.g. judo shodan / BJJ brown belt]</p>
    <p>[Two or three sentences in the instructor's own words: how they started, who they trained under, why they're teaching in Clearwater.]</p>
    <p class="small">Lineage: [teacher] → [teacher] → [instructor]. Certifications: [NCCP / Judo BC / first aid, TBC].</p>
  </div>
</section>

<section class="sec learn" id="learn">
  <div class="sec-head"><h2>The dojo library</h2><p>The posters on our walls, free to read here: counting in Japanese, belt ranks, dojo words, throws, groundwork and where it all came from.</p></div>
  <div class="learn-grid" id="learnGrid"></div>
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
  <h2>Come try a class</h2>
  <p>Message the club to book your first class or ask anything.</p>
  <div class="contact-row"><span>Email: [TBC]</span><span>Phone / text: [TBC]</span><span>Instagram: [TBC]</span></div>
</section>
</main>

<footer class="foot">
  <span class="foot-mark" data-mark></span>
  <p><b>Clearwater Jiu Jitsu &amp; Judo</b><br>52 Ridge · Clearwater Valley Resort · Clearwater, BC</p>
  <p class="small">Temporary site · {t['label']} design direction · <a href="../posters/?theme={theme}">Posters</a></p>
</footer>

<script src="https://cdnjs.cloudflare.com/ajax/libs/qrcode-generator/1.4.4/qrcode.min.js"></script>
<script src="../assets/content.js"></script>
<script src="../assets/brand.js"></script>
<script src="../posters/render.js"></script>
<script>
  document.querySelectorAll("[data-mark]").forEach((el) => el.innerHTML = {mark_js(theme)});
  document.documentElement.style.setProperty("--asanoha", BRAND.asanohaURI("rgba(238,233,221,0.07)", 1.1));
  const land = document.getElementById("heroLand");
  if (land) land.innerHTML = BRAND.landscape({{ align: "xMidYMax" }});
  const picks = ["counting", "judo-belts", "bjj-belts", "two-names"];
  document.getElementById("learnGrid").innerHTML = picks.map((id) => {{
    const p = POSTERS.list.find((x) => x.id === id);
    return `<a class="learn-card" href="../posters/?theme={theme}&p=${{id}}" aria-label="${{p.title}} poster">${{POSTERS.renderPoster(p, "{theme}")}}</a>`;
  }}).join("");
</script>
</body>
</html>
"""


for theme in THEMES:
    out = ROOT / theme / "index.html"
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(page(theme), encoding="utf-8")
    print("wrote", out.relative_to(ROOT))
