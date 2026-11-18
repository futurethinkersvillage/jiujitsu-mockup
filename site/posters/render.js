/* Poster renderer: one markup, three themes (tenugui | stone | stripe). */
(function () {
  const { club, posters } = window.DOJO;
  const B = window.BRAND;
  const esc = (s) => String(s).replace(/&/g, "&amp;").replace(/</g, "&lt;");

  const THEMES = {
    tenugui: {
      label: "Tenugui", mark: () => B.seal({ fill: "#C8402A", ink: "#EEE9DD" })
    },
    stone: {
      label: "Stone & Water", mark: () => B.stone()
    },
    stripe: {
      label: "Stripe", mark: () => B.beltTip({ bg: "#F5F5F2" })
    }
  };

  function qr(size = 4) {
    if (!window.qrcode) return "";
    const q = window.qrcode(0, "M");
    q.addData(club.href);
    q.make();
    return q.createSvgTag({ cellSize: size, margin: 0, scalable: true });
  }

  const head = (p, theme) => `
    <header class="ph">
      ${theme === "stripe" ? stripeBand(p) : ""}
      <div class="ph-jp len-${Math.min([...p.jp].length, 5)}" lang="ja">${p.jp}</div>
      <div class="ph-text">
        <p class="ph-romaji">${esc(p.romaji)}</p>
        <h2 class="ph-title">${esc(p.title)}</h2>
        <p class="ph-lede">${esc(p.lede)}</p>
      </div>
      ${theme === "tenugui" ? `<div class="ph-seal">${B.seal()}</div>` : ""}
    </header>`;

  // Stripe theme: each poster opens with a belt running edge to edge, colour keyed to the poster.
  const BAND = { counting: "#F4F2EC", "judo-belts": "#F2C230", "bjj-belts": "#2557B8", "dojo-words": "#E8772E",
    "nage-waza": "#2E8B4E", "katame-waza": "#6A3FA0", "two-names": "#2557B8", ukemi: "#F2C230",
    principles: "#6B4226", lineage: "#16161A", "dojo-code": "#E8772E", "come-train": "#16161A" };
  function stripeBand(p) {
    const c = BAND[p.id] || "#16161A";
    const bar = c === "#16161A" ? "#D7262E" : "#16161A";
    const n = (posters.indexOf(p) % 4) + 1;
    return `<div class="band" style="background:${c}"><span class="band-bar" style="background:${bar}">${"<i></i>".repeat(n)}</span></div>`;
  }

  const foot = (theme) => `
    <footer class="pf">
      <div class="pf-mark">${THEMES[theme].mark()}</div>
      <div class="pf-name"><strong>${esc(club.name)}</strong><span>${esc(club.venue)} · Clearwater, BC</span></div>
      <div class="pf-url">${esc(club.url)}</div>
      <div class="pf-qr">${qr()}</div>
    </footer>`;

  const body = {
    counting: (p) => `
      <ol class="count">${p.items.map((i) => `
        <li><span class="c-n">${i.n}</span><span class="c-k" lang="ja">${i.k}</span>
        <span class="c-r">${esc(i.r)}</span><span class="c-kana" lang="ja">${i.kana}</span></li>`).join("")}
      </ol>
      <div class="count-extra">${p.extra.map((i) => `
        <div><span class="c-n">${i.n}</span><span class="c-k" lang="ja">${i.k}</span><span class="c-r">${esc(i.r)}</span><span class="c-note">${esc(i.note)}</span></div>`).join("")}
      </div>
      <p class="p-note">${esc(p.tip)}</p>`,

    belts: (p) => p.groups.map((g) => `
      <section class="bgroup"><h3 class="g-label">${esc(g.label)}</h3>
        <ul class="brows">${g.items.map((i) => `
          <li>${B.belt(i.c, { mode: "blocks" })}
            <span class="b-rank">${esc(i.rank)}</span><span class="b-name">${esc(i.name)}</span>
            <span class="b-k" lang="ja">${i.k}</span><span class="b-r">${esc(i.r)}</span></li>`).join("")}
        </ul></section>`).join("") + `<p class="p-note">${esc(p.note)}</p>`,

    bjjbelts: (p) => `
      <section class="bgroup"><h3 class="g-label">Adults · 16 and up</h3>
        <ul class="adults">${p.adults.map((i) => `
          <li>${B.belt([i.c], { bar: i.bar || "#1A1A1D", stripes: 4 })}
            <span class="b-name">${esc(i.name)}</span><span class="b-k" lang="ja">${i.jp}</span>
            <span class="b-age">${esc(i.age)}</span><span class="b-time">${esc(i.time)}</span></li>`).join("")}
        </ul></section>
      <div class="bjj-split">
        <section class="bgroup"><h3 class="g-label">Kids · 4 to 15</h3>
          <ul class="kids">${p.kids.map((i) => `<li>${B.belt(i.c, { mode: "center", bar: "#1A1A1D", stripes: 0, cls: "sm" })}<span>${esc(i.name)}</span></li>`).join("")}</ul>
        </section>
        <section class="bgroup"><h3 class="g-label">Beyond black</h3>
          <ul class="degrees">${p.degrees.map((i) => `<li>${B.belt(i.c, { mode: "blocks", cls: "sm" })}<span><b>${esc(i.label)}</b>${esc(i.sub)}</span></li>`).join("")}</ul>
        </section>
      </div>
      <p class="p-note">${esc(p.note)}</p>`,

    words: (p) => `<div class="words">${p.groups.map((g) => `
      <section class="wgroup ${g.seq ? "is-seq" : ""}"><h3 class="g-label">${esc(g.label)}</h3>
        <${g.seq ? "ol" : "ul"} class="terms">${g.items.map((i) => `
          <li><span class="t-k ${[...i.k].length > 4 ? "long" : ""}" lang="ja">${i.k}</span><span class="t-r">${esc(i.r)}</span><span class="t-e">${esc(i.e)}</span></li>`).join("")}
        </${g.seq ? "ol" : "ul"}></section>`).join("")}</div>`,

    techniques: (p) => `
      <ul class="tech">${p.items.map((i) => `
        <li><span class="t-f">${esc(i.f)}</span><span class="t-k ${[...i.k].length > 4 ? "long" : ""}" lang="ja">${i.k}</span>
        <span class="t-r">${esc(i.r)}</span><span class="t-e">${esc(i.e)}</span></li>`).join("")}
      </ul><p class="p-note">${esc(p.note)}</p>`,

    ground: (p) => `<div class="ground">${p.groups.map((g) => `
      <section class="ggroup"><h3 class="g-label"><span lang="ja">${g.k}</span> ${esc(g.r)}<small>${esc(g.label)}</small></h3>
        <ul class="terms">${g.items.map((i) => `
          <li><span class="t-k ${[...i.k].length > 4 ? "long" : ""}" lang="ja">${i.k}</span><span class="t-r">${esc(i.r)}</span><span class="t-e">${esc(i.e)}</span></li>`).join("")}
        </ul></section>`).join("")}</div><p class="p-note">${esc(p.note)}</p>`,

    pairs: (p) => `
      <div class="pairs-head"><span>Jiu jitsu</span><span>Judo</span></div>
      <ul class="pairs">${p.items.map((i) => `
        <li><span class="pa-a">${esc(i.a)}</span><span class="pa-eq" aria-hidden="true"></span>
        <span class="pa-k" lang="ja">${i.k}</span><span class="pa-r">${esc(i.r)}</span></li>`).join("")}
      </ul><p class="p-note">${esc(p.note)}</p>`,

    ukemi: (p) => `
      <ul class="ukemi">${p.items.map((i) => `
        <li><span class="t-k ${[...i.k].length > 4 ? "long" : ""}" lang="ja">${i.k}</span><span class="t-r">${esc(i.r)}</span><span class="t-e">${esc(i.e)}</span><span class="t-d">${esc(i.d)}</span></li>`).join("")}
      </ul>
      <section class="rules"><h3 class="g-label">Every time</h3><ol>${p.rules.map((r) => `<li>${esc(r)}</li>`).join("")}</ol></section>`,

    principles: (p) => `
      <ul class="princ">${p.items.map((i) => `
        <li><span class="pr-k ${[...i.k].length > 4 ? "long" : ""}" lang="ja">${i.k}</span><span class="t-r">${esc(i.r)}</span><span class="t-e">${esc(i.e)}</span><span class="t-d">${esc(i.d)}</span></li>`).join("")}
      </ul>`,

    timeline: (p) => `
      <ol class="timeline">${p.items.map((i) => `<li><span class="tl-y">${esc(i.y)}</span><span class="tl-t">${esc(i.t)}</span></li>`).join("")}</ol>`,

    code: (p) => `
      <ol class="code">${p.items.map((i) => `<li><span class="cd-k" lang="ja">${i.k}</span><span class="cd-t">${esc(i.t)}</span></li>`).join("")}</ol>`,

    promo: (p, theme) => `
      <div class="promo">
        <ul class="promo-progs">${p.programs.map((x) => `<li>${esc(x)}</li>`).join("")}</ul>
        <div class="promo-where"><strong>${esc(club.venue)}</strong><span>${esc(club.address)}</span></div>
        <div class="promo-qr"><div class="qr-box">${qr(6)}</div><p>${esc(p.cta)}<br><b>${esc(club.url)}</b></p></div>
      </div>`
  };

  function renderPoster(p, theme) {
    return `<div class="sheet"><article class="poster t-${p.type}" data-theme="${theme}" data-id="${p.id}">
      ${head(p, theme)}
      <div class="pb">${body[p.type](p, theme)}</div>
      ${foot(theme)}
    </article></div>`;
  }

  window.POSTERS = { THEMES, renderPoster, list: posters };
})();
