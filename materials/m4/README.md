# M4 · Document Factory & Artifact as Output Layer

13:00–13:40 · 40 นาที · Lecture 15 / Workshop 25 · Requirements 1, 4, 6, 7, 11

ผู้เรียนเห็นสายพาน **Document Factory: Multiple Sources → Process → Report → (Schedule/Distribution ใน M6)** แล้วสร้าง **Monthly Operations Report ก.ย. 2569** จาก 5 แหล่ง (Excel · CSV ~172,000 แถว · SharePoint List · Outlook · ราคาพลังงานสาธารณะ) ออกมาเป็น Word/PPTX **และ** Artifact Dashboard พร้อม iterate v1 → v2 แล้วแก้ปัญหารายงานจริงขนาด ~37 MB ที่แนบอีเมลไม่ได้

## Page counts

| Item | Budget | Actual |
|---|---|---|
| Slides (`python3 tools/build_slides.py materials/m4/slides.md --count`) | 15 (±10% → 14–16) | **15** (2 section/story + 13 content; speaker notes with minute marks on every slide) |
| Workshop pages (`## ` in `workshop.md`) | 5 | **5** |

## Timing (minute by minute)

| เวลา | นาที | สไลด์ / หน้า | กิจกรรม | ประเภท |
|---|---|---|---|---|
| 13:00–13:01 | 1 | 1–2 | เปิดโมดูล · ถามห้องว่าทำรายงานเดือนละกี่ชั่วโมง · เป้าหมาย 40 นาที | Lecture |
| 13:01–13:02 | 1 | 3 | Story: Deloitte Australia 2025 (รายงาน A$440k มีอ้างอิงปลอม) | Lecture · Story |
| 13:02–13:06 | 4 | 4–6 | Document Factory diagram · 5 แหล่ง + กับดัก · Input → Process → Output + กติกาตรวจ 3 ตัวเลข | Lecture |
| 13:06–13:11 | 5 | 7–11 | Artifact = output layer (Dashboard/App/Prototype/Diagram) · Demo Monthly Ops Dashboard (v1 ↔ v2) · iterate · เมื่อไรใช้ Word/Excel/PDF/PPT · quick quiz (Output Picker) | Lecture + Demo |
| 13:11–13:14 | 3 | 12–13 | ข้อจำกัดจริง: รายงานใหญ่เกินแนบ/อัปโหลด · 3 workaround | Lecture + Demo (ไฟล์ 37 MB) |
| 13:14–13:15 | 1 | 14 | บรีฟ workshop | Lecture |
| 13:15–13:18 | 3 | หน้า 1 | เตรียมโฟลเดอร์ + ตรวจ 5 แหล่ง (M4-P01) | Workshop · Hands-on |
| 13:18–13:25 | 7 | หน้า 2 | Plan → รวม 5 แหล่ง → ตรวจ 3 ตัวเลข (M4-P02–P04) | Workshop · Hands-on |
| 13:25–13:30 | 5 | หน้า 3 | Report → Word หรือ PPTX (M4-P05) | Workshop · Hands-on |
| 13:30–13:36 | 6 | หน้า 4 | Report → Artifact Dashboard v1 → v2 (M4-P06–P07) | Workshop · Hands-on |
| 13:36–13:40 | 4 | หน้า 5 · สไลด์ 15 | ไฟล์ใหญ่: ย่อรูป/แบ่งไฟล์/สรุป + ลิงก์ SharePoint (M4-P08) · Output Picker · สรุป 5 กฎ → M5/M6 | Workshop · Hands-on |

Lecture 15 นาที (รวม Demo ~3) · Workshop 25 นาที · ถ้าช้า: ข้ามหน้า 3 ไปทำใน M6 (เขียนไว้ใน workshop.md)

## Requirement coverage

| Req | หัวข้อ | อยู่ที่ไหน | ระดับ |
|---|---|---|---|
| 1 | M365 / Power Platform First | แหล่ง 3–4 = SharePoint List + Outlook (Connector จาก M3) · output Word/PPTX · workaround สรุป + ลิงก์ SharePoint · สไลด์ 5, 13 · workshop หน้า 1–3, 5 | **Hands-on** |
| 4 | Multiple Sources + Multiple Formats (ภายใน + ภายนอก) | Excel + CSV + SharePoint List + Email + CSV สาธารณะ → รายงานเดียว · สไลด์ 4–6 · workshop หน้า 1–2 · M4-P01–P04 | **Hands-on** |
| 6 | Real-world Document Factory | diagram document-factory (สไลด์ 4) · workshop ทั้งหมด · Dashboard Artifact ใช้เป็น Demo · ส่งต่อ Schedule/Distribution ใน M6 | **Hands-on + Demo** |
| 7 | ข้อจำกัดและ workaround ด้วยข้อมูลขนาดจริง | CSV ~172,000 แถว (สคริปต์สรุป) · `Monthly_Ops_Report_2569-09_FULL.docx` ~37 MB → ~6.4 MB หลังย่อรูป · สไลด์ 12–13 · workshop หน้า 5 · M4-P08 | **Hands-on + Demo** |
| 11 | Artifact as Output Layer, iterate หลายเวอร์ชัน, เมื่อไรใช้ Word/Excel/PDF/PPT | สไลด์ 7–11 · workshop หน้า 4 · Artifacts: Monthly Ops Dashboard (v1/v2 toggle), Output Picker | **Hands-on** |

