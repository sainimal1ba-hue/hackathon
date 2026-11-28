#!/usr/bin/env python3
"""Turn the Google Fonts CSS into a local fonts.css for the Round 0 deck.

Usage:
  1. curl the css2 API (Chrome UA) to /tmp/gf.css
  2. download every fonts.gstatic.com URL into to_submit_pdf/fonts/ as font_N.woff2
  3. run this script — it rewrites each URL to a same-directory relative name

Trap: url() inside a CSS file resolves against the CSS file's own directory,
NOT the HTML's — so the rewritten names must NOT carry a fonts/ prefix.
"""
import re, os, sys

GF = "/tmp/gf.css"
OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "to_submit_pdf", "fonts", "fonts.css")

css = open(GF, encoding="utf-8").read()
urls = sorted(set(re.findall(r"https://fonts\.gstatic\.com/[^)]+", css)))

if len(sys.argv) > 1 and sys.argv[1] == "--list":
    for i, u in enumerate(urls, 1):
        print(i, u)
    sys.exit(0)

for i, u in enumerate(urls, 1):
    css = css.replace(u, f"font_{i}.woff2")

os.makedirs(os.path.dirname(OUT), exist_ok=True)
open(OUT, "w", encoding="utf-8").write(css)
print(f"wrote {OUT} with {len(urls)} font files mapped")
