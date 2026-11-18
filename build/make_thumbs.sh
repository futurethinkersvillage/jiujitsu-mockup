#!/bin/bash
# Renders poster thumbnails for the homepages' Learn section.
# Needs the local preview server on :4317 (python -m http.server 4317 --directory site).
# Usage: bash build/make_thumbs.sh
set -e
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
OUT="$ROOT/site/posters/thumbs"; TMP="$(mktemp -d)"
mkdir -p "$OUT"
CH="/c/Program Files/Google/Chrome/Application/chrome.exe"
for theme in tenugui stone stripe; do
  for p in counting judo-belts bjj-belts two-names; do
    "$CH" --headless=new --disable-gpu --hide-scrollbars --force-device-scale-factor=1 --window-size=900,1200 \
      --virtual-time-budget=6000 --screenshot="$(cygpath -w "$TMP/$theme-$p.png")" \
      "http://localhost:4317/posters/?theme=$theme&p=$p&bare=1" >/dev/null 2>&1
    ffmpeg -loglevel error -y -i "$TMP/$theme-$p.png" -vf "scale=600:800:flags=lanczos" -c:v libwebp -quality 82 "$OUT/$theme-$p.webp"
  done
done
rm -rf "$TMP"; ls -la "$OUT"
