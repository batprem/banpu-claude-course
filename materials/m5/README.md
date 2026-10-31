# M5 · Skills & Plugins

13:40–14:10 · 30 นาที · Lecture 10 / Workshop 20 · Requirements 8, 9, 13

ผู้เรียนเข้าใจว่า Skill ต่างจาก Prompt · Project · Connector · Plugin อย่างไร ติดตั้งและทดสอบ Skill "รายงานมาตรฐานบ้านปู" (ฉบับฝึกอบรม) กับข้อมูลชุดใหม่ รู้ขั้นตอนแชร์ Skill ในทีมผ่านการตรวจของทีม Hi-I / IT และฝึกตรวจ Skill จากภายนอกด้วย Checklist 6 ข้อ จนได้ PDF ผลตรวจกลับไป

## Page counts

| Item | Budget | Actual |
|---|---|---|
| Slides (`python3 tools/build_slides.py materials/m5/slides.md --count`) | 10 (±10% → 9–11) | **10** (1 section + 1 story + 8 content; speaker notes on every slide) |
| Workshop pages (`## ` in `workshop.md`) | 4 | **4** (each checked to fit one A4 page in a print render) |

## Timing (minute by minute)

| เวลา | นาที | สไลด์ / หน้า | กิจกรรม | ประเภท |
|---|---|---|---|---|
| 13:40–13:40:30 | 0.5 | 1 | เปิดโมดูล · ผลลัพธ์ที่ได้กลับไป | Lecture |
| 13:40:30–13:42 | 1.5 | 2 | Story: ClawHavoc, Skill ปลอม 341 ตัว (ก.พ. 2026) | Lecture · Story |
| 13:42–13:43:30 | 1.5 | 3 | Skill คืออะไร: โฟลเดอร์ + SKILL.md (เปิดของจริงให้ดู) | Lecture · Demo |
| 13:43:30–13:45 | 1.5 | 4 | Prompt · Project · Skill · Connector · Plugin | Lecture |
| 13:45–13:46 | 1 | 5 | Diagram ทำงานร่วมกันอย่างไร · "งานซ้ำของคุณคืออะไร" | Lecture + interaction |
| 13:46–13:47 | 1 | 6 | Skill ประหยัด usage อย่างไร (progressive disclosure) | Lecture |
| 13:47–13:48 | 1 | 7 | แชร์ Skill ในทีม (ผ่าน Hi-I / IT, เก็บใน SharePoint) | Lecture |
| 13:48–13:49 | 1 | 8 | Checklist 6 ข้อก่อนติดตั้ง Skill จากภายนอก | Lecture |
| 13:49–13:50 | 1 | 9 | บรีฟ Workshop · แจกไฟล์และลิงก์ Artifact | Workshop brief |
| 13:50–13:57 | 7 | หน้า 1 | ① อ่าน Skill ด้วย Claude แล้วติดตั้ง banpu-standard-report | Workshop · Hands-on |
| 13:57–14:02 | 5 | หน้า 2 | ② ทดสอบกับข้อมูลชุดใหม่ (โซลาร์ Site F) + ตรวจตัวเลข | Workshop · Hands-on |
| 14:02–14:08 | 6 | หน้า 3 | ③ ล่าธงแดง Skill ปลอม + Checklist + Export PDF | Workshop · Hands-on |
| 14:08–14:10 | 2 | หน้า 4 · สไลด์ 10 | ④ Debrief · Skill ตัวแรกของฉัน · bridge → M6 | Workshop |

Lecture 10 นาที (13:40–13:50) · Workshop 20 นาที (13:50–14:10)

## Requirement coverage

| Req | หัวข้อ | อยู่ที่ไหน | ระดับ |
|---|---|---|---|
| 8 | Chat vs Skill vs Project vs Agent vs Artifacts – ใช้เมื่อไร | สไลด์ 3–5 (ต่อจาก decision tree ของ M1 + Connector/Plugin) · workshop หน้า 1–2 (ติดตั้งและใช้ Skill จริง, ทางสำรองผ่าน Project) · prompt M5-P01–P04 | **Hands-on + Demo** |
| 9 | Third-party Skill Security | สไลด์ 2 (ClawHavoc case), 7–8 · workshop หน้า 3 · Artifact Skill Security Checklist (ล่าธงแดง 16 จุด + checklist 16 ข้อ + PDF) · Skill ปลอม `skill-audit-sample/` · prompt M5-P05 | **Hands-on** |
| 13 | Cost / usage efficiency | สไลด์ 6 (progressive disclosure, ลดการ paste ซ้ำ/รอบแก้) · workshop หน้า 2 (ทดสอบโดยไม่ต้องพิมพ์คำสั่งยาว) | **Hands-on (เบา)** |

## Files

