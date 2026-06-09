#!/usr/bin/env python3
"""
Split the large window.logseq_db inline script out of index.html.

logseq/publish-spa embeds the entire graph as a single JS variable inside
index.html, which grows past GitHub's 100 MB per-file push limit as the graph
expands.  This script:

  1. Extracts the COMPLETE JS assignment  window.logseq_db="...data..."
     (outer quotes included) from the inline <script> block
  2. Gzip-compresses it and writes www/static/js/db.gz (~90% smaller)
  3. Rewrites index.html with an async loader that fetches + decompresses db.gz
     and eval()s the assignment, then loads all original <script src="..."> tags

IMPORTANT — why eval(), not direct assignment:
  The inline <script> source contains JS string-literal escape sequences
  (\n, \\, \uXXXX, etc.).  Assigning the raw text to window.logseq_db would
  leave those escapes un-evaluated (e.g. literal backslash-n instead of a
  newline), corrupting the Transit/JSON data and breaking JSON.parse inside
  the Logseq SPA.  eval() reproduces the exact same effect as the original
  inline script.
"""

import gzip
import json
import re
import sys
import os

INDEX = "www/index.html"
DB_GZ = "www/static/js/db.gz"

SCRIPT_START = '<script>window.logseq_db="'
SCRIPT_END = '"</script>'

with open(INDEX, "r", encoding="utf-8") as f:
    content = f.read()

# --- locate the inline DB script ---
idx = content.find(SCRIPT_START)
if idx == -1:
    print("ERROR: window.logseq_db inline script not found in index.html", file=sys.stderr)
    sys.exit(1)

data_begin = idx + len(SCRIPT_START)
data_end = content.find(SCRIPT_END, data_begin)
if data_end == -1:
    print("ERROR: could not find closing '\"</script>' for logseq_db", file=sys.stderr)
    sys.exit(1)

# Store the COMPLETE assignment so the browser can eval() it verbatim,
# preserving JS string-literal escape-sequence semantics.
# = 'window.logseq_db="...data..."'  (outer quotes included, no <script> tags)
assignment = content[idx + len("<script>") : data_end + 1]
raw = assignment.encode("utf-8")
compressed = gzip.compress(raw, compresslevel=6)

os.makedirs(os.path.dirname(DB_GZ), exist_ok=True)
with open(DB_GZ, "wb") as f:
    f.write(compressed)

print(
    f"db.gz: {len(raw):,} bytes → {len(compressed):,} bytes "
    f"({100 * (1 - len(compressed) / len(raw)):.1f}% reduction)"
)

# --- remove the inline DB script block from index.html ---
script_end_pos = data_end + len(SCRIPT_END)
new_html = content[:idx] + content[script_end_pos:]

# --- collect static/js script tags and remove them (we reload dynamically) ---
body_srcs = re.findall(r'<script src="(static/js/[^"]+)"', new_html)
new_html = re.sub(r'[ \t]*<script src="static/js/[^"]+"></script>[ \t]*\n?', "", new_html)
print(f"Dynamic scripts ({len(body_srcs)}): {body_srcs}")

# --- inject async loader before </body> ---
# Fetches db.gz, decompresses via DecompressionStream, eval()s the full JS
# assignment (preserving escape-sequence semantics), then loads scripts in order.
loader = (
    "<script>\n"
    "(async function(){\n"
    '  var r=await fetch("static/js/db.gz");\n'
    "  eval(await new Response(r.body.pipeThrough(new DecompressionStream(\"gzip\"))).text());\n"
    "  var srcs=" + json.dumps(body_srcs) + ";\n"
    "  for(var i=0;i<srcs.length;i++){\n"
    "    await new Promise(function(ok,err){\n"
    '      var e=document.createElement("script");\n'
    "      e.src=srcs[i];e.onload=ok;e.onerror=err;\n"
    "      document.head.appendChild(e);\n"
    "    });\n"
    "  }\n"
    "})();\n"
    "</script>"
)

new_html = new_html.replace("</body>", loader + "\n</body>")

with open(INDEX, "w", encoding="utf-8") as f:
    f.write(new_html)

print(
    f"index.html: {len(content):,} bytes → {len(new_html):,} bytes"
)
