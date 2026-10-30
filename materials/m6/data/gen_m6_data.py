#!/usr/bin/env python3
"""Generate the M6 Automation sample pack (synthetic, small, safe to commit).

Output: materials/m6/data/pack/
  meeting_notes/*.md   6 synthetic meeting notes, week 43–44 of 2569 (Oct 2026)
  news_fallback.md     synthetic energy-news headlines (backup if web search is blocked)
  watchlist.md         what the Weekly Insight watches (topics, keywords, owners)
Emails are NOT copied here: the demo reads materials/m3/data/pack/outlook/ read-only.

Every person, site, number and email is fictional. Run: python3 materials/m6/data/gen_m6_data.py
"""
import pathlib

OUT = pathlib.Path(__file__).resolve().parent / "pack"

MEETINGS = [
    ("2026-10-19_safety-standdown-site-a.md", "Safety Stand-down · Site A (เหมืองสมมติ ภูผาทอง)", "19 ต.ค. 2569 · 08:00–08:30",
     "คุณวิไลวรรณ (Project Control), คุณสมศักดิ์ (PM Site A), หัวหน้ากะ 3 คน",
     ["near-miss ระหว่างยกลูกกลิ้งสายพาน CV-03 (PRJ-101) ไม่มีผู้บาดเจ็บ",
      "สาเหตุเบื้องต้น: ไม่มีผู้ให้สัญญาณเฉพาะ และ lifting plan ไม่ได้ทบทวนหลังเปลี่ยนเครน",
      "มาตรการ: ทบทวน lifting plan ทุกงาน · เพิ่มผู้ให้สัญญาณ 1 คนต่อกะ"],
     [("บันทึก near-miss ใน Issue Log หมวด Safety", "คุณสมศักดิ์", "20 ต.ค."),
      ("ทบทวน lifting plan ทุกงานยกในเดือนนี้", "หัวหน้ากะ A", "31 ต.ค.")]),
    ("2026-10-22_finance-capex-check.md", "Finance check · Capex Tracker ก่อนปิดเดือน", "22 ต.ค. 2569 · 14:00–14:40",
     "คุณนกน้อย (Finance BP), คุณกัญญา (PM Site D), คุณประวิทย์ (PM Site F)",
     ["ตัวเลข Spent ใน Capex Tracker 3 แท็บไม่ตรงกับระบบบัญชี (ต่างกันรวม 2.1 ล้านบาท)",
      "PRJ-105 (Overhaul Unit 2) อาจต้องใช้งบเพิ่ม รออีเมลขออนุมัติอย่างเป็นทางการ",
      "PRJ-108 BESS: ยังไม่ตั้งงบ รอผลศึกษาความเป็นไปได้"],
     [("ทุก PM ตรวจแท็บไซต์ตัวเองและยืนยันตัวเลข", "PM ทุกไซต์", "30 ต.ค."),
      ("สรุปส่วนต่าง Spent ให้ผู้บริหาร", "คุณนกน้อย", "2 พ.ย.")]),
    ("2026-10-25_project-review-oct.md", "Project Review ประจำเดือน ต.ค. 2569", "25 ต.ค. 2569 · 09:00–10:30",
     "คุณชัยวัฒน์ (ผู้อำนวยการโครงการ), คุณสมศักดิ์, คุณกัญญา, คุณประวิทย์, คุณมะลิ, คุณนกน้อย",
     ["PRJ-104 บำบัดน้ำทิ้งเฟส 2 ล่าช้า รอใบอนุญาตระบายน้ำ (คาดออกกลาง พ.ย.)",
      "PRJ-106 DCS: เลื่อน go-live เป็น มี.ค. 2570 แล้ว แต่ยังเสี่ยงงบเกิน",
      "PRJ-101 สายพาน CV-03: Tracker ยัง On track แต่ supplier ส่งลูกกลิ้งไม่ครบ",
      "ทุก PM อัปเดต Capex Tracker ก่อน 30 ต.ค. ห้ามแก้แท็บของไซต์อื่น"],
     [("ติดตามใบอนุญาต PRJ-104", "คุณมะลิ", "15 พ.ย."),
      ("ส่งแผนลดความเสี่ยงงบ PRJ-106", "คุณกัญญา", "6 พ.ย."),
      ("รวบรวมสถานะโครงการส่งผู้บริหาร (ทุกวันจันทร์ 10:00)", "Project Control", "ทุกสัปดาห์")]),
    ("2026-10-27_pm-weekly-w44.md", "ประชุมทีม PM รายสัปดาห์ (สัปดาห์ 44)", "27 ต.ค. 2569 · 13:30–14:00",
     "คุณวิไลวรรณ, คุณสมศักดิ์, คุณกัญญา, คุณประวิทย์, คุณมะลิ",
     ["PRJ-101: ถ้าไม่ได้ลูกกลิ้งภายใน 7 พ.ย. เสร็จช้าจาก 15 ธ.ค. เป็นปลาย ธ.ค. → ควรเปลี่ยนสถานะเป็น At risk",
      "PRJ-112 รถขุด EX-07 รออะไหล่ไฮดรอลิก งานอาจเลื่อนไป 2 ธ.ค.",
      "PRJ-107 inverter ชุด 4 ผ่านการทดสอบ ชุด 5–6 ส่งของ 12 พ.ย.",
      "ทดลองใช้ Claude ร่างรายงานสถานะรายสัปดาห์ โดยคนตรวจก่อนส่งทุกครั้ง"],
     [("อัปเดตสถานะ PRJ-101 ใน Project Tracker", "คุณสมศักดิ์", "29 ต.ค."),
      ("ตั้ง Scheduled task ร่างรายงานสัปดาห์ (ทดลอง 4 สัปดาห์)", "คุณวิไลวรรณ", "2 พ.ย.")]),
    ("2026-10-28_energy-market-briefing.md", "Energy market briefing (ภายใน · ข้อมูลสมมติ)", "28 ต.ค. 2569 · 10:00–10:30",
     "ทีมกลยุทธ์สมมติ 4 คน (คุณภูมิ, คุณดาว, คุณต้นกล้า, คุณฟ้าใส)",
     ["ติดตามราคาถ่านหิน Newcastle และ LNG เอเชีย ทุกสัปดาห์ (ใช้ข่าวสาธารณะ ไม่ใช้รายงานซื้อขายภายใน)",
      "อยากได้สรุปสั้น 1 หน้าทุกเช้าวันจันทร์: ข่าวสำคัญ 5 ข่าว + ผลต่อโครงการของเรา",
      "ข้อกังวล: AI อาจสรุปข่าวผิดหรือไม่มีที่มา → ต้องมีลิงก์ทุกข่าว และคนตรวจก่อนส่งต่อ"],
     [("กำหนดรายการคำค้นข่าว (watchlist)", "คุณดาว", "30 ต.ค."),
      ("ทดลอง Weekly Energy Insight 2 รอบ แล้วประเมิน", "คุณภูมิ", "16 พ.ย.")]),
    ("2026-10-29_solar-site-f-sync.md", "Solar Site F · sync กับ supplier inverter", "29 ต.ค. 2569 · 15:00–15:20",
     "คุณประวิทย์ (PM Site F), ตัวแทน supplier สมมติ 2 คน",
     ["supplier ยืนยันส่ง inverter ชุด 5–6 วันที่ 12 พ.ย.",
      "ฝนตกหนักช่วงต้น พ.ย. อาจทำให้ติดตั้งช้า 2–3 วัน",
      "ยังไม่มีผลกระทบต่องบ"],
     [("ยืนยันทีมติดตั้งและเครนวันที่ 12–15 พ.ย.", "คุณประวิทย์", "5 พ.ย.")]),
]

