# M3 · Microsoft 365 Connectors อย่างปลอดภัย

11:15–12:00 · 45 นาที (Lecture 15 · Workshop 30) · Requirements 1, 3, 4, 5, 7

## Page counts (budget)
| Item | Built | Budget |
|---|---|---|
| Lecture slides (`slides.md`) | 15 | 15 (1 slide/min) |
| Workshop pages (`workshop.md`, `## ` sections) | 6 | 6 (1 page/5 min) |
| Prompts (`prompts.md`) | 9 (M3-P01…P09) | — |
| Diagrams (`diagrams/*.mmd` + workshop) | 6 + 1 inline | every workflow |
| Artifacts | 1 Connector Mission (+ spec) | — |

## Timing
| Time | Min | Block | Material |
|---|---|---|---|
| 11:15–11:16 | 1 | เปิดโมดูล + เป้าหมาย | slides 1–2 |
| 11:16–11:19 | 3 | AI → Connect → Data → Execute · Connector ที่ใช้ได้ (SharePoint + Outlook) · เปิดใช้ 3 คน 3 ขั้น | slides 3–5 |
| 11:19–11:21 | 2 | Read vs Write · Story: PHE 15,841 เคสหายเพราะไฟล์ Excel | slides 6–7 |
| 11:21–11:24 | 3 | Excel ที่หลายคนแก้พร้อมกัน · copy-before-write | slides 8–9 |
| 11:24–11:28 | 4 | หลายแหล่ง → สรุปเดียว · Demo 3 แหล่ง · Demo Capex Tracker (เรื่องสมมติ) | slides 10–12 |
| 11:28–11:30 | 2 | ข้อจำกัด + ทางเลี่ยง · แนะนำ workshop · 5 กฎ | slides 13–15 |
| 11:30–12:00 | 30 | Workshop 6 หน้า (3 · 5 · 8 · 5 · 6 · 3 นาที) | workshop p1–6, Connector Mission |

## Requirement coverage
| Req | Where | Depth |
|---|---|---|
| 1 M365-first | Outlook + SharePoint (site, List, Excel) throughout | Hands-on |
| 3 Approved connectors, Read/Write, copy-before-write | slides 3–9, workshop p2, p5–6, Artifact stage 5 | Hands-on |
| 4 Multiple sources/formats | email (.eml) + SharePoint List (CSV) + Excel → one summary (workshop p3–4) | Hands-on |
| 5 Human-in-the-Loop before write | M3-P06 "รอฉันพิมพ์อนุมัติ", Artifact approve/reject plan, M3-P09 draft-only email | Hands-on |
| 7 Connector limits + workarounds | slide 13 (tenant-wide search, partial results, write tools), PHE story, workshop p2/p4 checkpoints | Demo + Hands-on |

## Files

| Path | What |
|---|---|
| **Slides Artifact** · https://claude.ai/artifact/MFFCrgSvtQS9S4guydcnoz | **Delivery deck.** 15 slides built on Claude's core Slides Artifact type; speaker notes on every slide; Present mode; download as PDF/PPTX from Share › Export. All 6 diagrams redrawn natively (boxes + connectors) in the 3 STYLE colours with legend. Private until shared from the page's Share menu |
| `deck/project/deck.json` + `deck/project/slides/s01–s15.html` | Source files of the Slides Artifact (republish with the Artifact tool, `root: materials/m3/deck`) |
| `slides.md` → `slides.html` | Content source the Artifact was built from (same 15 slides and notes); superseded for delivery |

- `workshop.md` · `prompts.md` · `diagrams/` (6)
- `artifacts/connector-mission.html` + `.spec.md` (Export PDF)
- `data/gen_m3_data.py` (seed 303) → `data/pack/outlook/` (20 emails + index), `data/pack/sharepoint/` (Project Tracker, Issue Log, Shared Capex Tracker) · `data/IT_SETUP.md` (test tenant checklist + fallback)

## Build notes
- The M3 Orca worker built slides, prompts, diagrams and data, then was cut off twice by API connection loss. The orchestrator wrote `workshop.md`, the Connector Mission Artifact + spec, `IT_SETUP.md`, `SOURCES.md` and this README, and replaced the slide-7 story (the Replit case duplicated M2) with the PHE Excel case.

## Open questions for Prem
1. Can IT provide a test tenant (test accounts, `M3-Training` site, test mailbox) — or do we plan for route B (local Sample Pack + Cowork) for everyone?
2. Are M365 **write tools** enabled in Banpu's Claude org? The course assumes read-only; please confirm so slide 5 is accurate.
3. The connector's tenant-wide search means learners' real accounts would see real content — confirm the workshop must use test accounts only (recommended).
