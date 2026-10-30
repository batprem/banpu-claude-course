# UC4 · จากบันทึกประชุมสู่ Action Tracker (Meeting-to-Action Tracker)
> ข้อมูลสมมติเพื่อการอบรมเท่านั้น (synthetic) ไม่ใช่ข้อมูลจริงของบ้านปู · ทำสำเนาก่อนให้ Claude แก้ (copy-before-write)

**เจ้าของโจทย์ (สมมติ):** ทีม Ops Planning ประชุมทุกสัปดาห์ action item กระจายอยู่ในบันทึกหลายรูปแบบ งานหลุดบ่อยเพราะไม่มีใครรวมเข้า tracker

| Canvas | ตั้งต้น (ทีมปรับได้) |
|---|---|
| Data | `meetings/` 4 ไฟล์ (.md .txt .vtt transcript) · `action_tracker_sharepoint_list_export.csv` (tracker เดิม) · `owners.md` |
| Connector | วันจริง: SharePoint List (tracker) + Outlook (ร่างอีเมลติดตาม) · วันนี้: โฟลเดอร์ใน Cowork |
| Output | Tracker ฉบับใหม่ (ใคร · ทำอะไร · กำหนด · สถานะ · มาจากประชุมไหน) + ร่างอีเมลติดตามรายคน |
| Trade-off | งานที่ไม่มีวันกำหนดห้ามให้ AI เดาวัน → ใส่ "ต้องยืนยัน" · ร่างอีเมลเท่านั้น · transcript จริงอาจมีเรื่องส่วนตัว = 🟡 |

**เกณฑ์เสร็จ:** ดึง action item ครบ (ใบ้: ≥ 8 รายการ) · จับงานที่ปิดแล้ว/ถูกเลื่อน · มีรายการ "ต้องยืนยันวัน" อย่างน้อย 2 รายการ
**ต่อยอด:** Connector Outlook/SharePoint (M3) · Weekly Insight (M6)
**Prompt เริ่มต้น:** `M7-P07`
