# M1 · Claude Foundation & Security First (บังคับ)

09:15–10:15 · 60 นาที · Lecture 40 / Workshop 20 · Requirements 2, 8, 9, 13

ผู้เรียนเข้าใจว่า Claude / Cowork ทำงานแบบ Agent (คิด → วางแผน → ลงมือ) เลือก Chat · Project · Skill · Agent (Cowork) · Artifact ได้ถูกงาน เห็นความต่าง Chat vs Cowork จาก Demo รู้ข้อจำกัดของ Team plan และวินัยด้านข้อมูล (Data Traffic Light) ก่อนลงมือกับไฟล์จริงใน M2–M7

## Page counts

| Item | Budget | Actual |
|---|---|---|
| Slides (`python3 tools/build_slides.py materials/m1/slides.md --count`) | 40 (±10% → 36–44) | **41** (7 section/story + 34 content; speaker notes on every slide) |
| Workshop pages (`## ` in `workshop.md`) | 4 | **4** |

## Timing (minute by minute)

| เวลา | นาที | สไลด์ | กิจกรรม | ประเภท |
|---|---|---|---|---|
| 09:15–09:17 | 2 | 1–2 | เปิดโมดูล · เป้าหมาย 60 นาที | Lecture |
| 09:17–09:18 | 1 | 3 | Story: แชต ChatGPT ที่แชร์ไว้โผล่ใน Google, ก.ค. 2025 (ข้อมูลรั่วจากความหวังดี) | Lecture · Story |
| 09:18–09:23 | 5 | 4–9 | Claude / Cowork · Chatbot vs Agent · Agent loop · Plan → Approve → Execute | Lecture |
| 09:23–09:32 | 9 | 10–18 | Chat / Project / Skill / Agent / Artifact · decision tree · quick quiz | Lecture + interaction |
| 09:32–09:40 | 8 | 19–23 | Demo Chat vs Cowork (Excel → HTML dashboard) · debrief | Demo |
| 09:40–09:50 | 10 | 24–33 | Personal/Team/Enterprise · Team governance limits · นโยบายบ้านปู · ข้อมูลอ่อนไหว · Data Traffic Light · anonymize · third-party Skill + Cato case | Lecture · Story |
| 09:50–09:55 | 5 | 34–37 | เลือก model · weekly usage limit · 5 นิสัยประหยัด usage | Lecture |
| 09:55–09:57 | 2 | 38–39 | Workshop: บรีฟกติกา (workshop หน้า 1) | Workshop |
| 09:57–10:05 | 8 | — | รอบ 1: เกม 15 ใบใน Artifact (หน้า 2) | Workshop · Hands-on |
| 10:05–10:10 | 5 | — | รอบ 2: anonymize ไพ่เหลืองด้วย Claude + คนตรวจ (หน้า 3) | Workshop · Hands-on |
| 10:10–10:15 | 5 | 40–41 | Debrief · กฎ 3 ข้อของฉัน · Export PDF · สรุป → M2 (หน้า 4) | Workshop |

Lecture 40 นาที (รวม Demo 8) · Workshop 20 นาที

## Requirement coverage

| Req | หัวข้อ | อยู่ที่ไหน | ระดับ |
|---|---|---|---|
| 2 | Security & Sensitive Data; Personal vs Team vs Enterprise; Team governance/audit limits; ห้าม Personal AI | สไลด์ 3, 24–30 · workshop หน้า 1–4 · Artifact Data Traffic Light | **Hands-on** |
| 8 | Chat vs Skill vs Project vs Agent vs Artifact | สไลด์ 5–18 (decision tree + quiz) · Demo สไลด์ 19–23 · prompt M1-P01–P03 | **Demo + Lecture** (Hands-on เต็มใน M5) |
| 9 | Third-party Skill Security | สไลด์ 14, 31–33 (Cato case) · diagram third-party-skill-check | **Awareness** (แนะนำแนวคิด; Hands-on ใน M5) |
| 13 | Cost / usage efficiency, model choice, weekly limit | สไลด์ 35–37 · prompt M1-P06 | **Awareness** (แนะนำแนวคิด; Hands-on ใน M8) |

