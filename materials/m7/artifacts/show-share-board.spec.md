# Spec · Show & Share Board (Artifact)

File: `show-share-board.html` · Owner: M7 · Feeds: M8 (30-day plan starts from each card's "ก้าวต่อไปใน 30 วัน")

## Purpose
One place where every Capstone team posts its use case in the same shape (Data → Connector → Output → Trade-off + HITL + diagram + demo note), the trainer runs the 3-minute presentations, scores the rubric, counts votes, and exports one PDF for the class. Covers requirement 14 (Capstone: data, connector, output, trade-off · Hands-on).

## Users
- **Teams (5 per class, 6–8 people):** the presenter fills tab ① on their own laptop (pasted into Claude as an Artifact, or opened as a local HTML file).
- **Trainer:** runs the board on the projector laptop: tabs ② – ⑤, Export PDF at the end.

## Interactions
1. **① การ์ดทีม** (team form): ชื่อทีม · โจทย์ (UC1–UC5 / BYO) · สมาชิก/บทบาท · ปัญหา · Data + สี 🟢🟡🔴 · Connector (SharePoint / Outlook / โฟลเดอร์ใน Cowork / เว็บสาธารณะ: no Google Drive option) · Output · HITL · Trade-off 3 มุม (🛡️ ⚠️ 🔋) · ผลที่วัดได้ · Demo link/note · ก้าวต่อไป 30 วัน.
   - **Diagram builder:** up to 6 boxes, each typed 🟩 Data / 🟦 AI / 🟧 คน (HITL), with live preview in the course colours. "ใช้แม่แบบของโจทย์" fills a starter flow per UC (matches `diagrams/uc*.mmd`). "คัดลอกเป็น Mermaid" exports the flow with the 3 standard `classDef`s.
   - Completeness meter (0–100%) counts 10 required fields + data colour + connector + diagram (≥ 3 boxes, ≥ 1 HITL box). Saving tells the team exactly what is missing.
   - **✅ บันทึกลงบอร์ด** (same device) or **📋 คัดลอกรหัสการ์ด**: a `M7CARD:` + base64(JSON) code the team pastes into the class chat. If clipboard access is blocked, the code appears in a text box to copy by hand.
2. **② บอร์ด:** paste one or more card codes → นำเข้า (same team name = update, not duplicate). Cards show in presentation order with ◀ ▶ to reorder, 🎤 นำเสนอ (jumps to Timer with that team), แก้ไข (loads into tab ①), ลบ (two-click confirm, no browser dialogs). "+ การ์ดตัวอย่าง" adds a filled UC2 example card for the briefing.
3. **③ โหวต:** table of teams × 3 categories (🏆 ใช้ได้จริง · 🛡️ ปลอดภัย · 💡 ไอเดีย); trainer counts hands and presses +1/−; leaders get 👑 and a highlight. Two-click reset.
4. **④ Rubric วิทยากร:** pick a team, score 4 criteria 1–4 (same rubric as workshop page 13), total /16, feedback note "1 ชม · 1 ถาม · 1 แนะ". Not shown on the board cards (coaching only), printed in the PDF.
5. **⑤ Timer:** presets 3:00 / 4:00 / 5:00 / 1:00, start/pause/reset, big digits; yellow at ≤ 30 s, red and counting overtime (`+0:12`) after zero; shows the presenting team's name and diagram.

## Export PDF
- Button in the header from `materials/_shared/export-pdf.html` (window.print + print CSS).
- Print hides tabs, forms and buttons and prints `#report`: class name + date (Thai calendar), vote winners per category, every team card in full (with diagram and vote counts), and the rubric table with feedback.
- If the board is empty (a team printing from its own laptop), the PDF prints the team's current draft card instead, so each team can keep its own one-page record.

## Data
- No AI calls, no network calls except Google Fonts. State in `localStorage` key `m7-show-share-v1` (every read/write wrapped in try/catch; the page works without storage, it just forgets on reload).
- Card codes are plain base64 JSON, not encrypted: the board tells teams to use synthetic data only. Demo links render as links only when they are `https://` URLs; everything else is escaped text.
- Starter diagrams (`TPL`) and rubric (`RUB`) are constants in the script; keep them in sync with `diagrams/uc*.mmd` and `workshop.md` page 13.

## Engagement mechanic
Live completeness meter, visual diagram builder in the course colours, the team's card "going up on the big screen", a visible countdown, and a 3-category vote with crowns, then a printable class record that becomes the starting point for M8's 30-day plan.

## Constraints
- Thai learner text; product terms in English. Synthetic data only; no real names or Banpu data on cards (the sample card is fictional).
- Connector choices limited to M365 (SharePoint, Outlook) plus local folder and public web; Google Drive is deliberately absent.
- Sharing one live board across devices would need a shared-state runtime; this version uses copy/paste codes so it works in any Claude Team account or offline. See README open question 3.
