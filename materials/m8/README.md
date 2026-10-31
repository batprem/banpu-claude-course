# M8 · Security Recap, Quiz & แผน 30 วัน

16:15–17:00 · 45 นาที (Lecture 20 · Workshop 25) · Requirements 2, 3, 9, 13

## Page counts (budget)
| Item | Built | Budget |
|---|---|---|
| Lecture slides (`slides.md`) | 20 | 20 (1 slide/min) |
| Workshop pages (`workshop.md`, `## ` sections) | 5 | 5 (1 page/5 min) |
| Prompts (`prompts.md`) | 7 (M8-P01…P07) | — |
| Diagrams (`diagrams/*.mmd`) | 9 | every workflow |
| Artifacts | 2: Security & Usage Quiz · แผน 30 วัน (+ specs) | — |

## Timing
| Time | Min | Block | Material |
|---|---|---|---|
| 16:15–16:18 | 3 | เปิด · Story: Microsoft AI research 38TB shared link (Wiz, 2023) | slides 1–3 |
| 16:18–16:27 | 9 | 6 กฎที่พกกลับบ้าน · สิ่งที่ไม่ให้ Claude ทำ · 4 คำถามก่อนกด Allow/Approve | slides 4–11 |
| 16:27–16:31 | 4 | ใช้ให้คุ้มภายใต้ weekly limit · 3 เทคนิค · ตัวอย่างรายงานรายเดือน · เข้า workshop | slides 12–17 |
| 16:31–16:36 | 5 | ภารกิจ 1 · ใช้ให้คุ้ม (M8-P01/P02) | workshop p1 |
| 16:36–16:48 | 12 | ภารกิจ 2 · Quiz 18 ข้อ + รอบสุดท้าย Traffic Light 6 ใบ + Export PDF | workshop p2–3, security-quiz |
| 16:48–16:56 | 8 | ภารกิจ 3 · แผน 30 วัน + Export PDF | workshop p4, plan-30-days |
| 16:56–17:00 | 4 | Debrief Quiz · ถาม-ตอบ + แบบประเมิน · พรุ่งนี้เริ่มอะไร | slides 18–20 · workshop p5 (หลังอบรม) |

## Requirement coverage
| Req | Where | Depth |
|---|---|---|
| 2 Security & sensitive data; Personal vs Team; no Personal AI | rules 1–2, story, quiz categories ข้อมูลอ่อนไหว + บัญชี & การแชร์, Traffic Light final round | Hands-on |
| 3 Approved connectors, copy-before-write | rules 3–4, quiz category Connector | Hands-on |
| 9 Third-party Skill security | rule 5, quiz category Skill จากภายนอก | Hands-on (recap) |
| 13 Usage efficiency / model choice | slides 12–15, mission 1 (M8-P01/P02), quiz category ใช้ให้คุ้ม | Hands-on (light) |

## Files

| Path | What |
|---|---|
| **Slides Artifact** · https://claude.ai/artifact/Uix5PCdLVDFT2EpceDUi1Q | **Delivery deck.** 20 slides built on Claude's core Slides Artifact type; speaker notes on every slide; Present mode; download as PDF/PPTX from Share › Export. All 9 diagrams redrawn natively (boxes + connectors) in the 3 STYLE colours with legend. Private until shared from the page's Share menu |
| `deck/project/deck.json` + `deck/project/slides/s01–s20.html` | Source files of the Slides Artifact (republish with the Artifact tool, `root: materials/m8/deck`) |
| `slides.md` → `slides.html` | Content source the Artifact was built from (same 20 slides and notes); superseded for delivery |
| `workshop.md` | Workshop guide, 5 pages |
| `prompts.md` | M8-P01 … M8-P07 (copy-ready) |
| `diagrams/*.mmd` | 9 Mermaid diagrams (all embedded in slides) |
| `artifacts/security-quiz.html` + spec | 18 questions in 6 categories + final round of 6 M1 cards, per-category score, explanations, Export PDF. Data in `data/quiz_questions.json`; run `python3 materials/m8/data/sync_quiz.py` after editing (re-embeds questions + M1 cards read-only, regenerates `trainer/answer-key.md`) |
| `artifacts/plan-30-days.html` + spec | 30-day adoption plan with readiness meter, hours-saved counter, safety warnings, Export PDF |
| `trainer/answer-key.md` | Answers + reasons for the quiz and final round |

## Build notes
- Built by the M8 Orca worker over two attempts; both were cut off by API connection loss. The orchestrator finished the 30-day plan Artifact script, its spec, `workshop.md`, `SOURCES.md` and this README.

## Open questions for Prem
1. Name of Banpu's approved tool for sensitive data, so rule 1 and quiz Q01 can name it instead of "เครื่องมือที่บริษัทกำหนด" (same as M1 Q1).
2. Course evaluation form (slide 19): does Hi-I have its own form/link, or should we provide one?
3. Should the quiz score be collected (e.g. a shared Artifact or Microsoft Forms) for Hi-I reporting? Currently scores stay on each learner's machine by design.
4. Who receives the 30-day plans (buddy only, manager, or Hi-I)? This affects the guidance on where to store the PDF.
