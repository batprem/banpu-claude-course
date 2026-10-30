#!/usr/bin/env python3
"""Sample Data Pack (core) for the Banpu Claude course — 100% synthetic.

Writes (small, committed):
  core/ops_monthly_clean.csv / .xlsx   tidy monthly production & cost, 6 fictional sites,
                                       Jan 2023–Dec 2025 (พ.ศ. 2566–2568), Budget vs Actual
  workshop_b_scattered/                the same data, deliberately scattered and inconsistent
                                       (Workshop B / Excel Detective)
  answer_key/insights.md               trainer answers: traps per file + key numbers

Usage: python3 materials/m2/data/generate_core_pack.py   (deterministic, seed 2569)
Every site, number and person is invented. Do not replace with real Banpu data.
"""
import csv
import math
import pathlib
import random
import shutil

from openpyxl import Workbook
from openpyxl.styles import Font

HERE = pathlib.Path(__file__).resolve().parent
rng = random.Random(2569)

TH_MONTH = ["ม.ค.", "ก.พ.", "มี.ค.", "เม.ย.", "พ.ค.", "มิ.ย.", "ก.ค.", "ส.ค.", "ก.ย.", "ต.ค.", "พ.ย.", "ธ.ค."]
YEARS = [2023, 2024, 2025]

# code, Thai name, English short, type, unit, base monthly volume, base unit cost (THB/unit)
SITES = [
    ("A", "เหมืองสมมติ ภูผาทอง", "PhuPhaThong", "เหมือง", "ตัน", 410_000, 1_150),
    ("B", "เหมืองสมมติ ดอยหินดำ", "DoiHinDam", "เหมือง", "ตัน", 285_000, 1_240),
    ("C", "เหมืองสมมติ ผาแดง", "PhaDaeng", "เหมือง", "ตัน", 198_000, 1_310),
    ("D", "โรงไฟฟ้าสมมติ ลำน้ำใส", "LamNamSai", "โรงไฟฟ้า", "MWh", 455_000, 2_050),
    ("E", "โรงไฟฟ้าสมมติ ทุ่งทอง", "ThungThong", "โรงไฟฟ้า", "MWh", 312_000, 2_180),
    ("F", "ฟาร์มโซลาร์สมมติ แสงตะวัน", "SaengTawan", "โซลาร์", "MWh", 9_800, 640),
]


def season(site_type, m):
    """Rainy season (Jun–Oct) slows mines; solar peaks in hot season; power follows demand."""
    if site_type == "เหมือง":
        return 0.88 if 6 <= m <= 10 else 1.04
    if site_type == "โซลาร์":
        return 1 + 0.18 * math.cos((m - 4) / 12 * 2 * math.pi)
    return 1.06 if 3 <= m <= 6 else 0.97


def build_rows():
    rows = []
    for code, th, en, typ, unit, vol0, uc0 in SITES:
        for y in YEARS:
            for m in range(1, 13):
                t = (y - 2023) * 12 + m - 1
                growth = 1 + (0.035 * t / 12 if code == "F" else 0.01 * t / 12)
                budget_vol = vol0 * season(typ, m) * growth
                actual_vol = budget_vol * rng.uniform(0.95, 1.04)
                cost_factor = rng.uniform(0.97, 1.04)
                # Story events the learners should discover
                if code == "B" and (y, m) in [(2024, 9), (2024, 10)]:
                    actual_vol = budget_vol * (0.55 if m == 9 else 0.62)   # flood
                if code == "D" and (y, m) == (2025, 3):
                    actual_vol = budget_vol * 0.35                          # planned overhaul, not in budget
                if code == "C" and y == 2025:
                    cost_factor *= 1 + 0.025 * m                            # fuel & haul cost creep
                if code == "F" and y >= 2024:
                    actual_vol *= 1.06                                      # new panels beat plan
                uc = uc0 * (1 + 0.03 * (y - 2023))
                budget_cost = budget_vol * uc / 1e6
                actual_cost = (actual_vol * uc * cost_factor + budget_vol * uc * 0.25 * (1 - actual_vol / budget_vol)) / 1e6
                rows.append({
                    "year": y, "year_be": y + 543, "month": m, "period": f"{y}-{m:02d}",
                    "site_code": code, "site_name": th, "site_type": typ, "unit": unit,
                    "budget_volume": round(budget_vol), "actual_volume": round(actual_vol),
                    "budget_cost_mthb": round(budget_cost, 2), "actual_cost_mthb": round(actual_cost, 2),
                })
    for r in rows:
        r["actual_unit_cost_thb"] = round(r["actual_cost_mthb"] * 1e6 / r["actual_volume"], 1)
    return rows


