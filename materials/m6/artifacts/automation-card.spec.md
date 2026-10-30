# Spec · Automation Card (Artifact)

File: `automation-card.html` · Owner: M6 · Used in: slide 14 (workshop brief), slide 13 (quick quiz), workshop pages 1–4

## Purpose
Help each learner design **one** Scheduled task safely before touching Claude: fill 6 slots (⏰ เมื่อไร · 🟩 Input · 🟦 Process · 🟦 Output · 🟧 Checkpoint · 🟧 Owner), get a copy-ready task prompt, and leave with a PDF that names the owner and the human checkpoints. Covers requirement 5 (HITL), 6 (Document Factory → Schedule/Distribution) and 10 (monitoring task template).

## Users
Learners on laptops, solo, during the 20-minute workshop (opened on page 1, revisited on pages 3–4). Trainer can project the Quiz tab during slide 13.

## Interactions
1. **Tab 1 · การ์ด 6 ช่อง**
   - 3 template buttons prefill the card: (ก) Weekly project status (M6-P03), (ข) Weekly Energy & Ops Insight (M6-P04), (ค) own task (M6-P05, 🟢 data only).
   - Route switch: A = Connector (SharePoint/Outlook test tenant, runs in the cloud) · B = local folder `Documents/Claude-Workshop/M6/` (computer on + not asleep + Claude Desktop open).
   - Input/Output chips, checkpoint checklist, approval mode buttons (Manual / Auto / Skip), owner + backup + review deadline.
   - Live readiness meter "x/6" and badge **พร้อมตั้งเวลา** when all 6 slots pass; per-slot ✓ marks.
   - Warnings (rules from slides 8–9): 🔴 Skip selected, auto-send, overwriting the source (copy-before-write), sharing outside without approval, 🔴 data (salary/personal); ⚠ Auto selected (use Manual until 4 clean runs), hourly cadence (usage), Outlook Drafts needs route A, no internal names in web search terms, date in output file name, Owner must be 1 person + backup.
   - Generated task prompt (draft-and-wait wording, "🛑 หยุดรอคนตรวจ") with **Copy prompt** button.
2. **Tab 2 · Quiz ตั้งเวลาได้ไหม?** The 4 scenarios A–D from slide 13; learner picks 🟢 / 🟡 / 🔴 and sees the explanation.
3. **Tab 3 · รอบทดสอบ + ตัดสินใจ** Test-run checklist (nothing sent, `input/` unchanged, draft header, 3 numbers checked), decision Pause vs. keep for a 4-week trial, and the "before lowering approval" gate.
4. **↺ เริ่มใหม่** clears saved state.

## Export PDF
Header button from `materials/_shared/export-pdf.html` (`window.print()`). Print CSS hides tabs/buttons/toasts, shows all three panels one after another (Quiz on a new page), expands the generated prompt, keeps slots unbroken. Verified with headless Chrome print-to-PDF.

## Data
Templates, quiz items and rules live in JS objects in the HTML. Example people (คุณวิไลวรรณ etc.) and projects (PRJ-101, PRJ-105) are fictional and match the M3/M6 synthetic data. No Banpu data.

## Storage
`localStorage` (per viewer, wrapped in try/catch) only so a learner does not lose the card when switching tabs or reloading; the page works fully without it.

## Engagement mechanic
Progress meter + "พร้อมตั้งเวลา" badge, instant rule warnings (traffic-light colours), 4-question quiz, and a take-home PDF that becomes half of the M7 Capstone canvas.

## Constraints
Self-contained (Google Fonts only), no network/AI calls (no Team plan usage), STYLE.md colours (human `#E4572E`, AI `#2E86AB`, data `#3BA55C`, warning `#F2A541`), responsive single column on phones.
