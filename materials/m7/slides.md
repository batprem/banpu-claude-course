---
title: Capstone · Use Case จริงของเรา
module: M7
duration: 75 min (Lecture 10 / Workshop 65)
---
<!-- type: section -->
# M7 · Capstone: Use Case จริงของเรา

เอาทุกอย่างตั้งแต่เช้ามาประกอบเป็นงานจริง 1 ชิ้น ในทีม 6–8 คน (5 ทีมต่อคลาส)

15:00–16:15 · 75 นาที (บรรยาย 10 · Workshop 65)

???
[0:00] หลังเบรกบ่าย พลังงานห้องเริ่มตก บอกตรง ๆ ว่า 65 นาทีต่อจากนี้ "เราทำ ไม่ใช่ฟัง" บรรยายแค่ 10 นาที
Requirement 14 (Capstone: data, connector, output, trade-off · Hands-on) และประยุกต์ requirement 1–7
ผลลัพธ์ของแต่ละทีม: ต้นแบบ 1 ชิ้น + การ์ดบน Show & Share board + PDF แผนต่อยอด ที่เอาไปใช้ใน M8 แผน 30 วัน
ก่อนเริ่ม: ให้นับ 1–5 วนทั้งห้องเพื่อแบ่งทีม (หรือใช้ทีมที่ Hi-I จัดไว้ล่วงหน้า)

---
<!-- type: story -->
# Novo Nordisk: เอกสารที่เคยใช้ 10+ สัปดาห์ เหลือ 10 นาที

- ทีมเล็ก **11 คน** เริ่มจากงานเดียวที่เจ็บที่สุด: เขียนรายงานผลการศึกษาทางคลินิก
- เดิมผู้เขียน 1 คนทำได้เฉลี่ย **2.3 ฉบับต่อปี**
- ใช้ Claude ร่าง → เวลาเขียนลดลง 90% · รอบรีวิว**ลดลงครึ่งหนึ่ง**
- แต่ร่างทุกฉบับ "ส่งถึงมือคนเพื่อตรวจและอนุมัติ"

> "เราโยนข้อมูลใส่ LLM แล้วหวังว่าจะออกมาดีไม่ได้" — ทีม Novo Nordisk