def wb_save(wb, path):
    path.parent.mkdir(parents=True, exist_ok=True)
    wb.save(path)


def write_core(rows):
    out = HERE / "core"
    out.mkdir(exist_ok=True)
    cols = list(rows[0].keys())
    with open(out / "ops_monthly_clean.csv", "w", newline="", encoding="utf-8-sig") as f:
        w = csv.DictWriter(f, fieldnames=cols)
        w.writeheader()
        w.writerows(rows)
    wb = Workbook()
    ws = wb.active
    ws.title = "monthly"
    ws.append(cols)
    for r in rows:
        ws.append([r[c] for c in cols])
    ws2 = wb.create_sheet("sites")
    ws2.append(["site_code", "site_name", "english_short", "site_type", "unit"])
    for s in SITES:
        ws2.append(list(s[:5]))
    ws3 = wb.create_sheet("README")
    ws3.append(["ข้อมูลจำลองทั้งหมด (synthetic) สำหรับหลักสูตร Claude for Business — ไม่ใช่ข้อมูลจริงของบ้านปู"])
    wb_save(wb, out / "ops_monthly_clean.xlsx")


def by_site(rows, code):
    return [r for r in rows if r["site_code"] == code]


def write_scattered(rows):
    d = HERE / "workshop_b_scattered"
    if d.exists():
        shutil.rmtree(d)
    d.mkdir()

    # A: one file per Thai year, Thai headers, Thai month text, actuals only, million THB
    a = by_site(rows, "A")
    for y in YEARS:
        wb = Workbook()
        ws = wb.active
        ws.title = "ผลผลิต"
        ws.append(["เดือน", "ผลผลิตจริง (ตัน)", "ต้นทุนจริง (ล้านบาท)"])
        for r in [r for r in a if r["year"] == y]:
            ws.append([f"{TH_MONTH[r['month'] - 1]} {r['year_be']}", r["actual_volume"], r["actual_cost_mthb"]])
        name = f"SiteA_ภูผาทอง_{y + 543}.xlsx" if y < 2025 else f"SiteA_ภูผาทอง_{y + 543}_final_v2.xlsx"
        wb_save(wb, d / name)
        if y == 2025:   # trap: older "final" missing Dec and with a different Nov figure
            ws.delete_rows(ws.max_row)
            ws.cell(row=ws.max_row, column=2).value = round(ws.cell(row=ws.max_row, column=2).value * 0.9)
            wb_save(wb, d / f"SiteA_ภูผาทอง_{y + 543}_final.xlsx")

    # B: English headers, title rows above the header, cost in THB (not million)
    wb = Workbook()
    ws = wb.active
    ws.title = "Monthly"
    ws.append(["DoiHinDam site – monthly production report"])
    ws["A1"].font = Font(bold=True, size=14)
    ws.append(["Prepared by: สมชาย ใจดีสมมติ (somchai.j@example.com)"])
    ws.append([])
    ws.append(["Month", "Output_t", "Cost_THB", "Remark"])
    for r in by_site(rows, "B"):
        remark = "น้ำท่วมถนนขนส่ง" if (r["year"], r["month"]) in [(2024, 9), (2024, 10)] else ""
        ws.append([f"{r['period']}-01", r["actual_volume"], round(r["actual_cost_mthb"] * 1e6), remark])
    wb_save(wb, d / "DoiHinDam_Production_2023-2025.xlsx")

    # C: wide format, one sheet per year, metrics as rows, Nov 2024 missing
    wb = Workbook()
    wb.remove(wb.active)
    c = by_site(rows, "C")
    for y in YEARS:
        ws = wb.create_sheet(str(y))
        yr = [r for r in c if r["year"] == y]
        ws.append(["ตัวชี้วัด"] + [f"{r['month']:02d}/{y}" for r in yr])
        ws.append(["ผลผลิต (ตัน)"] + [None if (y, r["month"]) == (2024, 11) else r["actual_volume"] for r in yr])
        ws.append(["ต้นทุน (ล้านบาท)"] + [None if (y, r["month"]) == (2024, 11) else r["actual_cost_mthb"] for r in yr])
    wb_save(wb, d / "ผาแดง รายงานรายเดือน.xlsx")

    # D: GWh + thousand THB, Buddhist-year period text
    wb = Workbook()
    ws = wb.active
    ws.title = "gen"
    ws.append(["period_BE", "Net_Generation_GWh", "Cost_kTHB"])
    for r in by_site(rows, "D"):
        ws.append([f"{r['year_be']}-{r['month']:02d}", round(r["actual_volume"] / 1000, 3), round(r["actual_cost_mthb"] * 1000, 1)])
    wb_save(wb, d / "LNS_power_monthly.xlsx")
    shutil.copy(d / "LNS_power_monthly.xlsx", d / "Copy of LNS_power_monthly.xlsx")

    # E: semicolon CSV, dd/mm/yyyy, thousands separators, inconsistent site names
    with open(d / "ทุ่งทอง_gen_cost.csv", "w", newline="", encoding="utf-8-sig") as f:
        w = csv.writer(f, delimiter=";")
        w.writerow(["วันที่", "ไซต์", "พลังงานสุทธิ (MWh)", "ต้นทุน (ล้านบาท)"])
        for i, r in enumerate(by_site(rows, "E")):
            name = ["ทุ่งทอง", "Site E", "ทุ่งทอง ", "โรงไฟฟ้าทุ่งทอง"][i % 4]
            w.writerow([f"01/{r['month']:02d}/{r['year']}", name, f"{r['actual_volume']:,}", r["actual_cost_mthb"]])

    # F: clean but includes budget columns too (only site that does)
    wb = Workbook()
    ws = wb.active
    ws.title = "solar"
    ws.append(["Year", "Month", "Budget_MWh", "Actual_MWh", "Budget_Cost_MTHB", "Actual_Cost_MTHB"])
    for r in by_site(rows, "F"):
        ws.append([r["year"], r["month"], r["budget_volume"], r["actual_volume"], r["budget_cost_mthb"], r["actual_cost_mthb"]])
    wb_save(wb, d / "solar_F_2023_2025.xlsx")

    # Budget for all sites: one sheet per Thai year, wide by month, codes differ from file names
    wb = Workbook()
    wb.remove(wb.active)
    ws = wb.create_sheet("รหัสไซต์")
    ws.append(["รหัส", "ชื่อไซต์", "ชื่อย่อในไฟล์อื่น", "หน่วย"])
    for code, th, en, typ, unit, *_ in SITES:
        ws.append([f"Site {code}", th, en, unit])
    for y in YEARS:
        for metric, key in [("ปริมาณ", "budget_volume"), ("ต้นทุน ล้านบาท", "budget_cost_mthb")]:
            ws = wb.create_sheet(f"{metric} {y + 543}")
            ws.append(["ไซต์"] + TH_MONTH)
            for code, *_ in SITES:
                ws.append([f"Site {code}"] + [r[key] for r in rows if r["site_code"] == code and r["year"] == y])
    wb_save(wb, d / "Budget_FY2566-2568_ทุกไซต์.xlsx")

    # Distractors
    old = d / "เก่า_ไม่ใช้"
    old.mkdir()
    wb = Workbook()
    ws = wb.active
    ws.append(["เดือน", "ผลผลิตจริง (ตัน)", "ต้นทุนจริง (ล้านบาท)"])
    for m in range(1, 13):
        ws.append([f"{TH_MONTH[m - 1]} 2565", rng.randint(360_000, 420_000), round(rng.uniform(400, 470), 2)])
    wb_save(wb, old / "SiteA_2565.xlsx")
    (d / "อ่านก่อน.txt").write_text(
        "โฟลเดอร์นี้รวบรวมไฟล์รายงานไซต์ที่ส่งมาทางอีเมลช่วงปี 2566–2568 (ข้อมูลจำลอง)\n"
        "ผู้รวบรวม: วิไลวรรณ สมมติ (wilaiwan.s@example.com)\n"
        "หมายเหตุ: แต่ละไซต์ใช้รูปแบบไฟล์ของตัวเอง ยังไม่มีใครรวมให้\n", encoding="utf-8")


