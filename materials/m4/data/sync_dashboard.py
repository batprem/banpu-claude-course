#!/usr/bin/env python3
"""Inject dashboard_data.json (+ hand-written causes) into artifacts/monthly-ops-dashboard.html.

Run after gen_m4_data.py. The HTML keeps a single line `/*DATA*/const DATA=...;/*END*/`.
Usage: python3 materials/m4/data/sync_dashboard.py
"""
import json
import pathlib
import re

HERE = pathlib.Path(__file__).resolve().parent
HTML = HERE.parent / "artifacts" / "monthly-ops-dashboard.html"

# Causes are what a human adds after reading sources 2–4 (shift log, SharePoint, Outlook) — fictional
CAUSES = {
    "D": {"short": "Overhaul หม้อไอน้ำ Unit 2 (PRJ-105)",
          "long": "Unit 2 หยุดตามแผน overhaul ตั้งแต่ ส.ค. และพบรอยร้าวท่อ superheater เพิ่ม → ขออนุมัติงบเพิ่ม 3.8 ลบ.",
          "ref": "อีเมล [PRJ-105] ขออนุมัติงบเพิ่ม 3.8 ล้านบาท · Project_Tracker PRJ-105"},
    "C": {"short": "รถขุด EX-07 รออะไหล่ (PRJ-112)",
          "long": "รถขุด EX-07 รออะไหล่ไฮดรอลิก รถขน C-HT11–13 ต้องรอคิว → ปริมาณลดแต่ต้นทุนคงที่ ต้นทุนต่อหน่วยจึงสูง",
          "ref": "อีเมล [PRJ-112] รถขุด EX-07 รออะไหล่ไฮดรอลิก · shift log ก.ย. 2569"},
    "B": {"short": "ฝนหนัก ก.ย. · รถ B-HT07 หยุดนาน",
          "long": "ฝนตกหนักทั้งเดือน downtime รวมสูงสุดใน 3 เหมือง รถ B-HT07 หยุดนานผิดปกติ ควรตรวจสภาพ",
          "ref": "shift_log_2568-2569.csv (สรุปด้วยสคริปต์)"},
}


def main():
    data = json.loads((HERE / "dashboard_data.json").read_text(encoding="utf-8"))
    data["causes"] = CAUSES
    js = "/*DATA*/const DATA=" + json.dumps(data, ensure_ascii=False, separators=(",", ":")) + ";/*END*/"
    page = HTML.read_text(encoding="utf-8")
    page, n = re.subn(r"/\*DATA\*/.*?/\*END\*/", lambda _: js, page, flags=re.S)
    assert n == 1, "marker not found"
    HTML.write_text(page, encoding="utf-8")
    print(f"{HTML.name}: data synced ({len(js) / 1024:.1f} KB)")


if __name__ == "__main__":
    main()
