# M6 · Automation

14:10–14:45 · 35 นาที (Lecture 15 · Workshop 20) · Requirements 5, 6, 10, 15, 16

## Page counts (budget)
| Item | Built | Budget |
|---|---|---|
| Lecture slides (`slides.md`) | 15 | 15 (1 slide/min) |
| Workshop pages (`workshop.md`, `## ` sections) | 4 | 4 (1 page/5 min) |
| Prompts (`prompts.md`) | 7 (M6-P01…P07) | — |
| Diagrams (`diagrams/*.mmd`) | 8 | every workflow |
| Artifacts | 1 Automation Card (+ spec) | — |

## Timing
| Time | Min | Block | Material |
|---|---|---|---|
| 14:10–14:12 | 2 | เปิดโมดูล · Story: Air Canada chatbot (ข้อความอัตโนมัติถึงคนนอก = คำพูดของบริษัท) | slides 1–2 |
| 14:12–14:14 | 2 | Scheduled task ใน Cowork · เงื่อนไขการรัน (local vs remote) | slides 3–4 |
| 14:14–14:17 | 3 | Document Factory → Schedule/Distribution · Monitoring: Web + Email + Meeting → Insight | slides 5–6 |
| 14:17–14:19 | 2 | HITL 4 กฎ · เขียน task ให้ปลอดภัย 6 ช่อง | slides 7–8 |
| 14:19–14:22 | 3 | Demo: Weekly Energy & Ops Insight → ร่างที่หยุดรอคน | slides 9–10 |
| 14:22–14:24 | 2 | Awareness: dashboard refresh · sub-agent / multi-agent | slides 11–12 |
| 14:24–14:25 | 1 | Quick quiz · เข้า workshop · สรุป 5 กฎ | slides 13–15 |
| 14:25–14:45 | 20 | Workshop: Automation Card → สร้าง task แบบ Manual → Run now 1 รอบ + ตรวจร่าง → เก็บไว้หรือ Pause | workshop p1–4, Automation Card |

## Requirement coverage
| Req | Where | Depth |
|---|---|---|
| 5 Human-in-the-Loop | HITL 4 กฎ, approval mode = Manual, "🛑 หยุดรอคนตรวจ" in every task prompt, workshop p3 check of the draft | Hands-on |
| 6 Document Factory → Schedule/Distribution | slide 5 + workshop task (ก) weekly project status (reuses M3/M4 outputs) | Demo + Hands-on |
| 10 Automatic Monitoring (Web + Email + Meeting → Weekly Insight) | slides 6, 9–10 demo; workshop task (ข) | Demo + Hands-on |
| 15 Dashboard refresh (real-time vs scheduled) | slide 11 | Awareness |
| 16 Sub-agent / Multi-agent | slide 12 (Anthropic multi-agent research case) | Awareness only |

## Files

| Path | What |
|---|---|
| **Slides Artifact** · https://claude.ai/artifact/77u51h2Mek9CgrSedciouK | **Delivery deck.** 15 slides built on Claude's core Slides Artifact type; speaker notes on every slide; Present mode; download as PDF/PPTX from Share › Export. All 7 diagrams redrawn natively (boxes + connectors) in the 3 STYLE colours with legend. Private until shared from the page's Share menu |
| `deck/project/deck.json` + `deck/project/slides/s01–s15.html` | Source files of the Slides Artifact (republish with the Artifact tool, `root: materials/m6/deck`) |
| `slides.md` → `slides.html` | Content source the Artifact was built from (same 15 slides and notes, minute marks); superseded for delivery |
| `workshop.md` | Workshop guide, 4 pages |
| `prompts.md` | M6-P01 … M6-P07 (copy-ready) |
| `diagrams/` (8) | Mermaid sources of the workflow diagrams |
| `artifacts/automation-card.html` + `.spec.md` | 6-slot task designer (เมื่อไร · Input · Process · Output · Checkpoint · Owner), safety warnings, copy-ready task prompt, quiz, test-run checklist, Export PDF |
| `data/gen_m6_data.py` → `data/pack/` · `data/build_m6_pack.py` → `data/out/M6_pack(.zip)` | Synthetic meeting notes, watchlist, fictional news fallback; pack is gitignored and reuses M3 emails + SharePoint CSVs read-only |

## Claude Artifacts (claude.ai)

All private until shared from each page's Share menu. Published 31 Oct 2026 with `capabilities: {downloads: true}`.

| Artifact | File | claude.ai URL | Export PDF |
|---|---|---|---|
| M6 Slides (15 slides) | `deck/project/` | https://claude.ai/artifact/77u51h2Mek9CgrSedciouK | ✅ (Share › Export, PDF/PPTX) |
| M6 Workshop (ใบงาน 4 หน้า) | `artifacts/workshop-sheet.html` | https://claude.ai/artifact/WpGFhe1gXGwqSYhLeteZYo | ✅ |
| Automation Card (การ์ด 6 ช่อง + Quiz + รอบทดสอบ) | `artifacts/automation-card.html` | https://claude.ai/artifact/HFdt3zwrfBgErGfv6q5TUk | ✅ |

## Build notes
- Built by the M6 Orca worker over three attempts; each was cut off by API connection loss. The orchestrator wrote this README and `SOURCES.md`, and replaced the story slide (the Replit case was already used in M2) with the Air Canada chatbot case.

## Open questions for Prem
1. **Run conditions changed recently:** Anthropic Help Center pages disagree on whether scheduled tasks run remotely when the laptop is asleep/closed or only locally. Re-check SOURCES #1/#4 the week of training and confirm in the dry-run on Banpu's Team account.
2. Approval-mode default: confirm whether Banpu's admins can (and will) disable "Automatically approve" and require approval for write-capable connectors.
3. Route A needs the M3 test tenant (Outlook Drafts); otherwise everyone uses route B (local `M6_pack`).
4. Scheduled tasks consume Team-plan usage on every run — agree a guideline (e.g. weekly, not hourly) with Hi-I.
