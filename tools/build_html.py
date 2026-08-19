#!/usr/bin/env python3
"""Render every tracked Markdown file to standalone HTML under html/.

    python tools/build_html.py

Math is pulled out of the source before Markdown runs and put back afterwards as
\\( … \\) and \\[ … \\], which are the only delimiters MathJax is configured to see.
A stray dollar sign therefore cannot start an equation — see the `**$10,000**` case
in shape-of-math-kontorovich.md, which renders as the money it is.

Needs: python-markdown (`pip install markdown`). No network at build time.
"""

import html
import io
import os
import re
import subprocess
import sys

import markdown

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(ROOT, "html")
TOKEN = "MATHPLACEHOLDER%dENDMATH"          # survives Markdown, tables and md_in_html
MAX_INLINE = 500                             # a longer $…$ span is not an equation

MATHJAX = """<script>
window.MathJax = {
  loader: {load: ['[tex]/mathtools', '[tex]/textmacros']},
  tex: {
    packages: {'[+]': ['mathtools', 'textmacros']},
    inlineMath: [['\\\\(', '\\\\)']],
    displayMath: [['\\\\[', '\\\\]']],
    processEscapes: false,
    macros: {fint: '{\\\\rlap{\\\\,\\\\text{--}}\\\\!\\\\int}'}
  },
  options: {skipHtmlTags: ['script', 'noscript', 'style', 'textarea', 'pre', 'code']}
};
</script>
<script async src="https://cdn.jsdelivr.net/npm/mathjax@3.2.2/es5/tex-mml-chtml.js"
  integrity="sha384-Wuix6BuhrWbjDBs24bXrjf4ZQ5aFeFWBuKkFekO2t8xFU0iNaLQfp2K6/1Nxveei"
  crossorigin="anonymous"></script>"""

CSS = """:root{color-scheme:dark}
*{box-sizing:border-box}
body{margin:0;background:#0f172a;color:#e2e8f0;
  font:16px/1.7 -apple-system,BlinkMacSystemFont,"Segoe UI",Roboto,"Helvetica Neue",sans-serif}
.wrap{max-width:52rem;margin:0 auto;padding:2.5rem 1.25rem 6rem}
a{color:#2dd4bf;text-decoration:none}
a:hover{text-decoration:underline}
h1,h2,h3,h4{line-height:1.25;color:#f1f5f9;margin:2.2rem 0 .8rem}
h1{font-size:1.9rem;margin-top:0}
h2{font-size:1.4rem;border-bottom:1px solid #334155;padding-bottom:.35rem}
h3{font-size:1.15rem;color:#fb923c}
h4{font-size:1rem;color:#cbd5e1}
p,li{color:#cbd5e1}
strong{color:#f1f5f9}
hr{border:0;border-top:1px solid #334155;margin:2.5rem 0}
blockquote{margin:1.4rem 0;padding:.6rem 1.1rem;border-left:3px solid #fb923c;
  background:#1e293b;border-radius:0 6px 6px 0;color:#cbd5e1}
blockquote p:last-child{margin-bottom:0}
code{background:#1e293b;border:1px solid #334155;border-radius:4px;
  padding:.1rem .35rem;font-size:.9em;color:#fb923c}
pre{background:#1e293b;border:1px solid #334155;border-radius:8px;
  padding:1rem;overflow-x:auto}
pre code{background:none;border:0;padding:0;color:#cbd5e1}
.tablewrap{overflow-x:auto;margin:1.4rem 0}
table{border-collapse:collapse;width:100%;font-size:.94rem}
th,td{border:1px solid #334155;padding:.5rem .7rem;text-align:left;vertical-align:top}
th{background:#1e293b;color:#f1f5f9}
details{background:#1e293b;border:1px solid #334155;border-radius:8px;
  padding:.7rem 1rem;margin:1.2rem 0}
details[open]{padding-bottom:1rem}
summary{cursor:pointer;color:#2dd4bf;font-weight:600}
.meta{background:#1e293b;border:1px solid #334155;border-radius:10px;
  padding:1rem 1.2rem;margin:0 0 2rem;font-size:.92rem;color:#94a3b8}
.meta div{margin:.2rem 0}
.meta b{color:#cbd5e1;font-weight:600}
.home{display:inline-block;margin-bottom:1.5rem;font-size:.9rem;color:#94a3b8}
mjx-container{overflow-x:auto;overflow-y:hidden;max-width:100%}
mjx-container[display="true"]{margin:1.2rem 0}
"""

