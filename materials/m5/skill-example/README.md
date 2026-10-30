# Skill ตัวอย่าง: banpu-standard-report (ฉบับฝึกอบรม)

Skill ที่ใช้ใน M5 Workshop ขั้น 1–2 · ข้อมูลและรูปแบบทั้งหมดเป็นของสมมติเพื่อการอบรม ไม่ใช่มาตรฐานรายงานจริงของบ้านปู

```
banpu-standard-report/
├── SKILL.md                         # ชื่อ + description (Claude อ่านก่อน) + วิธีทำงาน โทน รูปแบบตัวเลข checklist
├── templates/report-template.md     # โครง 6 หัวข้อ ห้ามสลับ
└── examples/example-report-site-b.md# ตัวอย่างผลลัพธ์ (Site B ปี 2567, ข้อมูลจำลองจาก M2)
```

## ติดตั้งเพื่อทดสอบ (ผู้เรียน)

1. ดาวน์โหลด `banpu-standard-report.zip` ที่วิทยากรแชร์ (โฟลเดอร์ `banpu-standard-report/` ต้องอยู่ชั้นบนสุดของ ZIP)
2. Claude Desktop → **Settings → Capabilities → Skills** (บางเวอร์ชันอยู่ที่ Customize → Skills) → **Upload skill** → เลือก ZIP
3. เปิดสวิตช์ Skill และตรวจว่า Code execution / file creation เปิดอยู่ (ถ้าเมนูไม่มี ให้แจ้งวิทยากร: admin ต้องเปิดให้)
4. ทดสอบด้วย prompt `M5-P03` ใน `../prompts.md`

## สร้าง ZIP (วิทยากร)

```bash
cd materials/m5/skill-example && python3 -m zipfile -c banpu-standard-report.zip banpu-standard-report/
```

ZIP ไม่ถูก commit (ดู `.gitignore`) สร้างใหม่ก่อนอบรมทุกครั้งหลังแก้ไฟล์

## แชร์ในทีม (หลังผ่านการตรวจ)

ผู้สร้าง → ทดสอบกับข้อมูล 2 ชุด → ส่งให้ทีม Hi-I/IT ตรวจตาม Skill Security Checklist → Owner ของ Claude Team เพิ่มเป็น Skill ขององค์กร (organization skill) หรือแชร์ให้กลุ่มที่กำหนด → เก็บต้นฉบับและประวัติเวอร์ชันใน SharePoint ของทีม