def write_answer_key(rows):
    out = HERE / "answer_key"
    out.mkdir(exist_ok=True)
    lines = ["# Answer key — Workshop B / Excel Detective (trainer only)", "",
             "สร้างโดย `generate_core_pack.py` (seed 2569). ข้อมูลจำลองทั้งหมด", "",
             "## กับดักในแต่ละไฟล์", "",
             "| ไฟล์ | กับดัก |", "|---|---|",
             "| SiteA_ภูผาทอง_2566/2567.xlsx, _2568_final_v2.xlsx | เดือนเป็นข้อความไทย (ม.ค. 2566), แยกไฟล์รายปี, ไม่มี budget |",
             "| SiteA_ภูผาทอง_2568_final.xlsx | เวอร์ชันเก่า: ไม่มี ธ.ค. และ พ.ย. ต่างจาก v2 → ต้องใช้ final_v2 |",
             "| DoiHinDam_Production_2023-2025.xlsx | header อยู่แถว 4, ต้นทุนเป็นบาท (ไม่ใช่ล้านบาท), ชื่อไซต์ภาษาอังกฤษ |",
             "| ผาแดง รายงานรายเดือน.xlsx | แบบกว้าง (เดือนเป็นคอลัมน์), แยก sheet รายปี, พ.ย. 2024 ว่าง |",
             "| LNS_power_monthly.xlsx | หน่วย GWh และ พันบาท, ปีเป็น พ.ศ. |",
             "| Copy of LNS_power_monthly.xlsx | ไฟล์ซ้ำ ห้ามนับสองครั้ง |",
             "| ทุ่งทอง_gen_cost.csv | ตัวคั่น `;`, วันที่ dd/mm/yyyy, ตัวเลขมีคอมมา, ชื่อไซต์ 4 แบบ |",
             "| solar_F_2023_2025.xlsx | ไฟล์เดียวที่มี budget ในตัว (ใช้เทียบกับไฟล์ Budget ได้) |",
             "| Budget_FY2566-2568_ทุกไซต์.xlsx | sheet ต่อปีต่อ metric, ใช้รหัส Site A–F, มี sheet รหัสไซต์ไว้ map ชื่อ |",
             "| เก่า_ไม่ใช้/SiteA_2565.xlsx | นอกช่วงเวลา (ปี 2565) ไม่ใช้ |", "",
             "ไฟล์ข้อมูลที่ต้องใช้: 9 ไฟล์ (A×3, B, C, D, E, F, Budget) · ไฟล์ที่ต้องตัดทิ้ง: 3 (A_2568_final, Copy of LNS, SiteA_2565) · ทั้งหมด 13 ไฟล์ (รวม อ่านก่อน.txt)", "",
             "## ตัวเลขสำคัญ (Actual vs Budget)", "",
             "| ไซต์ | ปี | Budget ปริมาณ | Actual ปริมาณ | ส่วนต่าง % | Budget ต้นทุน (ลบ.) | Actual ต้นทุน (ลบ.) | ต้นทุนต่อหน่วยจริง (บาท) |",
             "|---|---|---|---|---|---|---|---|"]
    summary = {}
    for code, th, *_ in SITES:
        for y in YEARS:
            rr = [r for r in rows if r["site_code"] == code and r["year"] == y]
            bv = sum(r["budget_volume"] for r in rr)
            av = sum(r["actual_volume"] for r in rr)
            bc = sum(r["budget_cost_mthb"] for r in rr)
            ac = sum(r["actual_cost_mthb"] for r in rr)
            summary[(code, y)] = (bv, av, bc, ac)
            lines.append(f"| {code} {th} | {y + 543} | {bv:,} | {av:,} | {100 * (av - bv) / bv:+.1f}% | {bc:,.1f} | {ac:,.1f} | {ac * 1e6 / av:,.0f} |")
    worst = min(((c, y) for c, *_ in SITES for y in YEARS),
                key=lambda k: (summary[k][1] - summary[k][0]) / summary[k][0])
    c25 = [r for r in rows if r["site_code"] == "C" and r["year"] == 2025]
    lines += ["", "## Insight ที่ควรค้นเจอ", "",
              f"1. ปริมาณต่ำกว่างบมากที่สุด: Site {worst[0]} ปี {worst[1] + 543} "
              f"({100 * (summary[worst][1] - summary[worst][0]) / summary[worst][0]:+.1f}%) — ก.ย.–ต.ค. 2567 น้ำท่วมถนนขนส่ง (ดู Remark ในไฟล์ B)",
              f"2. Site C ต้นทุนต่อหน่วยปี 2568 ไต่ขึ้นทุกเดือน: ม.ค. {c25[0]['actual_unit_cost_thb']:,.0f} → ธ.ค. {c25[-1]['actual_unit_cost_thb']:,.0f} บาท/ตัน",
              "3. Site D มี.ค. 2568 ผลิตไฟฟ้าได้ ~35% ของแผน (overhaul ที่ไม่ได้ใส่ใน budget)",
              f"4. Site F ผลิตเกินแผนต่อเนื่องตั้งแต่ปี 2567 (2567: {100 * (summary[('F', 2024)][1] - summary[('F', 2024)][0]) / summary[('F', 2024)][0]:+.1f}%)",
              "5. ข้อมูลที่หายไป: Site C พ.ย. 2567 (ต้องแจ้ง ไม่ใช่เดาเติม)"]
    (out / "insights.md").write_text("\n".join(lines) + "\n", encoding="utf-8")
    return worst, summary


if __name__ == "__main__":
    rows = build_rows()
    write_core(rows)
    write_scattered(rows)
    worst, _ = write_answer_key(rows)
    print(f"{len(rows)} rows · worst variance: Site {worst[0]} {worst[1] + 543}")
    print("files:", sorted(p.name for p in (HERE / "workshop_b_scattered").rglob("*") if p.is_file()))
