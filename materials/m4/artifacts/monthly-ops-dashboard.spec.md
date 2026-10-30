# Spec · Monthly Ops Dashboard (Artifact)

File: `monthly-ops-dashboard.html` · Owner: M4 · Reused by: M6 (the report that gets scheduled), M7 (Capstone reference)

## Purpose
A reference answer for workshop page 4 and the live demo for slides 7–8. Shows what "Artifact as Output Layer" looks like for the Monthly Operations Report built from 5 sources, and makes **iteration (v1 → v2)** and the **Human-in-the-Loop number check** visible. Covers requirements 4, 6, 11 (Hands-on) and 7 (the big-file note).

## Users
- Trainer: projects it in the lecture (slide 7) and shares the link after workshop page 4.
- Learners: compare their own dashboard with it; managers in the story ("ผู้บริหารฝ่ายปฏิบัติการ") are the imagined viewers.

## Interactions
1. **v1 / v2 toggle** (header): v1 = sites in code order, all projects, no causes. v2 = the result of 3 feedback items (worst-first sort, cause labels from e-mail/projects, only non-On-track projects). A note explains the change, which is the iteration lesson.
2. KPI row (4 tiles): sites worse than budget > 5 %, total cost vs budget, projects At risk/Delayed, Australian coal price with month-on-month change.
3. 6 site cards with traffic-light dots (worse of volume shortfall and unit-cost overrun: ≤ 2 % green, 2–5 % amber, > 5 % red). Clicking a card opens the detail panel: bar chart of % vs budget Jan–Sep 2569, Sep and YTD table, shift-log stats (mines), cause + reference, site projects.
4. Energy prices: 3 sparklines (coal, Brent, LNG Asia), last 12 months, with source line.
5. Projects table (SharePoint List) + open Issue Log counts.
6. HITL checklist of 3 numbers; a badge appears when all 3 are ticked.
7. Sources box (5 sources, internal/external tags) + note that the ~37 MB full report goes to SharePoint as a link.

## Export PDF
Header button from `materials/_shared/export-pdf.html`. Print CSS hides the toggle/buttons, keeps site cards (they are `<button>`s, re-shown via `.site{display:block!important}`), keeps 2-column layout and adds a print-only table of all 6 sites with causes. Tested in headless Chrome: 4 A4 pages.

## Data
- One line `/*DATA*/const DATA=…;/*END*/` in the HTML, written by `data/sync_dashboard.py` from `data/dashboard_data.json` (made by `data/gen_m4_data.py`) + hand-written `CAUSES` in the sync script.
- Internal numbers are synthetic (seed 2569). Energy prices are real public data (IMF via FRED, `data/energy_prices_public_2023-2026.csv`), refreshed with `data/fetch_energy_prices.py`.
- People, sites and e-mails are fictional (`@example.com`), and match the M3 SharePoint/Outlook pack.

## Engagement mechanic
"Be the manager": find the problem site in 10 seconds, click it to see why, flip v1 ↔ v2 to feel what good feedback does, tick the 3-number check to earn the "พร้อมส่ง" badge.

## Constraints
Self-contained (Google Fonts only), inline SVG charts, no network/AI calls (no Team plan usage), no storage. Colours from STYLE.md. Responsive down to phone width.
