#!/usr/bin/env python3
"""Render materials/<mN>/slides.md into a 16:9 HTML deck (slides.html).

Format (see materials/STYLE.md):
  front matter between the first two '---' lines (key: value),
  then slides separated by a line containing only '---',
  speaker notes after a line containing only '???'.

Usage: python3 tools/build_slides.py materials/m1/slides.md [--count]
Markdown and Mermaid are rendered in the browser (marked + mermaid from jsDelivr).
Keys: ←/→ navigate, N toggles notes, P prints (one slide per page).
"""
import html
import json
import pathlib
import re
import sys


def parse(text):
    meta, body = {}, text
    m = re.match(r"^---\n(.*?)\n---\n", text, re.S)
    if m:
        for line in m.group(1).splitlines():
            if ":" in line:
                k, v = line.split(":", 1)
                meta[k.strip()] = v.strip()
        body = text[m.end():]
    slides = []
    for chunk in re.split(r"^---[ \t]*$", body, flags=re.M):
        if not chunk.strip():
            continue
        content, _, notes = chunk.partition("\n???\n")
        kind = re.search(r"<!--\s*type:\s*(\w+)\s*-->", content)
        slides.append({"md": content.strip(), "notes": notes.strip(),
                       "type": kind.group(1) if kind else "content"})
    return meta, slides


TEMPLATE = """<!doctype html>
<html lang="th"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>__TITLE__</title>
<link href="https://fonts.googleapis.com/css2?family=IBM+Plex+Sans+Thai:wght@400;600;700&display=swap" rel="stylesheet">
<style>
:root{--human:#E4572E;--ai:#2E86AB;--data:#3BA55C;--ink:#1F2933;--paper:#FAF8F3;--warn:#F2A541}
*{box-sizing:border-box}
body{margin:0;background:#2b2f33;font-family:'IBM Plex Sans Thai',sans-serif;color:var(--ink)}
.slide{width:1280px;height:720px;margin:24px auto;background:var(--paper);position:relative;overflow:hidden;
  padding:56px 72px 48px;display:none;border-top:10px solid var(--ai)}
.slide.active{display:block}
.slide h1{font-size:44px;margin:0 0 24px;line-height:1.25}
.slide h2{font-size:32px;margin:0 0 16px}
.slide p,.slide li{font-size:26px;line-height:1.55}
.slide table{border-collapse:collapse;font-size:20px;width:100%}
.slide th,.slide td{border-bottom:1px solid #d9d4c7;padding:6px 10px;text-align:left}
.slide th{background:#efeadf}
.slide code{background:#efeadf;padding:1px 6px;border-radius:4px;font-size:.85em}
.slide pre{background:#1F2933;color:#f5f5f5;padding:16px;border-radius:8px;font-size:18px;white-space:pre-wrap}
.slide pre code{background:none;color:inherit}
.slide img{max-width:100%;max-height:440px;display:block;margin:8px auto}
.slide blockquote{border-left:6px solid var(--warn);margin:12px 0;padding:4px 18px;background:#fff6e6}
.slide .mermaid{display:flex;justify-content:center}
.slide.section{background:var(--ai);color:#fff;display:none;flex-direction:column;justify-content:center;border-top:0}
.slide.section.active{display:flex}
.slide.section h1{font-size:60px}
.slide.story{border-top-color:var(--human)}
.slide.story::before{content:"เรื่องเล่า / Case";position:absolute;top:18px;right:72px;font-size:16px;color:var(--human);font-weight:700}
.foot{position:absolute;bottom:16px;left:72px;right:72px;display:flex;justify-content:space-between;font-size:14px;opacity:.6}
.notes{width:1280px;margin:0 auto 24px;background:#fffbe8;padding:12px 18px;font-size:16px;display:none;white-space:pre-wrap}
body.show-notes .notes.active{display:block}
@media print{
  @page{size:1280px 720px;margin:0}
  body{background:#fff}
  .slide,.slide.section{display:block!important;margin:0;page-break-after:always;break-after:page}
  .slide.section{display:flex!important}
  .notes{display:none!important}
}
</style></head><body>
<div id="deck"></div>
<script src="https://cdn.jsdelivr.net/npm/marked@12.0.2/marked.min.js"></script>
<script src="https://cdn.jsdelivr.net/npm/mermaid@10.9.1/dist/mermaid.min.js"></script>
<script>
const META = __META__;
const SLIDES = __SLIDES__;
const deck = document.getElementById('deck');
marked.use({renderer:{code(code, lang){
  if(lang==='mermaid') return '<div class="mermaid">'+code+'</div>';
  return false;}}});
SLIDES.forEach((s,i)=>{
  const el=document.createElement('section');
  el.className='slide '+s.type; el.innerHTML=marked.parse(s.md)+
    '<div class="foot"><span>'+(META.module||'')+' · '+(META.title||'')+'</span><span>'+(i+1)+' / '+SLIDES.length+'</span></div>';
  deck.appendChild(el);
  const n=document.createElement('div'); n.className='notes'; n.textContent=s.notes; deck.appendChild(n);
});
mermaid.initialize({startOnLoad:false,theme:'base',themeVariables:{fontFamily:'IBM Plex Sans Thai',fontSize:'20px'}});
let cur=Math.max(0,Math.min(SLIDES.length-1,(parseInt(location.hash.slice(1))||1)-1));
const slides=[...document.querySelectorAll('.slide')], notes=[...document.querySelectorAll('.notes')];
async function show(i){cur=Math.max(0,Math.min(slides.length-1,i));
  slides.forEach((s,j)=>s.classList.toggle('active',j===cur));
  notes.forEach((s,j)=>s.classList.toggle('active',j===cur));
  history.replaceState(null,'','#'+(cur+1));
  const pending=slides[cur].querySelectorAll('.mermaid:not([data-processed])');
  if(pending.length) await mermaid.run({nodes:pending});}
document.addEventListener('keydown',e=>{
  if(['ArrowRight','PageDown',' '].includes(e.key)) show(cur+1);
  if(['ArrowLeft','PageUp'].includes(e.key)) show(cur-1);
  if(e.key==='n') document.body.classList.toggle('show-notes');
  if(e.key==='p'){mermaid.run({querySelector:'.mermaid:not([data-processed])'}).then(()=>window.print());}
});
window.addEventListener('beforeprint',()=>mermaid.run({querySelector:'.mermaid:not([data-processed])'}));
show(cur);
</script></body></html>
"""


def main():
    if len(sys.argv) < 2:
        sys.exit(__doc__)
    src = pathlib.Path(sys.argv[1])
    meta, slides = parse(src.read_text(encoding="utf-8"))
    if "--count" in sys.argv:
        print(f"{src}: {len(slides)} slides")
        return
    out = src.with_suffix(".html")
    page = (TEMPLATE.replace("__TITLE__", html.escape(meta.get("title", src.stem)))
            .replace("__META__", json.dumps(meta, ensure_ascii=False))
            .replace("__SLIDES__", json.dumps(slides, ensure_ascii=False).replace("</", "<\\/")))
    out.write_text(page, encoding="utf-8")
    print(f"{out}: {len(slides)} slides")


if __name__ == "__main__":
    main()