PAGE = """<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<meta name="color-scheme" content="dark">
<title>{title}</title>
<style>{css}</style>
{mathjax}
</head>
<body>
<div class="wrap">
{home}{meta}{body}
</div>
</body>
</html>
"""


def extract_math(src):
    """Replace every math span with a token. Returns (text, [(token, latex, display)]).

    The scanner steps over fenced blocks and inline code, so a dollar sign inside
    `code` is never math. Inline math may wrap across one line break — the corpus
    hard-wraps at 90 characters — but never across a blank line.
    """
    out, spans, i, n = [], [], 0, len(src)
    while i < n:
        ch = src[i]
        if src.startswith("```", i):                      # fenced code
            end = src.find("```", i + 3)
            end = n if end == -1 else end + 3
            out.append(src[i:end]); i = end; continue
        if ch == "`":                                     # inline code
            m = re.compile(r"(`+)").match(src, i)
            ticks = m.group(1)
            end = src.find(ticks, i + len(ticks))
            end = i + len(ticks) if end == -1 else end + len(ticks)
            out.append(src[i:end]); i = end; continue
        if ch == "\\" and i + 1 < n and src[i + 1] == "$":  # escaped dollar
            out.append("$"); i += 2; continue
        if src.startswith("$$", i):
            end = src.find("$$", i + 2)
            if end != -1:
                tok = TOKEN % len(spans)
                spans.append((tok, src[i + 2:end], True))
                out.append(tok); i = end + 2; continue
        if ch == "$":
            end = src.find("$", i + 1)
            body = src[i + 1:end] if end != -1 else ""
            ok = (end != -1 and body and len(body) <= MAX_INLINE
                  and not body[0].isspace() and not body[-1].isspace()
                  and "\n\n" not in body)
            if ok:
                tok = TOKEN % len(spans)
                spans.append((tok, body, False))
                out.append(tok); i = end + 1; continue
        out.append(ch); i += 1
    return "".join(out), spans


def restore_math(text, spans):
    for tok, latex, display in spans:
        assert text.count(tok) == 1, "token %s appears %d times" % (tok, text.count(tok))
        safe = html.escape(latex, quote=False)
        text = text.replace(tok, ("\\[%s\\]" if display else "\\(%s\\)") % safe)
    return text


def front_matter(src):
    """Split a leading YAML block. Returns (fields, rest)."""
    if not src.startswith("---\n"):
        return {}, src
    end = src.find("\n---", 4)
    if end == -1:
        return {}, src
    fields = {}
    for line in src[4:end].splitlines():
        m = re.match(r"^([a-z_]+):\s*(.+)$", line)
        if m:
            fields[m.group(1)] = m.group(2).strip().strip('"')
    return fields, src[end + 4:].lstrip("\n")


def link(url, text=None):
    return '<a href="%s">%s</a>' % (html.escape(url, quote=True), html.escape(text or url))


