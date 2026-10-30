# Spec · Skill Security Checklist (Artifact)

File: `skill-security-checklist.html` · Owner: M5 · Can be reused by: M8 (security recap)

## Purpose
Learners practise auditing a third-party Skill **before** installing it, then record a verdict they can hand to the approver (Hi-I / IT). Covers requirement 9 (Third-party Skill Security, Hands-on).

## Users
- Learners (30–40 per class), solo or in pairs, opened as a Claude Artifact (company Claude Team account) or as a local HTML file.
- Trainer projects tab ① for the debrief, and uses the PDF as an example of an "audit record".

## Interactions
1. Header fields: ผู้ตรวจ/ทีม, Skill ที่ตรวจ, แหล่งที่ได้มา (all printed on the PDF).
2. **Tab ① ล่าธงแดง** (game): the 3 files of the fake Skill `quick-excel-summary-pro` are shown with line numbers. Learner clicks suspicious lines.
   - Hit → line turns red, toast shows the category and **why** it is a red flag.
   - Miss → line shakes, toast reminds the 5 questions (ใครทำ / ขอเข้าถึงอะไร / รันอะไร / ส่งไปไหน / ซ่อนอะไร).
   - HUD: found x/16, misses, hints used; progress bar; per-category chips (6 checklist categories); per-file "เหลือ n".
   - 💡 Hint names the file + category of a random unfound flag. 👀 Reveal highlights all remaining flags in yellow. ↺ Reset.
   - Badges: ≥6 🔎, ≥12 🥈 Skill Inspector, 16/16 🏆 Hi-I Ready.
3. **Tab ② Checklist & คะแนน**: 16 questions in 6 categories (ที่มา · สิทธิ์ · Script · ส่งข้อมูลออก · คำสั่งแอบแฝง · ผู้อนุมัติ/เวอร์ชัน); answers ✅ ผ่าน (1) / ❓ ไม่แน่ใจ (0.5) / ❌ ไม่ผ่าน (0). 10 questions are marked **สำคัญ** (critical).
   - Score = points ÷ 16 × 100.
   - Verdict: any critical ❌ → 🔴 ไม่ติดตั้ง · not all answered → grey · any ❌/❓ or no approver name → 🟡 ส่งให้ทีม Hi-I / IT ตรวจก่อน · all ✅ + approver → 🟢 ใช้ได้ตามเวอร์ชันที่อนุมัติ.
   - Prefill buttons: "Skill ปลอม" (all ❌ → 🔴) and "banpu-standard-report" (all ✅ except A2 ❓ → 🟡, teaching that even our own Skill needs an approver before team-wide use).
   - Approver name + date/version, free-text notes.
4. **Tab ③ บันทึกผลตรวจ**: "บันทึกผลลงตาราง" appends the current audit to an in-memory log so a learner can compare 2 Skills (fake vs own).

## Export PDF
- Button in the header, from `materials/_shared/export-pdf.html` (window.print + print CSS).
- Print hides tabs/controls and prints a generated report (`#report`, `.print-only.print-expand`): header fields, verdict + score, approver, notes, all 16 checklist answers, the full red-flag list (found / not found, file:line, why) and the audit log. So the PDF doubles as the answer key once the learner has played.

## Data
- Embedded JSON between `/*AUDIT_DATA_START*/ … /*AUDIT_DATA_END*/`.
- Canonical sources: the sample Skill files in `materials/m5/skill-audit-sample/quick-excel-summary-pro/` and flags in `materials/m5/data/audit_flags.json` (`id`, `file`, `match`, `cat`, `why`).
- After editing either, run `python3 materials/m5/data/sync_audit_sample.py` (fails if a `match` is not on exactly one line).
- Checklist questions live in the HTML (`Q` array). Everything is fictional; URLs are `example.com` / `example.net`.

## Engagement mechanic
Find-the-flaws game with instant explanations, hints with a visible cost, category chips that fill up, badges, then a "real" decision (verdict) and a printable audit record learners can keep as their personal template.

## Constraints
- Self-contained: Google Fonts only (IBM Plex Sans Thai / Mono). No network calls, no AI calls (uses no Team plan usage), no storage (log lives only until the page closes).
- Colours from STYLE.md; responsive to phone width; lines are keyboard-focusable (Tab + Enter).
- The checklist is a teaching default. The real policy and approver role come from Banpu Hi-I / IT (open question in README).
- Tested: headless Chrome, 16/16 flags clickable, verdict logic for the 3 cases, Export PDF prints 4 A4 pages.