NEWS = """# ข่าวพลังงานสำรอง (ข่าวจำลอง · ใช้เมื่อ web search ใช้ไม่ได้ในห้องอบรม)

> ทุกข่าวด้านล่างเป็น **ข่าวสมมติ** เขียนขึ้นเพื่อฝึก ไม่ใช่ข่าวจริง ตัวเลขไม่ใช่ราคาตลาดจริง
> ในการสาธิตจริง ให้ Claude ค้นเว็บสาธารณะและแนบลิงก์ทุกข่าว

| # | วันที่ | หัวข่าว (สมมติ) | แหล่ง (สมมติ) |
|---|---|---|---|
| 1 | 26 ต.ค. 2569 | ราคาถ่านหินเอเชียทรงตัว หลังความต้องการไฟฟ้าช่วงปลายฝนลดลง | energy-news.example.com |
| 2 | 27 ต.ค. 2569 | ราคา LNG ตลาดจรเอเชียขยับขึ้นเล็กน้อย ก่อนเข้าฤดูหนาว | lng-watch.example.com |
| 3 | 28 ต.ค. 2569 | หน่วยงานกำกับเปิดรับฟังความเห็นร่างแผนพลังงานหมุนเวียนฉบับใหม่ | policy-brief.example.com |
| 4 | 29 ต.ค. 2569 | ราคาแผงโซลาร์และ inverter ในภูมิภาคลดลงต่อเนื่องไตรมาสที่ 3 | solar-market.example.com |
| 5 | 29 ต.ค. 2569 | พายุโซนร้อนคาดว่าจะทำให้ฝนตกหนักภาคตะวันออกเฉียงเหนือต้น พ.ย. | weather-desk.example.com |
| 6 | 30 ต.ค. 2569 | ผู้ผลิตแบตเตอรี่รายใหญ่ประกาศขยายโรงงาน BESS ในเอเชียตะวันออกเฉียงใต้ | storage-news.example.com |
"""

