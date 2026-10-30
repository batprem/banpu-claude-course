# M7 · Capstone: Use Case จริงของเรา

15:00–16:15 · 75 นาที (Lecture 10 / Workshop 65) · Requirement 14 (Hands-on) + ประยุกต์ 1–7 · Scope: `proposal/proposal.html` §M7

Learners form 5 teams (6–8 people), pick one of 5 synthetic use cases (standing in for the 3–5 use cases Hi-I will send) or bring their own with mock data, analyse it with the **Use-case Canvas: Data → Connector → Output → Trade-off (+ HITL)**, build a prototype with Cowork, then present for 3 minutes on the **Show & Share board** with trainer feedback and a class vote. The board's PDF (with each team's "next 30 days") feeds M8.

## Page counts (budget: 10 slides · 13 workshop pages)
| Item | Count | Check |
|---|---|---|
| Slides (`slides.md` → `slides.html`) | **10** (1 section, 1 story, 8 content; speaker notes on all) | `python3 tools/build_slides.py materials/m7/slides.md --count` |
| Workshop pages (`workshop.md`, `## ` sections) | **13** | `grep -c '^## ' materials/m7/workshop.md` |
| Prompts (`prompts.md`) | 10 (`M7-P01`…`P10`), reuses M2–M6 IDs by reference | |
| Diagrams (`diagrams/*.mmd`, all with human/ai/data classes, all parsed with Mermaid 10.9.1) | 9 | 5 embedded in slides, all 9 in workshop |
| Artifacts | 1: `show-share-board.html` + `.spec.md` (Export PDF tested in headless Chrome) | |

## Minute-by-minute
| Clock | Min | Segment | Material |
|---|---|---|---|
| 15:00–15:01 | 1 | Section: what we'll do in 65 min, count off into 5 teams | slide 1 |
| 15:01–15:02 | 1 | Story: Novo Nordisk (one use case, small team, human approval) | slide 2 |
| 15:02–15:03 | 1 | 65-minute flow + team roles | slide 3 |
| 15:03–15:05 | 2 | Use-case Canvas + Trade-off (security · limits · usage · HITL) | slides 4–5 |
| 15:05–15:07 | 2 | Menu of UC1–UC5 + BYO rules · worked example UC2 | slides 6–7 |
| 15:07–15:09 | 2 | Build recipe with Cowork · Show & Share format + rubric | slides 8–9 |
| 15:09–15:10 | 1 | 4 ground rules, start timer | slide 10 |
| 15:10–15:15 | 5 | ① Teams + roles + pick use case, download ZIP | workshop p.1–2 · `M7-P02` (BYO) |
| 15:15–15:20 | 5 | ② Canvas via Interview pattern | p.3 · `M7-P01` |
| 15:20–15:25 | 5 | ② Trade-off table + team diagram on the board | p.4 · board tab ① |
| 15:25–15:30 | 5 | ③ Copy folder, Restate + Plan → Approve | p.5 · `M7-P03` |
| 15:30–15:46 | 16 | ③ Execute per use case + HITL self-check | p.6 + p.7–11 · `M7-P04…P09` |
| 15:46–15:50 | 4 | ④ Card on the board + 3-minute script | p.12 · `M7-P10` |
| 15:50–16:10 | 20 | ⑤ Show & Share: 5 teams × (3 min + 1 min feedback) | p.13 · board tabs ②④⑤ |
| 16:10–16:15 | 5 | ⑥ Vote, winners, Export PDF → M8 | p.13 · board tab ③ |

## Requirement coverage
| Req | What | Where in M7 | Depth |
|---|---|---|---|
| 14 | Capstone from learners' own use case: data, connector, output, trade-off | Whole module: Canvas (slides 4–5, p.3–4), build (p.5–11), Show & Share board + rubric (p.12–13) | **Hands-on** |
| 1 | M365 first | All 5 use cases shaped as SharePoint library/List + Outlook data; connector choices on the board limited to M365 | Hands-on (apply) |
| 2 | Security & sensitive data | Data colour 🟢🟡🔴 on every card, 🛡️ trade-off, BYO only with mock data, rubric ③ | Hands-on (apply) |
| 3 | M365 connectors, copy-before-write | Copy folder before Cowork (p.5), drafts only / no write-back (UC2, UC4), route B via folder (`M3-P08`) | Hands-on (apply) |
| 4 | Multiple sources + formats → one output | UC1 docx+csv · UC2 csv+eml · UC3 xlsx+csv mixed units · UC4 md/txt/vtt+List export · UC5 csv+md | Hands-on |
| 5 | Human-in-the-Loop | Plan → Approve gate (`M7-P03`), HITL reviewer role, `M7-P09`, trainer answer keys with planted data traps | Hands-on |
| 6 | Document Factory | UC2/UC5 report pipelines; "เสร็จเร็ว" extensions to Scheduled task (M6) | Hands-on (light) |
| 7 | Limits & workarounds | ⚠️ trade-off on every card, "จุดที่ทีมมักติด" table (p.6); data pack is small by design (real-size data was M2–M4) | Awareness (apply) |

## Files
```
materials/m7/
  README.md · SOURCES.md
  slides.md · slides.html
  workshop.md (13 pages) · prompts.md (M7-P01…P10)
  diagrams/ capstone-flow · usecase-framework · build-loop · show-share · uc1-contract-summary · uc2-incident-weekly
            uc3-esg-consolidation · uc4-meeting-actions · uc5-energy-market-brief (.mmd)
  artifacts/ show-share-board.html · show-share-board.spec.md
  data/ gen_m7_data.py · uc1_contract_summary/ … uc5_energy_market_brief/ (each with BRIEF.md) · out/ (ZIPs, gitignored)
  img/ (empty: no external images used)
```
Regenerate the data pack + ZIPs: `python3 materials/m7/data/gen_m7_data.py` (needs `python-docx`, `openpyxl`). The `BRIEF.md` files are hand-written and are not overwritten by the generator. Trainer answer keys (counts, dates, traps) are in workshop pages 7–11 under 🔑 and match the committed data (seed 7).

## Open questions for Prem
1. **Real use cases from Hi-I:** the proposal says Hi-I sends 3–5 real use cases ≥ 1 week before training. UC1–UC5 are stand-ins. When they arrive, do we replace UC1–UC5 (same Canvas/board, new synthetic data per case) or keep UC1–UC5 and add theirs as BYO?
2. **Class size / team count:** timing assumes 30–40 learners → 5 teams × 4 min. With ~200+ users over several classes, please confirm per-class headcount; 6+ teams needs 2-minute pitches (fallback on p.13).
3. **Shared board:** the board uses copy/paste card codes so it works on any account offline. Do we want a version with live shared state (all teams post directly to one board), given it would require company Claude accounts and a shared Artifact?
4. **Distribution of ZIPs:** plan is a class SharePoint folder (USB as backup). Is there a training SharePoint site / Teams chat per class we can use?
5. **Test tenant:** if a test SharePoint site/mailbox exists (M3), should UC2/UC4 teams use the real Connector instead of the folder route?
6. **Prize / follow-up:** should the 🏆 winning use case go to Hi-I as a post-training pilot candidate (mentioned in trainer note p.13)?
