# ⚠️ TRAINING SAMPLE · Skill ปลอมสำหรับฝึกตรวจ ห้ามติดตั้ง

โฟลเดอร์ `quick-excel-summary-pro/` เป็น **Skill จากภายนอกที่แต่งขึ้น** เพื่อให้ผู้เรียน M5 ฝึกหา "ธงแดง" ตาม Skill Security Checklist

ทำไมถึงปลอดภัยสำหรับการอบรม
- ไม่มีโค้ดที่ทำงานได้: script ใช้นามสกุล `.py.txt` และบรรทัดแรกของโค้ดสั่ง `raise SystemExit` ทันที
- URL ทุกอันเป็น `example.com` / `example.net` (โดเมนสงวนสำหรับตัวอย่าง ตาม RFC 2606) ไม่มีเซิร์ฟเวอร์จริงรับข้อมูล
- ข้อความ base64 ในไฟล์ถอดแล้วได้แค่ `https://example.com/collect`
- `SKILL.md` ขึ้นต้นด้วยบรรทัดคำเตือนก่อน frontmatter จึงไม่ใช่ Skill ที่ติดตั้งได้
- ชื่อผู้สร้าง ลิงก์ และกลุ่มแชตทั้งหมดเป็นของสมมติ

วิธีใช้ในห้อง: เปิดไฟล์ใน Artifact `artifacts/skill-security-checklist.html` (แท็บ "ล่าธงแดง") หรือแนบโฟลเดอร์นี้ใน Chat แล้วใช้ prompt `M5-P05`
เฉลยสำหรับวิทยากร: `../trainer/audit-answer-key.md`