def meta_block(f):
    if not f:
        return ""
    rows = []
    if f.get("speaker"):
        rows.append("<div><b>Speaker:</b> %s</div>" % html.escape(f["speaker"]))
    if f.get("event") or f.get("date"):
        rows.append("<div><b>Talk:</b> %s</div>"
                    % html.escape(" — ".join(x for x in (f.get("event"), f.get("date")) if x)))
    if f.get("source"):
        rows.append("<div><b>Video:</b> %s</div>" % link(f["source"]))
    if f.get("paper", "").startswith("http"):
        rows.append("<div><b>Companion:</b> %s</div>" % link(f["paper"].split()[0]))
    if f.get("difficulty_for_you"):
        rows.append("<div><b>Level:</b> %s</div>" % html.escape(f["difficulty_for_you"]))
    if f.get("reading_time"):
        rows.append("<div><b>Reading time:</b> %s</div>" % html.escape(f["reading_time"]))
    return '<div class="meta">%s</div>\n' % "".join(rows) if rows else ""


def convert(path):
    src = io.open(os.path.join(ROOT, path), encoding="utf-8").read()
    fields, body = front_matter(src)
    body, spans = extract_math(body)
    # Real <details> tags start a line; the ones inside `code` spans do not.
    body = re.sub(r"(?m)^<details>", '<details markdown="1">', body)

    md = markdown.Markdown(extensions=["extra", "sane_lists", "md_in_html"])
    out = md.convert(body)
    out = restore_math(out, spans)
    out = re.sub(r'(<table>)', r'<div class="tablewrap">\1', out)
    out = re.sub(r'(</table>)', r'\1</div>', out)
    # point cross-document links at the rendered pages, leave external URLs alone
    out = re.sub(r'href="(?!https?:)([^"#]+)\.md((?:#[^"]*)?)"', r'href="\1.html\2"', out)

    depth = path.count("/")
    title = fields.get("title") or re.search(r"(?m)^#\s+(.+)$", body).group(1) if re.search(
        r"(?m)^#\s+(.+)$", body) else os.path.basename(path)
    home = ('<a class="home" href="%sindex.html">← all documents</a>\n' % ("../" * depth))
    page = PAGE.format(title=html.escape(re.sub(r"[*`]", "", title)), css=CSS,
                       mathjax=MATHJAX, home=home, meta=meta_block(fields), body=out)

    dest = os.path.join(OUT, path[:-3] + ".html")
    os.makedirs(os.path.dirname(dest), exist_ok=True)
    io.open(dest, "w", encoding="utf-8", newline="\n").write(page)
    return dest, len(spans), sum(1 for s in spans if s[2])


def index(rendered):
    groups = {}
    for path, _, _ in rendered:
        groups.setdefault(os.path.dirname(path) or ".", []).append(path)
    parts = ["<h1>ICM 2026 — rendered documents</h1>",
             "<p>Every Markdown file in the repository, rendered with MathJax. "
             "The Markdown originals stay the source of truth.</p>"]
    labels = {".": "Top level", "summaries": "The twenty tutorials", "verify": "Verification record"}
    for d in sorted(groups, key=lambda x: (x != ".", x)):
        parts.append("<h2>%s</h2><ul>" % html.escape(labels.get(d, d)))
        for p in sorted(groups[d]):
            parts.append('<li><a href="%s.html">%s</a></li>' % (p[:-3], html.escape(p)))
        parts.append("</ul>")
    page = PAGE.format(title="ICM 2026 — rendered documents", css=CSS, mathjax="",
                       home="", meta="", body="\n".join(parts))
    io.open(os.path.join(OUT, "index.html"), "w", encoding="utf-8", newline="\n").write(page)


def main():
    files = [p for p in subprocess.check_output(
        ["git", "ls-files", "*.md"], cwd=ROOT, text=True).split() if p]
    rendered, total, disp = [], 0, 0
    for p in files:
        dest, n, d = convert(p)
        rendered.append((p, n, d))
        total += n
        disp += d
    index(rendered)
    print("%d files -> html/  (%d math spans, %d of them display)" % (len(files), total, disp))
    bad = [p for p, n, _ in rendered
           if "MATHPLACEHOLDER" in io.open(os.path.join(OUT, p[:-3] + ".html"),
                                           encoding="utf-8").read()]
    if bad:
        print("UNRESTORED PLACEHOLDERS in:", bad, file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
