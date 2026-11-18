// Runs site/assets/brand.js in Node and prints the marks as JSON, so the
// homepages can inline them (logos and the landscape show without JavaScript).
const fs = require("fs");
const path = require("path");
global.window = {};
eval(fs.readFileSync(path.join(__dirname, "..", "site", "assets", "brand.js"), "utf8"));
const B = window.BRAND;
const out = {
  tenugui: { nav: B.seal(), foot: B.seal() },
  stone: { nav: B.stone(), foot: B.stone() },
  stripe: { nav: B.beltTip({ bg: "none" }), foot: B.beltTip({ bg: "none" }) },
  asanoha: B.asanohaURI("rgba(238,233,221,0.07)", 1.1),
};
process.stdout.write(JSON.stringify(out));
