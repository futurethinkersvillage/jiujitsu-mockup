/* Brand marks and patterns for the three directions: Tenugui, Stone & Water, Stripe. */
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

  /* --- Stone & Water direction: a river stone carved with 清水道場 in brush script,
         with a small red seal like the one on Ernst's carved-rock banner. --- */
  function stone({ fill = "#1E2124", ink = "#ECEDEA", seal = "#B8322A", size = "100%" } = {}) {
    return `<svg class="mark stone" viewBox="0 0 100 100" width="${size}" role="img" aria-label="River stone carved with 清水道場, Shimizu Dōjō">
      <path d="M48 4 C72 3 93 19 96 45 C99 72 81 95 52 97 C25 99 4 82 4 54 C4 27 22 5 48 4 Z" fill="${fill}"/>
      <path d="M30 14 C42 8 60 8 72 14" stroke="${ink}" stroke-opacity=".14" stroke-width="3" fill="none" stroke-linecap="round"/>
      <g fill="${ink}" font-family="'Yuji Boku', 'Shippori Mincho B1', serif" font-size="31" text-anchor="middle">
        <text x="66" y="47">清</text><text x="66" y="82">水</text>
        <text x="33" y="47">道</text><text x="33" y="82">場</text>
      </g>
      <rect x="77" y="80" width="7" height="7" rx="1" fill="${seal}"/>
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

  window.BRAND = { asanohaURI, seal, stone, beltTip, belt };
})();
