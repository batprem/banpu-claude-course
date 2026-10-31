#!/usr/bin/env python3
"""Build workshop-sheet.html (M7) from ../workshop.md. Stdlib only.

Usage: python3 materials/m7/artifacts/build_workshop_sheet.py
One <section class="card"> per '## ' page; ```text -> copy-ready prompt; ```mermaid -> diagram
(mermaid@10.9.1); lines starting with ✅ -> checkbox checkpoint. Look and Export PDF follow the
M6 sheet (its <style> block is reused) and materials/_shared/export-pdf-artifact.html.
"""
import html, re, pathlib

HERE = pathlib.Path(__file__).resolve().parent
MD = HERE.parent / 'workshop.md'
OUT = HERE / 'workshop-sheet.html'
M6 = HERE.parents[1] / 'm6' / 'artifacts' / 'workshop-sheet.html'
SNIP = HERE.parents[1] / '_shared' / 'export-pdf-artifact.html'


def inline(s):
    s = html.escape(s, quote=False)
    s = re.sub(r'`([^`]+)`', r'<code>\1</code>', s)
    s = re.sub(r'\*\*(.+?)\*\*', r'<b>\1</b>', s)
    return s


def cells(line):
    return [c.strip() for c in line.strip().strip('|').split('|')]


def table(rows):
    head, body = cells(rows[0]), [cells(r) for r in rows[2:]]
    h = ''.join(f'<th>{inline(c)}</th>' for c in head)
    b = ''.join('<tr>' + ''.join(f'<td>{inline(c)}</td>' for c in r) + '</tr>' for r in body)
    return f'<div class="tbl"><table><thead><tr>{h}</tr></thead><tbody>{b}</tbody></table></div>'


def blocks(lines, pno, counter):
    out, i = [], 0
    while i < len(lines):
        ln = lines[i]
        if ln.startswith('```'):
            kind = ln[3:].strip()
            j = i + 1
            while not lines[j].startswith('```'):
                j += 1
            src = '\n'.join(lines[i + 1:j])
            if kind == 'mermaid':
                out.append('<div class="diagram mmd" role="img" aria-label="แผนภาพขั้นตอน">'
                           f'<pre class="mmd-src">{html.escape(src)}</pre></div>')
            else:
                counter['p'] += 1
                pid = f'pr{counter["p"]}'
                out.append(f'<div class="prompt"><div class="prompt-bar"><span>Prompt</span>'
                           f'<button class="copy-btn no-print" type="button" data-copy="{pid}">Copy</button></div>'
                           f'<pre id="{pid}">{html.escape(src)}</pre></div>')
            i = j + 1
            continue
        if ln.startswith('|'):
            j = i
            while j < len(lines) and lines[j].startswith('|'):
                j += 1
            out.append(table(lines[i:j]))
            i = j
            continue
        m = re.match(r'(\d+)\. ', ln)
        if ln.startswith('- ') or m:
            tag = 'ol' if m else 'ul'
            start = f' start="{m.group(1)}"' if m and m.group(1) != '1' else ''
            items = []
            while i < len(lines) and (re.match(r'\d+\. ', lines[i]) if m else lines[i].startswith('- ')):
                items.append(re.sub(r'^(\d+\.|-) ', '', lines[i]))
                i += 1
            out.append(f'<{tag}{start}>' + ''.join(f'<li>{inline(t)}</li>' for t in items) + f'</{tag}>')
            continue
        if not ln.strip():
            i += 1
            continue
        if ln.startswith('✅'):
            counter['c'] += 1
            cid = f'ck{pno}_{counter["c"]}'
            out.append(f'<label class="check" for="{cid}"><input type="checkbox" id="{cid}">'
                       f'<span>{inline(ln[1:].strip())}</span></label>')
        elif ln.startswith('🟧 คน (HITL)'):
            out.append(f'<p class="legend">{inline(ln)}</p>')
        elif ln.startswith('**เป้าหมาย:**'):
            out.append(f'<p class="goal">{inline(ln)}</p>')
        elif ln.startswith(('🔑', '🧑‍🏫', '💡', '🚀', '🛡️')):
            cls = 'note key' if ln.startswith('🔑') else 'note'
            out.append(f'<p class="{cls}">{inline(ln)}</p>')
        elif re.fullmatch(r'\*\*[^*]+\*\*(\s*\(.*\))?', ln.strip()):
            out.append(f'<h3>{inline(ln.strip())}</h3>')
        else:
            out.append(f'<p>{inline(ln)}</p>')
        i += 1
    return '\n'.join(out)


EXTRA_CSS = '''
/* M7 additions */
.mmd .mmd-src{margin:0;font-family:var(--f-mono);font-size:12.5px;white-space:pre-wrap;color:var(--muted)}
.mmd svg{display:block;max-width:100%;height:auto;margin:0 auto}
.mmd.done .mmd-src{display:none}
.note.key{background:var(--tint-blue)}
.check span{min-width:0}
.card-head .chip{white-space:normal}
'''


def page(sec, pno, total, counter):
    head, *rest = sec.split('\n')
    m = re.match(r'หน้า \d+ · (.+?)(?: \(([^()]*)\))?$', head.strip())
    title, when = m.group(1), (m.group(2) or '')
    counter['c'] = 0
    body = blocks(rest, pno, counter)
    brk = '' if pno == 1 else ' pdf-page-break'
    chip = f'<span class="chip">{inline(when)}</span>' if when else ''
    return (f'<section class="card{brk}" id="page{pno}" data-page="{pno}">\n'
            f'<div class="card-head"><div><div class="pg">หน้า {pno} / {total}</div>'
            f'<h2>{inline(title)}</h2></div>{chip}</div>\n{body}\n</section>')


