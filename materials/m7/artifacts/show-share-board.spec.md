# Spec · Capstone Board · ผลงานของฉัน (Artifact)

File: `show-share-board.html` (file name and claude.ai URL kept from the earlier version) · Owner: M7 · Feeds: M8 (30-day plan starts from each card's "ก้าวต่อไปใน 30 วัน")

## Purpose
One page where each learner, working alone, records their own Capstone in the same shape (Data → Connector → Output → Trade-off + HITL + diagram + demo note), checks their own work with the 4-item **เช็กลิสต์ตรวจงานตัวเอง**, and exports one PDF. Nobody presents, votes or scores. Covers requirement 14 (Capstone: data, connector, output, trade-off · Hands-on).

## Users
- **Every learner** on their own laptop (opened from the claude.ai link). Workshop pages 3–4 (fill the card), 12 (self-check), 13 (finish card + Export PDF).
- **Trainer:** walks around; may open the gallery to look at shared cards. No trainer-only tab.

## Interactions
1. **① การ์ดงานของฉัน** (my card): ชื่อ/ชื่อเล่น · โจทย์ (UC1–UC5 / ใช้งานของคุณเอง) · ปัญหา · Data + สี 🟢🟡🔴 · Connector (SharePoint / Outlook / โฟลเดอร์ใน Cowork / เว็บสาธารณะ: no Google Drive option) · Output · จุดที่คนตรวจ (HITL) · Trade-off 3 มุม (🛡️ ⚠️ 🔋) · ผลที่วัดได้ · Demo note · ก้าวต่อไป 30 วัน.
   - **Diagram builder:** up to 6 boxes, each typed 🟩 Data / 🟦 AI / 🟧 คน (HITL), live preview in the course colours. "ใช้แม่แบบของโจทย์" fills a starter flow per UC (matches `diagrams/uc*.mmd`). "คัดลอกเป็น Mermaid" exports the flow with the 3 standard `classDef`s.
   - Completeness meter (0–100%) counts 10 required fields + data colour + connector + diagram (≥ 3 boxes, ≥ 1 HITL box) + all 4 self-check items answered. Saving lists exactly what is missing.
   - **✅ บันทึกการ์ดของฉัน** (kept on this device) · **📋 คัดลอกรหัสการ์ด** (optional): a `M7CARD:` + base64(JSON) code to paste in the class chat. If clipboard access is blocked, the code appears in a text box to copy by hand. **ล้างฟอร์ม** needs two clicks.
2. **② แกลเลอรี** (read-only browsing, optional): my card first (marked "การ์ดของฉัน"), then cards added from pasted codes (same name + use case = update, not duplicate). Filter by use case. Each pasted card can be removed (two-click). "+ การ์ดตัวอย่าง" adds a filled UC2 example. No ordering, no focus, no counts.
3. **③ เช็กลิสต์ตรวจงานตัวเอง**: the 4 items of workshop page 12, each ✅ ผ่าน / ⚠️ ต้องแก้ + "ถ้า ⚠️ จะแก้อะไร". Score "ผ่านแล้ว x / 4" on the tab. Stored with the card and inside the card code.
   1. ตัวเลข/ข้อเท็จจริง 2 ค่าตรงกับต้นฉบับ (เปิดไฟล์เทียบเอง)
   2. ทุกข้อสรุปบอกที่มาได้
   3. ไม่มีข้อมูล 🟡/🔴 หรือข้อมูลจริงของบริษัท · ไม่มีอะไรถูกส่ง/บันทึกลงระบบ
   4. ใช้ได้จริง: บอกได้ว่าใครใช้ ประหยัดเวลาเท่าไร และก้าวต่อไปใน 30 วัน

## Export PDF
- Button in the header from `materials/_shared/export-pdf-artifact.html` (html2pdf.js → `downloads.save`, fallback `window.print()`); publish with `capabilities: {downloads: true}`.
- The PDF prints `#report` only: title with the learner's name + date (Thai calendar), my card in full (with diagram and self-check line), the self-check table (item · ✅/⚠️ · what I'll fix), and ก้าวต่อไปใน 30 วัน. Gallery cards are not printed.

## Data
- No AI calls, no network calls except Google Fonts and the pinned html2pdf.js. State in `localStorage` key `m7-capstone-board-v1` (every read/write wrapped in try/catch; the page works without storage, it just forgets on reload).
- Card codes are plain base64 JSON, not encrypted: the page says synthetic data only. Demo notes render as links only when they are `https://` URLs; everything else is escaped text.
- Starter diagrams (`TPL`) and the self-check items (`CHECK`) are constants in the script; keep them in sync with `diagrams/uc*.mmd` and `workshop.md` page 12.

## Engagement mechanic
Live completeness meter, visual diagram builder in the course colours, a 4-item self-check with a visible x / 4 score, an optional quiet gallery of other learners' cards, and a one-page PDF that becomes the starting point for M8's 30-day plan.

## Constraints
- Thai learner text; product terms in English. Synthetic data only; no real names or Banpu data on cards (the sample card is fictional).
- Connector choices limited to M365 (SharePoint, Outlook) plus local folder and public web; Google Drive is deliberately absent.

## History
- 3 Nov 2026: reworked for individual work (Prem's decision): the earlier group version's extra tabs were removed; tabs are now ① การ์ดงานของฉัน · ② แกลเลอรี · ③ เช็กลิสต์ตรวจงานตัวเอง. Same file name and URL.
