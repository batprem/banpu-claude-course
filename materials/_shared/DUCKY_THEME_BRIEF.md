# Brief: apply the Ducky Engineer (วิศวกรเป็ด) theme to a module

Owner: course-orchestrator. Approved by Prem on 2 Nov 2026 (logo use approved). Reference implementation: the M1 deck, commit `0010ddd` (`git show 0010ddd -- materials/m1/deck` shows every change), live at https://claude.ai/artifact/B5QugBgGE4eWMe69TrCvbv.

Theme: font **Sarabun** · duck yellow `#FFD066` (primary) · ink `#231F20` · accent blue `#0684C9` · background `#F4F4F4` · light yellow band `#FFF3D1`. **Diagram role colours stay unchanged** (HITL `#E4572E`, AI `#2E86AB`, Data `#3BA55C`; boxes, legends and connectors that use them). Content, slide/page counts, speaker notes and Export PDF stay exactly as they are. Same URLs: always republish to the existing Artifact URL from the module README, never create a new Artifact.

## A. Slides deck (`materials/<mN>/deck/`, Slides Artifact type)
Follow the Slides type rules (sed only for simple same-change swaps; Edit for the rest; no scripts that generate slide files).
1. `Artifact read` the deck's `project/deck.json` and every `project/slides/*.html` (out_dir in your scratchpad), compare with the local files; if a published file differs, adopt the published one first.
2. Upload `materials/branding/ducky-logo-AW_Logo-Duck-03.png` to the deck (`action: publish`, `url` = deck, `file_path` = that PNG, `asset: true`) and use the returned `/_blob/<id>` verbatim.
3. Font: in every slide replace `font-family:'IBM Plex Sans Thai', Tahoma, sans-serif;` with `font-family:'Sarabun', Tahoma, sans-serif;` (keep other families such as `'Courier New', monospace`). In `deck.json` replace the face with `"sarabun":{"family":"Sarabun","href":"https://fonts.googleapis.com/css2?family=Sarabun:wght@400;600;700&display=swap"}`.
4. Cover (s01): rebuild like M1 s01 — `background:#FFD066;color:#231F20`, row layout: left column with eyebrow `วิศวกรเป็ด · DUCKY ENGINEER × CLAUDE FOR BUSINESS · โมดูล <n>` (28px, 700, ink), the module's own h1 / subtitle (`#4C402D`) / time pill (`color:#FFD066;background:#231F20;border-radius:40px`), right: 520px white circle (`#FFFDF8`, shadow) holding the logo at 440px. Keep the cover's own text; drop the old colour stripe; a cover illustration may stay only if it fits beside the logo (say what you did).
5. Every slide except the cover: insert before `<aside>` the badge
   `<div style="position:absolute;right:40px;bottom:32px;width:88px;height:88px;background:#FFFDF8;border-radius:50%;display:flex;align-items:center;justify-content:center;box-shadow:0 2px 8px rgba(35,31,32,0.15)"><img src="/_blob/<id>" alt="Ducky Engineer" style="width:72px;height:72px;object-fit:contain"></div>`
   If something already sits in that corner, move the badge just enough to avoid it and say so.
6. Section dividers (dark `background:#1F2933` slides with a centred h1 and a `ส่วนที่ …`/`WORKSHOP` eyebrow) become yellow — on those files only:
   `sed -i -e 's/background:#1F2933/background:#FFD066/g' -e 's/color:#FAF8F3/color:#231F20/g' -e 's/color:#F2A541/color:#231F20/g' -e 's/color:#C9D1D9/color:#4C402D/g'`
   Dark closing/summary or accent slides that are not section dividers stay dark ink.
7. All slides:
   `sed -i -e 's/background:#FAF8F3/background:#F4F4F4/g' -e 's/color:#1F2933/color:#231F20/g' -e 's/background:#1F2933/background:#231F20/g' -e 's/background:#F3EDE2/background:#FFF3D1/g' -e 's/color:#3A4651/color:#3D3839/g' -e 's/color:#5B6670/color:#5E5859/g' -e 's/color:#2E86AB/color:#0684C9/g' -e 's/background:#E8F1F6/background:#E2F1FA/g' -e 's/background:#FDF1DC/background:#FFF3D1/g' -e 's/#F2A541/#FFD066/g' -e 's/color:#FAF8F3/color:#FFFDF8/g' -e 's/#E7E1D5/#E2E2E2/g'`
   Then fix by hand: icons (`x-icon`) now `color:#FFD066` on a light background → `color:#0684C9`; any `#FFD066` text on a light background → ink or blue. Check other old hexes the module uses (`grep -o '#[0-9A-Fa-f]\{6\}'`) and map them in the same spirit.
8. Story/case slides (eyebrow `STORY`): left bar `#E4572E` → `#FFD066`, eyebrow `#B5461F` → `#0684C9` (700), quote `border-left … #E4572E` → `#FFD066`. Diagram edge labels in `#B5461F` stay.
9. Checks before publishing: no `IBM Plex`, no `#1F2933 #FAF8F3 #F3EDE2 #3A4651 #5B6670 #E8F1F6 #FDF1DC #F2A541 #C9D1D9 #E7E1D5`; role-colour box counts unchanged from before; badge on every slide but the cover; one `<section>` + `<aside>` per slide. Publish `deck.json` + all slide files to the same `url` with `root: materials/<mN>/deck`. Read back deck.json + 3 slides to confirm.

## B. Workshop sheet + interactive pages (`materials/<mN>/artifacts/*.html`)
1. For each page: `Artifact read` its existing URL (from the README table) to see the live version; if it differs from the local file, adopt the live one first.
2. Run `python3 tools/apply_ducky_page_theme.py materials/<mN>/artifacts/<file>.html` (font → Sarabun, ink/paper/warning hexes, embedded logo badge; role colours kept; idempotent).
3. Where reasonable, by hand with Edit: header/hero bars to duck yellow `#FFD066` with ink text (or keep ink headers with a yellow accent if contrast needs it); primary buttons/links/accents to `#0684C9`; keep role-colour meaning (HITL/AI/Data) and all behaviour. Keep the Export PDF snippet working.
4. Publish each page to its **existing URL** (`url` + `file_path`, `capabilities: {downloads: true}`), never a new Artifact. Read back once to confirm.

## C. Report (worker_done)
- Each Artifact: file → URL, and the sharing line the publish result printed ("readable by …" / "shared as …").
- Old-colour/IBM checks, badge counts, anything you could not theme and why.
- Do not edit other modules, STATUS.md, STYLE.md, briefs or tools. Do not commit or push.