SCRIPT = r'''
<script src="https://cdn.jsdelivr.net/npm/mermaid@10.9.1/dist/mermaid.min.js"></script>
<script>
(function(){
  var KEY='m7-workshop-v1', st={};
  try{st=JSON.parse(localStorage.getItem(KEY)||'{}')||{}}catch(e){st={}}
  var cards=[].slice.call(document.querySelectorAll('section.card'));
  function sync(){
    var done=0;
    cards.forEach(function(c){var b=c.querySelectorAll('.check input');var ok=b.length>0;
      b.forEach(function(x){if(!x.checked)ok=false});c.classList.toggle('done',ok);if(ok)done++;});
    document.getElementById('progBar').style.width=(done/cards.length*100)+'%';
    document.getElementById('progText').textContent=done+' / '+cards.length+' หน้า';
  }
  document.querySelectorAll('.check input').forEach(function(x){
    x.checked=!!st[x.id];
    x.addEventListener('change',function(){st[x.id]=x.checked;try{localStorage.setItem(KEY,JSON.stringify(st))}catch(e){}sync();});
  });
  sync();
  document.querySelectorAll('.copy-btn').forEach(function(b){
    b.addEventListener('click',function(){
      var pre=document.getElementById(b.dataset.copy),t=pre.textContent;
      function sel(){var r=document.createRange();r.selectNodeContents(pre);var s=getSelection();s.removeAllRanges();s.addRange(r);b.textContent='เลือกข้อความแล้ว กด Ctrl+C';}
      function ok(){b.textContent='คัดลอกแล้ว ✓';setTimeout(function(){b.textContent='Copy'},1800);}
      try{navigator.clipboard.writeText(t).then(ok,sel)}catch(e){sel()}
    });
  });
  if(window.mermaid){
    try{
      mermaid.initialize({startOnLoad:false,securityLevel:'strict',theme:'base',
        fontFamily:"'IBM Plex Sans Thai',sans-serif",flowchart:{htmlLabels:false,curve:'basis'},
        themeVariables:{lineColor:'#5B6670',primaryTextColor:'#1F2933',edgeLabelBackground:'#FFFFFF',fontSize:'14px'}});
      document.querySelectorAll('.mmd').forEach(function(d,i){
        var src=d.querySelector('.mmd-src').textContent;
        mermaid.render('m7mmd'+i,src).then(function(r){d.insertAdjacentHTML('beforeend',r.svg);d.classList.add('done');},function(){});
      });
    }catch(e){}
  }
})();
</script>
<script>document.documentElement.lang='th';document.body.setAttribute('data-pdf-name','M7-Workshop');</script>
'''


def main():
    md = MD.read_text(encoding='utf-8')
    top, *secs = re.split(r'^## ', md, flags=re.M)
    tl = top.strip().split('\n')
    h1 = tl[0].lstrip('# ').strip()
    intro = ' '.join(x for x in tl[1:] if x.strip())
    style = re.search(r'<style>(.*?)</style>', M6.read_text(encoding='utf-8'), re.S).group(1)
    style = style.replace('/* Layout: one calm column of 4 workshop "pages"', '/* Layout: one calm column of 13 workshop "pages"')
    style = style.replace('design → schedule → test run → decide.', 'team → canvas → build → present.')
    snip = SNIP.read_text(encoding='utf-8')
    scripts = snip[snip.index('<script src='):]
    btn = re.search(r'<button class="export-pdf-btn[^>]*>.*?</button>\n', scripts).group(0)
    scripts = scripts.replace(btn, '')
    counter = {'p': 0, 'c': 0}
    n = len(secs)
    pages = '\n\n'.join(page(s.rstrip(), k + 1, n, counter) for k, s in enumerate(secs))
    doc = f'''<title>M7 Workshop</title>
<meta name="claude:viewport-fit-sides" content="cover">
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=IBM+Plex+Sans+Thai:wght@400;600;700&family=IBM+Plex+Mono:wght@400;600&display=swap">
<style>{style}{EXTRA_CSS}</style>
<!-- generated by build_workshop_sheet.py from ../workshop.md; edit the .md and re-run -->

<div class="strip no-print">
  <div class="wrap strip-row">
    <div class="strip-title">M7 Workshop <span>· Capstone: Use Case จริงของเรา</span></div>
    <div class="prog" aria-label="ความคืบหน้า">
      <div class="track"><i id="progBar"></i></div>
      <b id="progText">0 / {n} หน้า</b>
    </div>
    {btn.strip()}
  </div>
</div>

<main class="wrap" data-pdf-root>
<header class="intro">
  <span class="eyebrow">M7 · Capstone</span>
  <h1>{inline(h1)}</h1>
  <p>{inline(intro)}</p>
</header>

{pages}

<footer>Banpu · Claude for Business · M7 Capstone · ข้อมูลทั้งหมดเป็นข้อมูลสมมติ · Connector: SharePoint + Outlook เท่านั้น</footer>
</main>
{SCRIPT}{scripts}'''
    OUT.write_text(doc, encoding='utf-8')
    print(f'{OUT.name}: {n} pages, {counter["p"]} prompts, {doc.count("class=\"diagram mmd")} diagrams')


if __name__ == '__main__':
    main()
