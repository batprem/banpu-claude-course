#!/usr/bin/env python3
"""Generate the small synthetic Excel used in the M1 demo (Chat vs Cowork → HTML dashboard).

Output: materials/m1/data/site_ops_sample.xlsx (~150 rows, < 50 KB, committed).
All sites, numbers and names are fictional. Re-run: python3 materials/m1/data/gen_site_ops.py
"""
import pathlib
import random

from openpyxl import Workbook
from openpyxl.styles import Font, PatternFill
from openpyxl.utils import get_column_letter

random.seed(2569)
OUT = pathlib.Path(__file__).with_name("site_ops_sample.xlsx")

# (site, ชื่อสมมติ, ประเภท, หน่วยผลผลิต, ผลผลิตฐาน/เดือน, ต้นทุนต่อหน่วย บาท)
SITES = [
    ("Site A", "เหมืองสมมติ ภูผาทอง", "เหมือง", "พันตัน", 820, 1450),
    ("Site B", "เหมืองสมมติ ดอยหินแก้ว", "เหมือง", "พันตัน", 610, 1520),
    ("Site C", "เหมืองสมมติ ห้วยทรายคำ", "เหมือง", "พันตัน", 450, 1610),
    ("Site D", "โรงไฟฟ้าสมมติ ลำน้ำใส", "โรงไฟฟ้า", "GWh", 390, 2100),
    ("Site E", "โรงไฟฟ้าสมมติ ทุ่งตะวัน", "โรงไฟฟ้า", "GWh", 120, 1650),
    ("Site F", "โรงไฟฟ้าสมมติ ลมเหนือ", "โรงไฟฟ้า", "GWh", 85, 1400),
]
MONTHS = [f"{y}-{m:02d}" for y in (2025, 2026) for m in range(1, 13)][:21]  # 2025-01 … 2026-09


def main():
    wb = Workbook()
    ws = wb.active
    ws.title = "Monthly"
    head = ["เดือน", "Site", "ชื่อ site (สมมติ)", "ประเภท", "หน่วย", "ผลผลิตแผน", "ผลผลิตจริง",
            "งบต้นทุน (ล้านบาท)", "ต้นทุนจริง (ล้านบาท)", "เหตุการณ์ near-miss", "หมายเหตุ"]
    ws.append(head)
    for site, name, kind, unit, base, cpu in SITES:
        for i, month in enumerate(MONTHS):
            season = 1 + 0.08 * ((i % 12) in (5, 6, 7)) * (-1 if kind == "เหมือง" else 1)
            plan = round(base * season * (1 + 0.01 * (i // 12)), 1)
            actual = round(plan * random.uniform(0.86, 1.07), 1)
            budget = round(plan * cpu / 1000, 2)
            cost = round(actual * cpu * random.uniform(0.95, 1.12) / 1000, 2)
            note = ""
            if actual < plan * 0.9:
                note = random.choice(["ฝนตกหนัก", "ซ่อมบำรุงตามแผน", "อุปกรณ์ขัดข้อง"])
            ws.append([month, site, name, kind, unit, plan, actual, budget, cost,
                       random.choice([0, 0, 0, 1, 1, 2]), note])
    for c in ws[1]:
        c.font = Font(bold=True, color="FFFFFF")
        c.fill = PatternFill("solid", fgColor="2E86AB")
    for col in range(1, len(head) + 1):
        ws.column_dimensions[get_column_letter(col)].width = 16
    ws.freeze_panes = "A2"

    info = wb.create_sheet("README")
    for row in [
        ["ไฟล์ตัวอย่างสำหรับ M1 Demo (ข้อมูลสมมติทั้งหมด)"],
        ["ห้ามใช้แทนข้อมูลจริงของบริษัท ชื่อ site และตัวเลขทั้งหมดถูกสร้างขึ้นด้วยสคริปต์"],
        ["ช่วงเวลา", f"{MONTHS[0]} ถึง {MONTHS[-1]}"],
        ["จำนวน site", len(SITES)],
    ]:
        info.append(row)
    wb.save(OUT)
    print(f"{OUT}: {ws.max_row - 1} rows")


if __name__ == "__main__":
    main()
