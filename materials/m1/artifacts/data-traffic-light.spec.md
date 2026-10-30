# Spec · Data Traffic Light (Artifact)

File: `data-traffic-light.html` · Owner: M1 · Reused by: M8 (security recap / quiz)

## Purpose
Learners practise deciding whether a piece of data may go into Claude: 🟢 เขียว ใช้ได้ · 🟡 เหลือง ต้อง anonymize · 🔴 แดง ห้ามใส่ Claude. Covers requirement 2 (Hands-on).

## Users
- Learners (30–40 per class) on laptops, solo or in pairs. Opened as a Claude Artifact (shared via company Claude Team account) or as a local HTML file.
- Trainer projects the same page for debrief.

## Interactions
1. Optional name/team field (shown on the PDF).
2. One card at a time (shuffled): title + grey "sample" box with synthetic content.
3. Answer with 3 big colour buttons or keys 1/2/3. Locked after the first answer.
4. Instant feedback: correct/incorrect, the right colour, **เหตุผล** and **ทำให้ปลอดภัยอย่างไร**.
5. Enter / "ใบถัดไป" advances. HUD: card x/15, score, streak; progress bar.
6. Result screen: score, badge (15/15 gold, ≥80% silver, otherwise "review"), correct count per colour, textarea "กฎ 3 ข้อของฉัน", replay (reshuffle).
7. Answer key with learner's choice per card appears after finishing.

## Export PDF
- Button in header and on the result screen, from `materials/_shared/export-pdf.html` (window.print + print CSS).
- Print: hides controls/game card; shows player, score, the 3 rules and the full answer key for all 15 cards (`.print-expand`), even if the game is unfinished.

## Data
- Card deck is a JSON block `<script type="application/json" id="cards-data">` inside the HTML.
- Canonical source: `materials/m1/data/traffic_light_cards.json`. Edit the JSON, then run `python3 materials/m1/data/sync_cards.py` (validates unique ids and answers).
- Card fields: `id`, `title`, `sample`, `answer` (green|yellow|red), `why`, `tip`, `module`.
- **M8 extension:** copy the JSON, add cards with `"module": "M8"` (ids C16+), then `python3 materials/m1/data/sync_cards.py <m8.json> <m8 game.html>` on a copy of the HTML in `materials/m8/`. The game reads any number of cards.
- All cards are synthetic; names like "คุณสมมติ ใจดี", emails `@example.com` (incl. `supplier.example.com`), Site A–H.

## Engagement mechanic
Instant feedback + streak (🔥 at 3, "Data Guardian" at 5) + badge + replay with shuffle + personal rules that end up in the learner's own PDF. Debrief uses the "commonly missed" cards (C05, C10, C15) whose colour changes with context.

## Constraints
- Self-contained: only Google Fonts (IBM Plex Sans Thai). No network calls, no AI calls (uses no Team plan usage), no storage.
- Colours from STYLE.md; responsive down to phone width; keyboard accessible.
- Classifications are teaching defaults; the real rule set follows Banpu IT/Data policy (open question in README).