## Files

| Path | What |
|---|---|
| **Slides Artifact** · https://claude.ai/artifact/KgQ57jcEaEb58SShmpLqkr | **Delivery deck.** 15 slides built on Claude's core Slides Artifact type; speaker notes on every slide; Present mode; download as PDF/PPTX from Share › Export. All 5 Mermaid diagrams redrawn natively (boxes + connectors) in the 3 STYLE colours with legend. Private until shared from the page's Share menu |
| `deck/project/deck.json` + `deck/project/slides/s01–s15.html` | Source files of the Slides Artifact (republish with the Artifact tool, `root: materials/m4/deck`) |
| `slides.md` → `slides.html` | Content source the Artifact was built from (same 15 slides and notes); superseded for delivery |
| `workshop.md` | Workshop guide, 5 A4 pages (goal · prompt ID · ✅ checkpoint · time per step) |
| `prompts.md` | M4-P01 … M4-P08 (copy-ready) |
| `diagrams/*.mmd` | document-factory · artifact-iterate · format-decision · too-big-workaround · workshop-flow (all embedded in slides) · office-report (workshop หน้า 3) |
| `artifacts/monthly-ops-dashboard.html` + `.spec.md` | Sample Monthly Ops Dashboard: KPI, 6 site cards (traffic light), detail panel with bar chart, energy sparklines, projects, HITL 3-number checklist + badge, v1/v2 toggle, Export PDF (4 A4 pages) |
| `artifacts/output-picker.html` + `.spec.md` | Quiz game: 8 "which format?" + 2 "too big" scenarios, streak, badge, result table, Export PDF |
| `data/gen_m4_data.py` | Makes `ops_monthly_2566-2569.xlsx` (M2 history + new Jan–Sep 2569, 270 rows, committed), `out/shift_log_2568-2569.csv` (172,260 rows, 11 MB), `out/Monthly_Ops_Report_2569-09_FULL.docx` (~37 MB), `dashboard_data.json` |
| `data/fetch_energy_prices.py` → `energy_prices_public_2023-2026.csv`, `raw/` | Real public prices (IMF via FRED): coal AU, Brent, LNG Asia, Jan 2023–Sep 2026 (`--offline` rebuilds from `raw/`) |
| `data/sync_dashboard.py` | Writes `dashboard_data.json` + causes into the dashboard HTML |
| `data/build_m4_pack.py` | Assembles the learner pack `data/out/M4_pack/input/` (27 files, ~49 MB) incl. M3 SharePoint CSV/.eml fallbacks (read-only copy) |
| `data/answer_key.md` | Trainer answers: per-site numbers, shift log, projects, prices, file-size results |
| `data/.gitignore` | `out/` (large generated files) |
| `SOURCES.md` | 8 entries (1 story, 1 public dataset, docs), all link-only |

Regenerate:
```bash
python3 materials/m4/data/fetch_energy_prices.py        # week of training (network)
python3 materials/m4/data/gen_m4_data.py                # ~20 s
python3 materials/m4/data/sync_dashboard.py
python3 materials/m4/data/build_m4_pack.py              # then upload out/M4_pack to the training SharePoint site
python3 tools/build_slides.py materials/m4/slides.md
```
Reused read-only: `m2/data/core/ops_monthly_clean.csv` (history), `m3/data/pack/sharepoint/*.csv`, `m3/data/pack/outlook/*.eml`.

## Stories / cases
1. Deloitte Australia, Jul–Oct 2025: a A$440,000 government report contained ~20 fabricated references and an invented court quote; revised version disclosed generative-AI use; Deloitte refunded the final instalment (slide 3; SOURCES #1). Used to motivate the two human checkpoints in the Document Factory.
2. Real public data as the external source: IMF commodity prices via FRED (SOURCES #2): coal +9.5 %, Brent +15.8 %, LNG +20.9 % m/m in Sep 2026.

## Open questions for Prem
1. **Outlook attachment limit at Banpu**: slide 12 says "20–35 MB, ask IT". Could คุณเก๊ confirm the tenant's real limit so we can state one number?
2. **External data choice**: IMF/FRED global prices (English, clean licence). Would you prefer a Thai source (e.g. EPPO energy price statistics) instead or as well? We'd need to check its reuse terms.
3. **Report month = ก.ย. 2569** because public data currently ends Sep 2026. If the course runs later, re-run `fetch_energy_prices.py` and shift the month (generator constants + answer key)?
4. **M4 pack delivery**: ~49 MB (includes the 37 MB file on purpose). Who uploads it to the training SharePoint site, and can learners download that size quickly in the room?
5. **Team-tenant settings to verify in dry-run**: file creation (docx/pptx) enabled, Artifact sharing inside the org enabled, SharePoint/Outlook Connectors approved. The workshop has local CSV/.eml fallbacks if Connectors are off.
6. **Story naming a real firm (Deloitte)**: OK for a Banpu audience, or swap for an anonymised version?
7. No images in `img/` and no Codex illustrations yet. Diagrams and the two Artifacts carry the visuals. Should I add 1–2 flat illustrations (e.g. "document factory" hero for slide 1/4)?