???
[0:45] เคสจริงจาก Anthropic customer story (SOURCES #1) เล่า 1 นาที
ประเด็นที่อยากให้ติดหัว 3 ข้อ: (1) เริ่มจาก use case เดียวที่ชัด ไม่ใช่ "เอา AI มาใช้ทั้งองค์กร" (2) ทีมเล็กก็สร้างได้ (3) คนยังเป็นผู้อนุมัติ = Human-in-the-Loop ตรงกับที่เราพูดมาทั้งวัน
ตัวเลข 10+ สัปดาห์ → 10 นาที เป็นของงานร่างเอกสาร ไม่ใช่การอนุมัติ ย้ำอย่าเข้าใจผิดว่า "ไม่ต้องตรวจแล้ว"
ถามห้อง: "งานไหนของทีมคุณที่กินเวลาเป็นสัปดาห์ แต่รูปแบบซ้ำเดิมทุกครั้ง?" นั่นคือผู้สมัคร capstone

---

# 65 นาทีจากนี้: ทำ → ตรวจ → โชว์

```mermaid
flowchart LR
    T["① ตั้งทีม + เลือก use case<br/>5 นาที"]:::human --> A["② วิเคราะห์ Canvas<br/>Data → Connector → Output → Trade-off<br/>10 นาที"]:::human
    D[("Data pack สมมติ UC1–UC5<br/>หรือ use case ของทีม (🟢 เท่านั้น)")]:::data --> A
    A --> B["③ สร้างต้นแบบด้วย Cowork<br/>21 นาที"]:::ai
    B --> C{"HITL: ตัวเลข/ที่มา<br/>ถูกไหม?"}:::human
    C -- แก้ --> B
    C -- ผ่าน --> P["④ เตรียมนำเสนอ<br/>+ โพสต์ Show & Share board · 4 นาที"]:::human
    P --> S["⑤ Show & Share 3 นาที/ทีม<br/>+ feedback 1 นาที · 20 นาที"]:::human
    S --> V["⑥ โหวต + สรุป → M8 · 5 นาที"]:::human
    classDef human fill:#E4572E,color:#fff,stroke:#1F2933;
    classDef ai fill:#2E86AB,color:#fff,stroke:#1F2933;
    classDef data fill:#3BA55C,color:#fff,stroke:#1F2933;
```
🟧 คน (HITL) · 🟦 AI · 🟩 Data/Connector

???
[2:00] เดินตาม diagram: ส้ม = เวลาที่ทีมต้องคิดและตัดสินใจเอง น้ำเงิน = ให้ Cowork ทำ
ย้ำว่าช่วงสร้างต้นแบบมีลูปกลับ: ถ้าตัวเลขหรือที่มาไม่ผ่าน ให้กลับไปแก้ ไม่ใช่เอาไปโชว์
เวลาจริงบนนาฬิกา: 15:10 ตั้งทีม · 15:15 Canvas · 15:25 สร้าง · 15:46 เตรียมนำเสนอ · 15:50 Show & Share · 16:10 โหวต/สรุป
บทบาทในทีม (เลือกใน 1 นาที): ผู้ขับ Cowork 1 · ผู้ตรวจ HITL 1 · ผู้ดูเวลา 1 · ผู้นำเสนอ 1 · ที่เหลือเป็นเจ้าของโจทย์/นักวิเคราะห์

---

# กรอบคิด Use Case: Data → Connector → Output → Trade-off

```mermaid
flowchart LR
    D[("Data<br/>ข้อมูลอยู่ไหน · สีอะไร 🟢🟡🔴")]:::data --> C[("Connector<br/>SharePoint · Outlook · โฟลเดอร์")]:::data
    C --> P["Process<br/>Claude / Cowork ทำอะไร"]:::ai
    P --> H{"HITL<br/>ใครตรวจ ตรงไหน"}:::human
    H --> O["Output<br/>Word · Excel · PPTX · Artifact · ร่างอีเมล"]:::ai
    O --> T{"Trade-off<br/>ความปลอดภัย · ข้อจำกัด · usage"}:::human
    T -. ปรับขอบเขต .-> D
    classDef human fill:#E4572E,color:#fff,stroke:#1F2933;
    classDef ai fill:#2E86AB,color:#fff,stroke:#1F2933;
    classDef data fill:#3BA55C,color:#fff,stroke:#1F2933;
```
🟧 คน (HITL) · 🟦 AI · 🟩 Data/Connector

???
[3:00] นี่คือ requirement 14 ทั้งข้อในภาพเดียว ทุกทีมต้องตอบครบ 4 ช่อง (+ จุด HITL) ก่อนลงมือ
Data: ข้อมูลอยู่ที่ไหน ใครเป็นเจ้าของ สีอะไรตาม Data Traffic Light (M1) · Connector: SharePoint / Outlook (M3) หรือโฟลเดอร์ใน Cowork (M2) — ไม่มี Google Drive
Output: เลือกตามคนอ่าน (Output Picker ของ M4) · Trade-off: ดูสไลด์ถัดไป
เส้นประกลับไปที่ Data: บ่อยครั้งทางแก้ Trade-off คือ "ลดขอบเขตข้อมูล" เช่น ใช้แค่ตารางสรุป ไม่ใช้ข้อมูลรายบุคคล

---

# Trade-off: 3 คำถามก่อนบอกว่า "ใช้ได้จริง"

| มุม | ถามตัวเอง | ทางแก้ที่เรียนแล้ว |
|---|---|---|
| 🛡️ **ความปลอดภัย** | ข้อมูลสีอะไร? ใครเห็นผลลัพธ์? | 🟡 anonymize · 🔴 ไม่ใส่ Claude (M1) |
| ⚠️ **ข้อจำกัด** | ไฟล์ใหญ่/เยอะเกินไหม? ต้องเปิดเครื่องไหม? | แบ่งไฟล์ · สรุปก่อน (M2, M4, M6) |
| 🔋 **Usage** | ทำบ่อยแค่ไหน? ใช้ model อะไร? | Skill · แชตใหม่ · model เบา (M5, M8) |
| ✋ **HITL** | ใครอนุมัติก่อนส่ง/บันทึก? | Plan → Approve → Execute · copy-before-write |

???
[4:30] ทีมที่ได้คะแนนสูงไม่ใช่ทีมที่ demo สวยที่สุด แต่เป็นทีมที่บอกได้ว่า "อะไรยังไม่ควรให้ Claude ทำ"
ตัวอย่าง trade-off ที่ดี: "รายงาน incident ใช้ชื่อพนักงานไม่ได้ (🔴/🟡) เราจึงตัดคอลัมน์ชื่อก่อนส่งเข้า Cowork"
ตัวอย่าง usage: งานรายสัปดาห์ที่สั่งด้วย prompt ยาวทุกครั้ง → ทำเป็น Skill (M5) แล้วตั้ง Scheduled task (M6) แต่ Scheduled task ต้องเปิดเครื่องไว้
เกณฑ์ rubric ข้อ 3 คือ trade-off ข้อนี้โดยตรง

---

# เมนูโจทย์: 5 use case (ข้อมูลสมมติ) หรือโจทย์ของทีมเอง

| # | Use case | Data | Connector | Output |
|---|---|---|---|---|
| UC1 | สรุปสัญญาจัดซื้อ | สัญญา .docx 3 ฉบับ + register | SharePoint | Excel + ปฏิทินแจ้งยกเลิก |
| UC2 | รายงาน Incident รายสัปดาห์ | log 150+ แถว + อีเมล 3 ฉบับ | SharePoint · Outlook | รายงาน + ร่างอีเมล |
| UC3 | รวมข้อมูล ESG 4 Site | xlsx/csv คนละหน่วย | SharePoint | ตารางรวม + Dashboard |
| UC4 | ประชุม → Action tracker | บันทึก .md .txt .vtt + tracker | SharePoint · Outlook | Tracker + ร่างอีเมลติดตาม |
| UC5 | Energy market brief | ราคา + ข่าว + มุมมองทีม | โฟลเดอร์ / เว็บสาธารณะ | Brief 1 หน้า |

**โจทย์ของทีมเอง (BYO):** ได้ แต่ใช้ข้อมูล 🟢 หรือข้อมูลจำลองเท่านั้น

???
[5:30] ทั้ง 5 โจทย์ปรับจากรูปแบบงานที่ทีม Hi-I ส่งมา (ฉบับนี้เป็นตัวแทนจนกว่าจะได้ use case จริง — ดู README open question) ข้อมูลทุกไฟล์เป็นข้อมูลสมมติ อยู่ใน ZIP M7_uc1…uc5
แต่ละโจทย์มีกับดักที่ตั้งใจใส่ไว้ให้ HITL จับ เช่น UC2 มีวันที่ 2026-13-02 และ "near miss" ตัวพิมพ์เล็ก · UC3 Site G ขาดเดือน ต.ค. และ Site F มีแค่รายไตรมาส · UC4 งานไม่มีวันกำหนด — ไม่ต้องบอกผู้เรียนล่วงหน้า
BYO: ทีมที่มีโจทย์จริงให้ใช้ Canvas เดียวกัน แต่สร้างข้อมูลจำลองก่อน (ให้ Claude สร้างไฟล์ตัวอย่างจากหัวคอลัมน์จริง ไม่ใช้ค่าจริง — prompt M7-P02)
ถ้ามีหลายทีมเลือกโจทย์ซ้ำ ได้ ไม่เป็นไร ทีมที่โจทย์ซ้ำจะเห็นทางแก้ต่างกันตอน Show & Share

---

# ตัวอย่างเต็ม 1 โจทย์: UC2 รายงาน Incident รายสัปดาห์

```mermaid
flowchart LR
    L[("incident_log.csv<br/>SharePoint List export")]:::data --> CL["Cowork ทำความสะอาด<br/>+ เทียบสัปดาห์ก่อน"]:::ai
    E[("อีเมล 3 ฉบับ<br/>Outlook")]:::data --> CL
    CL --> Q{"HITL: ตรวจข้อมูลผิดปกติ<br/>วันที่ผิด · ตัวพิมพ์"}:::human
    Q --> RP["ร่างรายงาน HSE รายสัปดาห์<br/>+ ร่างอีเมล"]:::ai
    RP --> AP{"ผู้จัดการ HSE อนุมัติ<br/>ก่อนส่ง (ไม่ส่งเอง)"}:::human
    classDef human fill:#E4572E,color:#fff,stroke:#1F2933;
    classDef ai fill:#2E86AB,color:#fff,stroke:#1F2933;
    classDef data fill:#3BA55C,color:#fff,stroke:#1F2933;
```
🟧 คน (HITL) · 🟦 AI · 🟩 Data/Connector

- Data ส่วนใหญ่ 🟢 สมมติ · ชื่อพนักงานในงานจริง = 🟡 ต้องตัดก่อน
- Trade-off: ร่างอีเมลเท่านั้น **ไม่ส่งเอง** · ไม่ต้องใช้ model ใหญ่

???
[6:30] ทำให้ดูว่า "Canvas ที่ครบ" หน้าตาเป็นอย่างไร ใช้เวลา 1 นาที ไม่ต้อง demo จริง
ไล่ 4 ช่อง: Data = incident_log.csv (เหมือน export จาก SharePoint List) + อีเมล Outlook 3 ฉบับ · Connector = SharePoint/Outlook ในวันจริง หรือโฟลเดอร์ ZIP ถ้าไม่มี test tenant (เส้นทาง B ของ M3)
Output = รายงานสัปดาห์ล่าสุดเทียบสัปดาห์ก่อน + ร่างอีเมลถึงผู้จัดการ HSE · HITL 2 จุด: ตรวจข้อมูลผิดปกติก่อนวิเคราะห์ และผู้จัดการอนุมัติก่อนส่ง
Trade-off: อีเมล 01 มีประโยคพูดถึงพนักงานที่บาดเจ็บ ในงานจริงต้อง anonymize (🟡) · ข้อมูลไม่ใหญ่ ใช้ model เบาได้ (M8)

---

# สร้างต้นแบบด้วย Cowork: สูตรเดิมจากเมื่อเช้า

```mermaid
flowchart LR
    F[("โฟลเดอร์ทีม (สำเนา)<br/>copy-before-write")]:::data --> I["Interview / Use your own words<br/>M2-P04 · M2-P03"]:::ai
    I --> PL["Claude เสนอแผน<br/>Plan"]:::ai
    PL --> AP{"ทีมอนุมัติแผน<br/>Approve"}:::human
    AP --> EX["Cowork ลงมือ<br/>Execute"]:::ai
    EX --> CK{"ตรวจ 3 จุด<br/>ตัวเลข · ที่มา · ห้ามส่งเอง"}:::human
    CK -- ยังไม่ผ่าน --> EX
    CK -- ผ่าน --> OUT["ต้นแบบ v1<br/>+ screenshot ลงบอร์ด"]:::ai
    classDef human fill:#E4572E,color:#fff,stroke:#1F2933;
    classDef ai fill:#2E86AB,color:#fff,stroke:#1F2933;
    classDef data fill:#3BA55C,color:#fff,stroke:#1F2933;
```
🟧 คน (HITL) · 🟦 AI · 🟩 Data/Connector

???
[7:30] ไม่มีอะไรใหม่ เป็นการประกอบของที่เรียนมา: copy-before-write (M3), Interview/Use your own words (M2-P04, M2-P03), Plan → Approve → Execute (M2-P02)
ไม่ต้องสร้างให้สมบูรณ์ เป้าหมายคือ "ต้นแบบ v1 ที่ทำงานได้ 1 รอบ" กับข้อมูลสมมติ
ตรวจ 3 จุดก่อนเอาไปโชว์: สุ่มตัวเลข 2 ค่าเทียบไฟล์ต้นฉบับ · ทุกข้อสรุปบอกที่มาได้ · ไม่มีอะไรถูกส่งออกหรือบันทึกทับเอง
ถ้า usage ใกล้เต็ม: คนเดียวในทีมเป็นผู้ขับ Cowork คนอื่นตรวจและเตรียมการ์ด ไม่ต้องรันพร้อมกันทั้ง 6 คน

---

# Show & Share: 3 นาทีต่อทีม

```mermaid
flowchart LR
    TM["ทีมกรอกการ์ดบนบอร์ด<br/>use case · diagram · demo"]:::human --> BD[("Show & Share board<br/>Artifact")]:::data
    BD --> PR["นำเสนอ 3 นาที<br/>ปัญหา → Demo → Trade-off"]:::human
    PR --> FB["วิทยากรให้ feedback<br/>rubric 4 ข้อ · 1 นาที"]:::human
    PR --> VT["ทุกคนโหวต<br/>🏆 ใช้ได้จริง · 🛡️ ปลอดภัย · 💡 ไอเดีย"]:::human
    FB --> PDF["Export PDF<br/>แผนต่อยอด → M8 แผน 30 วัน"]:::ai
    VT --> PDF
    classDef human fill:#E4572E,color:#fff,stroke:#1F2933;
    classDef ai fill:#2E86AB,color:#fff,stroke:#1F2933;
    classDef data fill:#3BA55C,color:#fff,stroke:#1F2933;
```
🟧 คน (HITL) · 🟦 AI · 🟩 Data/Connector

**Rubric วิทยากร (ข้อละ 1–4):** ① ปัญหาจริงและวัดผลได้ ② ต้นแบบทำงาน ③ Trade-off/HITL ชัด ④ ต่อยอดได้ใน 30 วัน

???
[8:30] โครง 3 นาที: 30 วินาทีปัญหา (ใครเจ็บ เสียเวลาเท่าไร) · 90 วินาที demo หรือ screenshot · 60 วินาที trade-off + ถ้าทำต่อจะทำอะไร
วิทยากรให้ feedback 1 นาทีต่อทีมตาม rubric 4 ข้อ (อยู่ในบอร์ด แท็บ "Rubric") ไม่ต้องให้คะแนนประกาศหน้าห้อง ใช้เป็นคำแนะนำ
โหวต 3 หมวด แต่ละคนได้ 1 เสียงต่อหมวด ห้ามโหวตทีมตัวเอง ทีมชนะได้ปรบมือ + PDF การ์ดไปเสนอหัวหน้า
PDF จาก Export PDF ของบอร์ด = ข้อมูลตั้งต้นของ M8 แผน 30 วัน

---

# กติกา 4 ข้อ แล้วเริ่มเลย

1. **ข้อมูลสมมติ หรือ 🟢 เท่านั้น** · ห้ามเปิดไฟล์งานจริงของบริษัท
2. **Connector: SharePoint / Outlook** หรือโฟลเดอร์สำเนา · ไม่ใช้ Google Drive
3. **ไม่มีอะไรถูกส่ง/บันทึกทับโดยไม่มีคนอนุมัติ**
4. **ติดขัดเกิน 3 นาที → ยกมือ** หรือดูทางสำรองในคู่มือ

เปิด: `workshop.md` · `prompts.md` (M7-P01…P10) · บอร์ด `artifacts/show-share-board.html`

???
[9:30] อ่านกติกาเร็ว ๆ แล้วเปิดนาฬิกานับถอยหลังบนบอร์ด (แท็บ Timer)
ข้อ 3 สำคัญที่สุดในวันนี้: UC2 และ UC4 มีร่างอีเมล ต้องเป็น draft เท่านั้น
ข้อ 4: วิทยากรและผู้ช่วยเดินวน ตามตาราง "จุดที่ทีมมักติด" ใน workshop หน้า 6 · ถ้าห้องมีผู้ช่วย 1 คน แบ่งกันดูคนละครึ่งห้อง
แจก ZIP ผ่านลิงก์ SharePoint ของคลาส (หรือ USB สำรอง) ตอนที่ตั้งทีม