WATCHLIST = """# Watchlist · Weekly Energy & Ops Insight (ตัวอย่างการตั้งค่า)

| หมวด | แหล่ง | คำค้น / ตัวกรอง | เจ้าของ (ตรวจก่อนส่ง) |
|---|---|---|---|
| 🌐 Web (ภายนอก) | ข่าวสาธารณะ 7 วันล่าสุด | coal price Asia, LNG Asia spot, Thailand renewable policy, solar inverter price, BESS Southeast Asia | คุณดาว |
| ✉️ Email (Outlook) | กล่องทดสอบ `m3.learner@example.com` | หัวเรื่องขึ้นต้น `[PRJ-` และ "ขออนุมัติ" 7 วันล่าสุด | คุณวิไลวรรณ |
| 📝 Meeting (SharePoint) | โฟลเดอร์ `Meeting Notes/2569` | ไฟล์ที่แก้ไขใน 7 วันล่าสุด | คุณวิไลวรรณ |

กติกา: ร่างอย่างเดียว · ห้ามส่งอีเมล · ห้ามแก้ไฟล์ต้นทาง · ทุกข้อมีที่มา · ถ้าแหล่งไหนเข้าไม่ได้ให้บอกในหัวรายงาน
"""


def meeting_md(title, when, who, points, actions):
    lines = [f"# {title}", "", "> บันทึกประชุมสมมติสำหรับการอบรม · ไม่ใช่ข้อมูลจริง", "",
             f"**วันเวลา:** {when}  ", f"**ผู้เข้าประชุม:** {who}", "", "## ประเด็นหลัก"]
    lines += [f"{i}. {p}" for i, p in enumerate(points, 1)]
    lines += ["", "## Action items", "", "| งาน | ผู้รับผิดชอบ | กำหนด |", "|---|---|---|"]
    lines += [f"| {a} | {o} | {d} |" for a, o, d in actions]
    return "\n".join(lines) + "\n"


def main():
    (OUT / "meeting_notes").mkdir(parents=True, exist_ok=True)
    for name, *rest in MEETINGS:
        (OUT / "meeting_notes" / name).write_text(meeting_md(*rest), encoding="utf-8")
    (OUT / "news_fallback.md").write_text(NEWS, encoding="utf-8")
    (OUT / "watchlist.md").write_text(WATCHLIST, encoding="utf-8")
    print(f"wrote {len(MEETINGS)} meeting notes + news_fallback.md + watchlist.md → {OUT}")


if __name__ == "__main__":
    main()
