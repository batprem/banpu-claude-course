# M2 · Cowork กับไฟล์และโฟลเดอร์ในงานจริง + Prompt Patterns

10:30–11:15 · 45 นาที (Lecture 15 · Workshop 30) · Requirements 1, 4, 5, 7, 12

## Page counts (budget)
| Item | Built | Budget |
|---|---|---|
| Lecture slides (`slides.md`) | 15 | 15 (1 slide/min) |
| Workshop pages (`workshop.md`, `## ` sections) | 6 | 6 (1 page/5 min) |
| Prompts (`prompts.md`) | 20 (M2-P01…P20) | — |
| Diagrams (`diagrams/*.mmd`) | 8 | every workflow |
| Artifacts | 4 (+ spec each) | — |

## Timing
| Time | Min | Block | Material |
|---|---|---|---|
| 10:30–10:31 | 1 | เปิดโมดูล + เป้าหมาย | slides 1–2 |
| 10:31–10:36 | 5 | Upload vs Project vs Cowork folder · Input → Process → Output · Plan → Approve → Execute | slides 3–5 |
| 10:36–10:38 | 2 | Story: Replit agent ลบ production database | slide 6 |
| 10:38–10:42 | 4 | Prompt Patterns 3 แบบ (Use your own words · Interview/grill-me · Prototype first) | slides 7–10, Prompt Playground |
| 10:42–10:45 | 3 | Demo: จัดโฟลเดอร์ ~1,500 ไฟล์ · ข้อจำกัดข้อมูลขนาดจริง · เข้า workshop | slides 11–15 |
| 10:45–10:48 | 3 | Workshop หน้า 1: เตรียมโฟลเดอร์ | workshop p1, Workshop Companion |
| 10:48–11:00 | 12 | Workshop B: Excel กระจัดกระจาย → Insight | workshop p2–3, Excel Detective |
| 11:00–11:12 | 12 | Workshop A: PowerPoint (Interview → … → Prototype ×3 → Build) | workshop p4–5, Prototype Gallery |
| 11:12–11:15 | 3 | ลองเอง: จัดโฟลเดอร์แบบ Plan only + สรุป | workshop p6 |

## Requirement coverage
| Req | Where | Depth |
|---|---|---|
| 1 M365-first context | Workshop A/B output Word/Excel/PPTX; Sample Pack via room SharePoint | Hands-on |
| 4 Multiple sources/formats | Workshop B: 13 Excel/CSV files, inconsistent schemas → one table; PDF 320 pages | Hands-on |
| 5 Human-in-the-Loop | Plan → Approve → Execute slide + ✅ checkpoint on every workshop step | Hands-on |
| 7 Limits with real volume | `data/generate_big_files.py`: CSV ~200k rows (12.9 MB), PDF 320 pages; workaround diagram | Demo |
| 12 Folder restructure | `data/generate_messy_folder.py` (~1,500 files, 2562–2569) demo + workshop p6 Plan only | Demo + Hands-on |

## Files

| Path | What |
|---|---|
| **Slides Artifact** · https://claude.ai/artifact/3kKwMXkqyNFfRMEQxCQVwu | **Delivery deck.** 15 slides built on Claude's core Slides Artifact type; speaker notes on every slide; Present mode; download as PDF/PPTX from Share › Export. All 8 Mermaid diagrams redrawn natively (boxes + connectors) in the 3 STYLE colours with legend; 2 `img/` illustrations uploaded as assets. Private until shared from the page's Share menu |
| `deck/project/deck.json` + `deck/project/slides/s01–s15.html` | Source files of the Slides Artifact (republish with the Artifact tool, `root: materials/m2/deck`) |
| `slides.md` → `slides.html` | Content source the Artifact was built from (same 15 slides and notes); superseded for delivery |

- `slides.md` / `slides.html` · `workshop.md` · `prompts.md` · `diagrams/` (8) · `img/` (2 generated illustrations)
- `artifacts/`: Workshop Companion · Prompt Playground · Excel Detective · Prototype Gallery (each `.html` + `.spec.md`, Export PDF)
- `data/` — **core Sample Data Pack** (owner M2, reused read-only by M3–M7):
  - `generate_core_pack.py` (seed 2569) → `core/ops_monthly_clean.{csv,xlsx}` (fictional sites, 3 years, Budget vs Actual), `workshop_b_scattered/` (13 messy files), `answer_key/insights.md` (trainer only)
  - `generate_messy_folder.py` → `out/` messy folder (~1,500 files) · `generate_big_files.py` → `out/` 200k-row CSV + 320-page PDF. `out/` is gitignored; regenerate with `python3 data/generate_*.py`.

## Claude Artifacts (claude.ai)

All private until shared from each page's Share menu. Every page except the Slides deck is published with `capabilities: {downloads: true}` and the shared `materials/_shared/export-pdf-artifact.html` snippet (html2pdf → downloads, fallback window.print). To republish, use the Artifact tool with the same file path, or pass the URL from another session.

| Artifact | File | claude.ai URL | Export PDF |
|---|---|---|---|
| M2 Slides (delivery deck) | `deck/project/` (Slides type) | https://claude.ai/artifact/3kKwMXkqyNFfRMEQxCQVwu | ✅ (Share › Export PDF/PPTX) |
| M2 Workshop (workshop sheet, 6 pages) | `artifacts/workshop-sheet.html` | https://claude.ai/artifact/2kVCrZwhnqqwMHBF326PvR | ✅ |
| Workshop Companion | `artifacts/workshop-companion.html` | https://claude.ai/artifact/Vyp7t1u44Ga5W4YbpuMYdP | ✅ |
| Excel Detective | `artifacts/excel-detective.html` | https://claude.ai/artifact/1ytRQDkazJW4Xw24zZwkLu | ✅ |
| Prompt Playground | `artifacts/prompt-playground.html` | https://claude.ai/artifact/LQ7Mh4vNj4syXPARm6ucV8 | ✅ |
| Prototype Gallery | `artifacts/prototype-gallery.html` | https://claude.ai/artifact/3s1YpuHwGK7QvSn7ogm2Aq | ✅ |

## Build notes
- Built by the M2 Orca worker; it was cut off twice by API connection loss before finishing. The orchestrator wrote this README, `SOURCES.md` and the 4 Artifact specs and reviewed the module.

## Open questions for Prem
1. Sample Pack distribution: room SharePoint site (as the slides say) — will IT provide one, or do we hand out a zip/USB?
2. Prototype Gallery shared voting needs Artifact shared storage + company accounts for viewers; if not available on the day, fall back to show of hands.
3. Matt Pocock `grill-me` licence: listed as MIT by repo listings — confirm against the LICENSE file before printing handouts.
4. Folder-restructure demo: run live on the trainer laptop (~1,500 files) or show a recording if Cowork is slow on the venue Wi-Fi?