| Path | What |
|---|---|
| **Slides Artifact** · https://claude.ai/artifact/PRZrJe9wv2nWeJSaTFy416 | **Delivery deck.** 10 slides built on Claude's core Slides Artifact type; speaker notes on every slide; Present mode; download as PDF/PPTX from Share › Export. All 5 diagrams redrawn natively (boxes + connectors) in the 3 STYLE colours with legend. Private until shared from the page's Share menu |
| `deck/project/deck.json` + `deck/project/slides/s01–s10.html` | Source files of the Slides Artifact (republish with the Artifact tool, `root: materials/m5/deck`) |
| `slides.md` → `slides.html` | Content source the Artifact was built from (same 10 slides and notes, minute marks); superseded for delivery |
| `workshop.md` | Workshop guide, 4 A4 pages |
| `prompts.md` | M5-P01 … M5-P06 (copy-ready) |
| `diagrams/*.mmd` | skill-vs-others · progressive-disclosure · skill-sharing-flow · third-party-audit · workshop-flow (all embedded in slides 5–9; workshop-flow also in workshop p.1) |
| `skill-example/banpu-standard-report/` | **Real example Skill**: `SKILL.md` + `templates/report-template.md` + `examples/example-report-site-b.md` (numbers match M2 answer key) |
| `skill-example/README.md` | How to zip, upload, share · `.gitignore` excludes the ZIP |
| `skill-audit-sample/` | **Fake risky third-party Skill** `quick-excel-summary-pro` (SKILL.md, `scripts/sync_helper.py.txt`, `reference/formatting-tips.md`) + `README-TRAINING.md`. Harmless: script is `.txt` and starts with `raise SystemExit`, URLs are example.com/.net, SKILL.md is deliberately not installable |
| `trainer/audit-answer-key.md` | Trainer-only answer key: 16 red flags + debrief points |
| `artifacts/skill-security-checklist.html` + `.spec.md` | Artifact: red-flag hunt game + 16-question checklist with score and 🟢🟡🔴 verdict + audit log + Export PDF |
| `data/audit_flags.json` | Canonical red-flag list (edit here) |
| `data/sync_audit_sample.py` | Embeds the fake Skill files + flags into the Artifact; fails if a flag no longer matches exactly one line |
| `SOURCES.md` | 12 link-only sources (1 case with 2 sources) |

Data reused read-only from M2: `materials/m2/data/workshop_b_scattered/solar_F_2023_2025.xlsx` (test dataset A), `materials/m2/data/core/ops_monthly_clean.csv` (dataset B), and the Site B 2567 figures in `materials/m2/data/answer_key/insights.md` (example report). M5 generates no new data files.

Regenerate: `python3 materials/m5/data/sync_audit_sample.py` · `python3 tools/build_slides.py materials/m5/slides.md` · ZIP: `cd materials/m5/skill-example && python3 -m zipfile -c banpu-standard-report.zip banpu-standard-report/`

## Stories / cases
1. ClawHavoc, Feb 2026: Koi Security audited 2,857 Skills on ClawHub (OpenClaw's public Skill registry) and found 341 malicious ones posing as popular tools; they told users to install a "prerequisite" that delivered an info-stealer (slide 2; SOURCES #1–2). It complements M1's Cato Networks proof-of-concept: M1 = "possible", M5 = "happened at scale".

## Trainer prep
- Build the ZIP and share it (plus the Artifact link) on the class SharePoint/Teams channel before 13:40.
- Dry-run on a Banpu Team account: upload the Skill, run M5-P03 with `solar_F_2023_2025.xlsx`, keep the output as a fallback screenshot; check that Claude shows it is using the Skill.
- Check that learners have Skills + Code execution enabled; if not, use the Project fallback on workshop p.4.
- Keep `trainer/audit-answer-key.md` open for the debrief. Do not distribute `trainer/` to learners.

## Open questions for Prem
1. **Skills enabled on Banpu's Team account?** Upload needs Skills + Code execution/file creation turned on by an Owner. If not enabled by training day, the workshop runs on the Project fallback (works, but loses the "Claude picks the Skill itself" moment).
2. **Who approves Skills?** Slides name "ทีม Hi-I / IT" as approver and Owner-provisioned org skills as the sharing path. Please confirm with คุณเก๊: approver role, whether peer sharing is enabled, and where approved Skills are stored (SharePoint site name?).
3. **"Banpu standard report" format:** the example Skill (6 sections, status thresholds ±3%/10%, Thai formal tone) is invented. Does Hi-I have a real report standard (headings, logo-free) we may mirror without real data? If yes, I will update SKILL.md and the template.
4. **Plugins:** slide 4 explains Plugins as a concept only (no hands-on). Are any Plugins allowed/installed on Banpu's Team account? Plugins with connectors other than SharePoint/Outlook are presented as out of scope.
5. **Checklist ownership:** the 6-category checklist (16 questions, 10 critical) is a teaching default. Should it be aligned to an existing Banpu IT software-approval checklist? M8 could reuse the Artifact for recap.
6. **Images:** M5 uses diagrams + code only. Want up to 2 flat-editorial illustrations (e.g. "Skill = recipe card" for slide 3, "inspector with magnifier" for slide 8)?
