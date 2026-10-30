# Spec · M3 Connector Mission

- **Purpose:** turn the 30-minute M3 workshop into 6 stages that mirror `workshop.md` pages 1–6, so learners practise AI → Connect → Data → Execute, cross-source checking and copy-before-write with a human approval step.
- **Users:** learners (one per laptop, beside Claude Desktop); trainer projects it to pace the room.
- **Stages:** 1 เลือกเส้นทาง A (test tenant) / B (local `M3_SamplePack` + Cowork) · 2 read-only connect check (copy M3-P01 or M3-P08 depending on route) · 3 three search missions (PRJ-105 approval, PRJ-101 conflicting status, PRJ-104 delay) with copy-ready M3-P03 prompts, hints and keyword-checked answers · 4 one-page summary + source check (M3-P02, M3-P04) · 5 **"คุณคือผู้อนุมัติ"**: approve/reject 6 lines of a Claude edit plan for the shared Capex Tracker (3 safe, 3 unsafe: formula → value, another site's tab, overwrite original) with explanations · 6 check-before-save checklist + the 5 rules.
- **Engagement mechanic:** points (missions 10, plan decisions 5, checklist 2), rank badge (ผู้ฝึกเชื่อมต่อ → ผู้เชื่อมต่อ → นักสืบข้ามแหล่ง → Connector Guardian), progress bar and green stage borders.
- **Data:** synthetic facts from `data/pack/` (PRJ-101/104/105, Capex Tracker cells). Progress saved in `localStorage` (this browser only, try/catch).
- **Export PDF:** button + print CSS; prints route, mission answers with feedback, approval decisions with reasons, checklists and the 5 rules.
- **AI calls:** none (no Team-plan usage). Copy buttons only put prompts on the clipboard; the learner pastes them into Claude.