## Files

| Path | What |
|---|---|
| **Slides Artifact** · https://claude.ai/artifact/B5QugBgGE4eWMe69TrCvbv | **Delivery deck.** 41 slides built on Claude's core Slides Artifact type; speaker notes on every slide; Present mode; download as PDF/PPTX from Share › Export. All 7 diagrams redrawn natively (boxes + connectors) in the 3 STYLE colours with legend. Private until shared from the page's Share menu |
| `deck/project/deck.json` + `deck/project/slides/s01–s41.html` | Source files of the Slides Artifact (republish with the Artifact tool, `root: materials/m1/deck`) |
| `slides.md` → `slides.html` | Content source the Artifact was built from (same 41 slides and notes); superseded for delivery |
| `workshop.md` | Workshop guide, 4 A4 pages |
| `prompts.md` | M1-P01 … M1-P06 (copy-ready) |
| `diagrams/*.mmd` | agent-loop · tool-decision-tree · demo-chat-vs-cowork · data-traffic-light · third-party-skill-check · model-usage-choice · workshop-flow (all embedded in slides; workshop-flow also in workshop.md) |
| `artifacts/data-traffic-light.html` + `.spec.md` | Data Traffic Light game (15 cards, streak/badge, rules box, Export PDF). Reused by M8 |
| `data/traffic_light_cards.json` | Canonical card deck (edit here) |
| `data/sync_cards.py` | Writes the JSON into the Artifact; supports other JSON/HTML paths for M8 |
| `data/gen_site_ops.py` → `data/site_ops_sample.xlsx` | Synthetic Excel for the demo (6 fictional sites × 21 months, 13 KB, committed) |
| `SOURCES.md` | 7 link-only sources (2 stories/cases) |

Regenerate: `python3 materials/m1/data/gen_site_ops.py` · `python3 materials/m1/data/sync_cards.py` · `python3 tools/build_slides.py materials/m1/slides.md`

## Stories / cases
1. Shared ChatGPT chats in Google, Jul–Aug 2025: users ticked "Make this chat discoverable" when sharing; Fast Company found ~4,500 indexed chats, some with names and confidential work content; OpenAI removed the feature (slide 3; SOURCES #1–2). Replaced the earlier 2023 opening case on Prem's request (31 Oct 2026).
2. Cato Networks, Dec 2025: a modified open-source Skill silently downloaded and ran ransomware in a test environment (slide 33; SOURCES #3–5).

## Trainer prep
- Copy `data/site_ops_sample.xlsx` into a clean `demo/M1` folder; run M1-P01 and M1-P02 once in the dry-run and keep the outputs as a fallback.
- Share the Artifact link (company Claude account) or the HTML file before 09:55.
- Open Settings → Usage in a tab to show usage after the demo.

## Open questions for Prem
1. **Sensitive-data tool name:** what exactly is "เครื่องมือที่บริษัทกำหนดสำหรับข้อมูลอ่อนไหว" at Banpu? Slide 27 says it generically; name it if Hi-I approves.
2. **Classification defaults:** do Hi-I/IT agree with the 15 card answers (esp. C10 sales volume + customer names = 🟡, C05 published report = 🟢)? Does Banpu have an official data classification (e.g. Public/Internal/Confidential/Restricted) we should map 🟢🟡🔴 to?
3. **Team plan facts:** slide 25 says Team has limited audit log / no Compliance API vs Enterprise, based on public pages as of 30 Oct 2026. Please re-check claude.com/pricing and the help center the week of training, and confirm whether Banpu's admin has enabled usage credits and which seat type (Standard/Premium) learners have.
4. **Model names:** slides use family names (Haiku / Sonnet / Opus). Confirm what the model menu shows on Banpu's Team account during the dry-run and whether any model is restricted.
5. **Images:** M1 currently uses no photos/illustrations (diagrams + tables only). Want up to 2 flat-editorial illustrations (e.g. traffic-light hero for slide 29, "Agent as assistant" for slide 6)?
6. **Demo safety:** the Chat demo uploads the synthetic Excel; OK to show this live on Banpu's tenant, or should the trainer use a dedicated demo account?
