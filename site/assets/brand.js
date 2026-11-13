/* Brand marks, patterns and illustrations for the three directions. */
(function () {
  let uid = 0;
  const id = (p) => `${p}${++uid}`;

  /* --- Asanoha (hemp-leaf) tile: a classic pattern for children's and martial-arts cloth,
         because hemp grows fast and straight. Tile = 40 x 69.282 (triangular lattice). --- */
  function asanohaPath() {
    const a = 40, h = 69.282, H = h / 2;
    const L = (x1, y1, x2, y2) => `M${x1} ${y1}L${x2} ${y2}`;
    const spokes = (cx, cy, pts) => pts.map(([x, y]) => L(cx, cy, x, y)).join("");
    return [
      L(0, 0, a, 0), L(0, H, a, H), L(0, h, a, h),
      L(0, 0, a, h), L(a, 0, 0, h),
      spokes(20, 11.547, [[0, 0], [a, 0], [20, H]]),
      spokes(0, 23.094, [[0, 0], [20, H], [-20, H]]),
      spokes(a, 23.094, [[a, 0], [20, H], [60, H]]),
      spokes(20, 57.735, [[0, h], [a, h], [20, H]]),
      spokes(0, 46.188, [[0, h], [20, H], [-20, H]]),
      spokes(a, 46.188, [[a, h], [20, H], [60, H]])
    ].join("");
  }
  function asanohaURI(stroke, width = 1) {
    const svg = `<svg xmlns='http://www.w3.org/2000/svg' width='40' height='69.282' viewBox='0 0 40 69.282'><path d='${asanohaPath()}' fill='none' stroke='${stroke}' stroke-width='${width}' stroke-linecap='round'/></svg>`;
    return `url("data:image/svg+xml,${encodeURIComponent(svg)}")`;
  }

  /* --- Tenugui direction: vermilion hanko seal reading 清水道場 (Shimizu Dōjō, "Clearwater Dojo").
         Traditional order: right column top-to-bottom, then left column. --- */
  function seal({ fill = "#C8402A", ink = "#EEE9DD", size = "100%" } = {}) {
    return `<svg class="mark seal" viewBox="0 0 100 100" width="${size}" role="img" aria-label="Seal reading 清水道場, Shimizu Dōjō">
      <rect x="3" y="3" width="94" height="94" rx="9" fill="${fill}"/>
      <rect x="9" y="9" width="82" height="82" rx="4" fill="none" stroke="${ink}" stroke-width="2.4"/>
      <line x1="50" y1="14" x2="50" y2="86" stroke="${ink}" stroke-width="1.2" opacity=".55"/>
      <g fill="${ink}" font-family="'Shippori Mincho B1', 'Noto Serif JP', serif" font-weight="800" font-size="34" text-anchor="middle">
        <text x="70.5" y="46">清</text><text x="70.5" y="84">水</text>
        <text x="29.5" y="46">道</text><text x="29.5" y="84">場</text>
      </g>
    </svg>`;
  }

  /* --- Wells Gray direction: park badge. Basalt ring, layered ridges, a falls dropping into the river. --- */
  function badge({ ring = "#23292B", paper = "#EEF2EC", sky = "#E3A13B", far = "#7FB0A6", mid = "#2C6E6A", near = "#1F3D3A", size = "100%" } = {}) {
    const top = id("bt"), bot = id("bb"), clip = id("bc");
    return `<svg class="mark badge" viewBox="0 0 200 200" width="${size}" role="img" aria-label="Clearwater Jiu Jitsu and Judo badge">
      <defs>
        <path id="${top}" d="M 30 100 A 70 70 0 0 1 170 100"/>
        <path id="${bot}" d="M 22 100 A 78 78 0 0 0 178 100"/>
        <clipPath id="${clip}"><circle cx="100" cy="100" r="56"/></clipPath>
      </defs>
      <circle cx="100" cy="100" r="97" fill="${ring}"/>
      <circle cx="100" cy="100" r="58.5" fill="none" stroke="${paper}" stroke-width="1.5"/>
      <g clip-path="url(#${clip})">
        <rect x="0" y="0" width="200" height="200" fill="${sky}"/>
        <circle cx="128" cy="86" r="15" fill="${paper}" opacity=".9"/>
        <path d="M40 120 L72 76 L92 98 L116 62 L160 120 Z" fill="${far}"/>
        <path d="M40 132 L64 104 L82 118 L100 96 L112 108 L112 160 L40 160 Z" fill="${mid}"/>
        <path d="M118 104 L140 92 L162 118 L162 160 L118 160 Z" fill="${mid}"/>
        <rect x="111" y="104" width="8" height="40" fill="${paper}"/>
        <path d="M40 140 Q 80 132 100 142 T 162 140 L162 170 L40 170 Z" fill="${near}"/>
        <path d="M70 150 Q 100 144 130 150" stroke="${paper}" stroke-width="2" fill="none" opacity=".7"/>
      </g>
      <g fill="${paper}" font-family="'Zilla Slab', serif" font-weight="700" letter-spacing="2.2">
        <text font-size="17"><textPath href="#${top}" startOffset="50%" text-anchor="middle">CLEARWATER</textPath></text>
        <text font-size="11.5"><textPath href="#${bot}" startOffset="50%" text-anchor="middle" dominant-baseline="hanging">JIU JITSU · JUDO · B.C.</textPath></text>
      </g>
      <circle cx="31" cy="100" r="2.4" fill="${paper}"/><circle cx="169" cy="100" r="2.4" fill="${paper}"/>
    </svg>`;
  }

  /* --- Stripe direction: the belt tip. A black belt with its red rank bar and four stripes of tape. --- */
  function beltTip({ belt = "#16161A", bar = "#D7262E", tape = "#F5F5F2", bg = "none", size = "100%" } = {}) {
    return `<svg class="mark belttip" viewBox="0 0 100 100" width="${size}" role="img" aria-label="Belt tip with four stripes">
      <rect width="100" height="100" fill="${bg}"/>
      <rect x="0" y="30" width="100" height="40" fill="${belt}"/>
      <rect x="54" y="30" width="34" height="40" fill="${bar}"/>
      <g fill="${tape}"><rect x="58" y="30" width="4" height="40"/><rect x="65" y="30" width="4" height="40"/><rect x="72" y="30" width="4" height="40"/><rect x="79" y="30" width="4" height="40"/></g>
    </svg>`;
  }

  /* --- Belt graphic. mode: solid | center (kids BJJ) | split (judo half grades) | blocks (coral, kōhaku) --- */
  function belt(colors, { mode = "solid", bar = null, stripes = 0, cls = "" } = {}) {
    const [a, b] = colors;
    let bg = a;
    if (b && mode === "center") bg = `linear-gradient(${a} 0 34%, ${b} 34% 66%, ${a} 66%)`;
    if (b && mode === "split") bg = `linear-gradient(${a} 0 50%, ${b} 50%)`;
    if (b && mode === "blocks") bg = `repeating-linear-gradient(90deg, ${a} 0 12.5%, ${b} 12.5% 25%)`;
    const light = /^#F/i.test(a) && !b;
    let barHtml = "";
    if (bar) {
      const tapes = Array.from({ length: stripes }, () => `<i></i>`).join("");
      barHtml = `<span class="belt-bar" style="background:${bar}">${tapes}</span>`;
    }
    return `<span class="belt ${light ? "is-light" : ""} ${cls}" style="background:${bg}">${barHtml}</span>`;
  }

  /* --- Wells Gray landscape strip for headers. viewBox 600 x 220. --- */
  function landscape({ sky = "#E3A13B", sun = "#F3EBDA", far = "#7FB0A6", mid = "#2C6E6A", near = "#1F3D3A", water = "#EEF2EC", cls = "", align = "xMidYMid" } = {}) {
    return `<svg class="landscape ${cls}" viewBox="0 0 600 220" preserveAspectRatio="${align} slice" aria-hidden="true">
      <rect width="600" height="220" fill="${sky}"/>
      <circle cx="430" cy="92" r="38" fill="${sun}"/>
      <path d="M0 150 L60 112 L110 130 L170 70 L230 118 L280 96 L340 128 L400 80 L470 126 L520 100 L600 136 L600 220 L0 220 Z" fill="${far}"/>
      <path d="M0 176 L50 150 L120 166 L190 128 L250 160 L300 140 L300 220 L0 220Z" fill="${mid}"/>
      <path d="M318 140 L380 122 L450 152 L520 132 L600 160 L600 220 L318 220Z" fill="${mid}"/>
      <rect x="300" y="138" width="18" height="58" fill="${water}"/>
      <path d="M300 146 h18 M300 160 h18 M300 174 h18" stroke="${mid}" stroke-width="1.2" opacity=".35"/>
      <path d="M0 196 Q 150 180 300 194 T 600 190 L600 220 L0 220Z" fill="${near}"/>
      <path d="M240 204 Q 300 196 360 204" stroke="${water}" stroke-width="3" fill="none" opacity=".75"/>
    </svg>`;
  }

  window.BRAND = { asanohaURI, seal, badge, beltTip, belt, landscape };
})();
