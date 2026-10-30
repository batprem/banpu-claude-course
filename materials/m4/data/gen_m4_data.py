#!/usr/bin/env python3
"""Synthetic data for M4 Document Factory (100% fictional; seed 2569).

Reuses M2/M3 data read-only and adds only what M4 is missing:

  ops_monthly_2566-2569.xlsx         Excel (source 1) = M2 core history 2566–2568 + new Jan–Sep 2569
  out/shift_log_2568-2569.csv        CSV  (source 2) ~172,000 rows, ~11 MB (gitignored)
  out/Monthly_Ops_Report_2569-09_FULL.docx   ~40 MB report with 14 "site photos" (gitignored)
                                     → the "too big to attach to email" exercise
  dashboard_data.json                numbers for the Monthly Ops Dashboard Artifact (sync_dashboard.py)

Sources 3–4 come from M3 (SharePoint List: Project_Tracker/Issue_Log · Outlook: 20 .eml).
Source 5 = energy_prices_public_2023-2026.csv (real public data, fetch_energy_prices.py).

Planted story for September 2569 (answer key: answer_key.md):
  Site D  generation ~−17% vs budget (Unit 2 boiler overhaul, PRJ-105 in M3)
  Site C  unit cost ~+15% vs budget (excavator EX-07 down, PRJ-112)
  Site B  rain: downtime up, truck B-HT07 the worst in the shift log
Usage: python3 materials/m4/data/gen_m4_data.py [--no-big]
"""
import csv
import datetime as dt
import io
import json
import pathlib
import random
import sys

from openpyxl import Workbook
from openpyxl.styles import Font, PatternFill

HERE = pathlib.Path(__file__).resolve().parent
M2_CORE = HERE.parent.parent / "m2" / "data" / "core" / "ops_monthly_clean.csv"
M3_SP = HERE.parent.parent / "m3" / "data" / "pack" / "sharepoint"
OUT = HERE / "out"
rng = random.Random(2569)

# month -> site -> (volume factor vs budget, cost factor vs budget)
SHOCKS = {
    8: {"D": (0.90, 0.97)},
    9: {"D": (0.82, 0.96), "C": (0.95, 1.07), "B": (0.93, 0.99)},
}


def load_history():
    with open(M2_CORE, encoding="utf-8-sig") as f:
        return list(csv.DictReader(f))


def make_2569(hist):
    rows = []
    for code in "ABCDEF":
        h = [r for r in hist if r["site_code"] == code]
        for m in range(1, 10):
            base = next(r for r in h if r["year"] == "2025" and int(r["month"]) == m)
            bv = round(float(base["budget_volume"]) * rng.uniform(1.01, 1.03))
            bc = round(float(base["budget_cost_mthb"]) * rng.uniform(1.03, 1.05), 2)
            fv, fc = SHOCKS.get(m, {}).get(code, (1.0, 1.0))
            av = round(bv * fv * rng.uniform(0.975, 1.02))
            ac = round(bc * fc * rng.uniform(0.98, 1.025), 2)
            rows.append({**{k: base[k] for k in ("site_code", "site_name", "site_type", "unit")},
                         "year": "2026", "year_be": "2569", "month": str(m), "period": f"2026-{m:02d}",
                         "budget_volume": bv, "actual_volume": av, "budget_cost_mthb": bc,
                         "actual_cost_mthb": ac, "actual_unit_cost_thb": round(ac * 1e6 / av, 1)})
    return rows


COLS = ["year", "year_be", "month", "period", "site_code", "site_name", "site_type", "unit",
        "budget_volume", "actual_volume", "budget_cost_mthb", "actual_cost_mthb", "actual_unit_cost_thb"]


def write_xlsx(rows):
    wb = Workbook()
    ws = wb.active
    ws.title = "data"
    ws.append(COLS)
    for c in ws[1]:
        c.font = Font(bold=True, color="FFFFFF")
        c.fill = PatternFill("solid", fgColor="3BA55C")
    for r in rows:
        ws.append([float(r[c]) if c in COLS[8:] else (int(r[c]) if c in ("year", "year_be", "month") else r[c])
                   for c in COLS])
    ws.freeze_panes = "A2"
    rd = wb.create_sheet("readme")
    for line in ["ข้อมูลสมมติทั้งหมด (synthetic) สำหรับ M4 Document Factory — ไม่ใช่ข้อมูลจริงของบริษัทใด",
                 "แหล่ง: ระบบรายงานปฏิบัติการ (สมมติ) · 6 ไซต์ · ม.ค. 2566 – ก.ย. 2569",
                 "หน่วย: volume = ตัน (เหมือง) / MWh (โรงไฟฟ้า, โซลาร์) · cost = ล้านบาท · unit cost = บาท/หน่วย",
                 "เจ้าของข้อมูล (สมมติ): ทีม Operations Excellence · ops-excellence@example.com"]:
        rd.append([line])
    path = HERE / "ops_monthly_2566-2569.xlsx"
    wb.save(path)
    print(f"{path.name}: {len(rows)} rows")


MINES = [("A", "PhuPhaThong"), ("B", "DoiHinDam"), ("C", "PhaDaeng")]


def write_shift_log():
    """Same schema as M2's production_shift_log (so prompts transfer), Jan 2568 – Sep 2569."""
    OUT.mkdir(exist_ok=True)
    path = OUT / "shift_log_2568-2569.csv"
    start, end = dt.date(2025, 1, 1), dt.date(2026, 9, 30)
    n, sep = 0, {}
    with open(path, "w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        w.writerow(["date", "site_code", "site", "shift", "truck_id", "material", "loads", "tonnes",
                    "diesel_l", "downtime_min", "operator_id"])
        day = start
        while day <= end:
            rain = 6 <= day.month <= 10
            heavy = day.year == 2026 and day.month == 9
            for code, site in MINES:
                for shift in ("D", "N", "G"):
                    for t in range(1, 31):
                        truck = f"{code}-HT{t:02d}"
                        loads = max(0, int(rng.gauss(14 if not rain else 11, 3)))
                        down = rng.choice([0, 0, 0, 0, 15, 30, 45, 90]) + (60 if rain and rng.random() < .2 else 0)
                        if heavy and code == "B":
                            down += rng.choice([0, 30, 60, 90])
                            loads = max(0, loads - 2)
                        if heavy and truck == "B-HT07":
                            down += 180
                            loads = max(0, loads - 6)
                        if heavy and code == "C" and t in (11, 12, 13):  # trucks idle behind EX-07
                            loads = max(0, loads - 4)
                            down += 60
                        tonnes = round(loads * rng.uniform(88, 96), 1)
                        diesel = round(tonnes * rng.uniform(0.9, 1.3), 1)
                        row_mat = "coal" if rng.random() < .15 else "overburden"  # strip ratio ~6:1
                        w.writerow([day.isoformat(), code, site, shift, truck, row_mat, loads, tonnes,
                                    diesel, down, f"OP{rng.randint(1000, 1999)}"])
                        n += 1
                        if day.year == 2026 and day.month == 9:
                            s = sep.setdefault(code, {"tonnes": 0, "diesel": 0, "down": 0, "trucks": {}})
                            s["tonnes"] += tonnes
                            s["coal"] = s.get("coal", 0) + (tonnes if row_mat == "coal" else 0)
                            s["diesel"] += diesel
                            s["down"] += down
                            s["trucks"][truck] = s["trucks"].get(truck, 0) + down
            day += dt.timedelta(days=1)
    print(f"{path.name}: {n:,} rows, {path.stat().st_size / 1e6:.1f} MB")
    return {c: {"tonnes": round(s["tonnes"]), "coal_t": round(s["coal"]), "diesel_l_per_t": round(s["diesel"] / s["tonnes"], 3),
                "downtime_h": round(s["down"] / 60), "worst_truck": max(s["trucks"], key=s["trucks"].get),
                "worst_truck_h": round(max(s["trucks"].values()) / 60)} for c, s in sep.items()}


def fake_photo(i):
    """A 'site photo' made of noise + gradient: realistic JPEG-less PNG weight (~2.8 MB each)."""
    from PIL import Image
    w, h = 1200, 850
    img = Image.effect_noise((w, h), 60).convert("RGB")
    tint = Image.new("RGB", (w, h), (90 + i * 4 % 120, 110, 80 + i * 7 % 100))
    img = Image.blend(img, tint, 0.45)
    buf = io.BytesIO()
    img.save(buf, "PNG")
    buf.seek(0)
    return buf


def write_big_docx(n_photos=14):
    from docx import Document
    from docx.shared import Cm
    doc = Document()
    doc.add_heading("Monthly Operations Report · กันยายน 2569 (ฉบับเต็ม · ข้อมูลสมมติ)", 0)
    doc.add_paragraph("ฉบับนี้ตั้งใจให้ใหญ่เกินแนบอีเมล ใช้ฝึก workaround ใน M4 · ภาพทั้งหมดเป็นภาพสังเคราะห์")
    for i in range(n_photos):
        site = "ABCDEF"[i % 6]
        doc.add_heading(f"ภาพหน้างาน {i + 1:02d} · Site {site} (ภาพสังเคราะห์)", 2)
        doc.add_picture(fake_photo(i), width=Cm(16))
        doc.add_paragraph(f"คำบรรยายภาพ {i + 1}: บันทึกสภาพพื้นที่ประจำเดือน (สมมติ)")
    path = OUT / "Monthly_Ops_Report_2569-09_FULL.docx"
    doc.save(path)
    print(f"{path.name}: {path.stat().st_size / 1e6:.1f} MB")
    return round(path.stat().st_size / 1e6, 1)


def pct(a, b):
    return round((a / b - 1) * 100, 1)


def dashboard_data(rows, shift, big_mb):
    sites = []
    for code in "ABCDEF":
        r = [x for x in rows if x["site_code"] == code]
        sep = next(x for x in r if x["month"] == "9")
        ytd = lambda k: sum(float(x[k]) for x in r)
        bu = sep["budget_cost_mthb"] * 1e6 / sep["budget_volume"]
        sites.append({
            "code": code, "name": sep["site_name"], "type": sep["site_type"], "unit": sep["unit"],
            "sep": {"bv": sep["budget_volume"], "av": sep["actual_volume"], "vol_var": pct(sep["actual_volume"], sep["budget_volume"]),
                    "bc": sep["budget_cost_mthb"], "ac": sep["actual_cost_mthb"],
                    "unit_cost": sep["actual_unit_cost_thb"], "unit_cost_var": pct(sep["actual_unit_cost_thb"], bu)},
            "ytd": {"bv": round(ytd("budget_volume")), "av": round(ytd("actual_volume")),
                    "vol_var": pct(ytd("actual_volume"), ytd("budget_volume")),
                    "bc": round(ytd("budget_cost_mthb"), 1), "ac": round(ytd("actual_cost_mthb"), 1)},
            "trend": [pct(x["actual_volume"], x["budget_volume"]) for x in r],
            "shift": shift.get(code),
        })
    with open(HERE / "energy_prices_public_2023-2026.csv", encoding="utf-8") as f:
        prices = list(csv.DictReader(f))[-12:]
    with open(M3_SP / "Project_Tracker.csv", encoding="utf-8-sig") as f:
        projects = [{k: p[k] for k in ("ProjectID", "Title", "Site", "Budget_MTHB", "Spent_MTHB", "DueDate", "Status", "PercentComplete")}
                    for p in csv.DictReader(f)]
    with open(M3_SP / "Issue_Log.csv", encoding="utf-8-sig") as f:
        issues = [i for i in csv.DictReader(f) if i["Status"] != "Closed"]
    sev = {s: sum(1 for i in issues if i["Severity"] == s) for s in ("High", "Medium", "Low")}
    data = {
        "title": "Monthly Operations Report · กันยายน 2569", "as_of": "2026-10-24",
        "note": "ข้อมูลสมมติทั้งหมด (ยกเว้นราคาพลังงานสาธารณะ: IMF via FRED)",
        "sites": sites, "prices": prices, "projects": projects, "open_issues": sev,
        "big_report_mb": big_mb,
        "sources": [
            ["Excel", "ops_monthly_2566-2569.xlsx", "ภายใน"],
            ["CSV", "shift_log_2568-2569.csv (~172,000 แถว)", "ภายใน"],
            ["SharePoint List", "Project_Tracker · Issue_Log (M3)", "ภายใน"],
            ["Outlook", "อีเมลอัปเดตโครงการ 20 ฉบับ (M3)", "ภายใน"],
            ["Web/CSV", "energy_prices_public_2023-2026.csv (IMF via FRED)", "ภายนอก สาธารณะ"],
        ],
    }
    (HERE / "dashboard_data.json").write_text(json.dumps(data, ensure_ascii=False, indent=1), encoding="utf-8")
    print("dashboard_data.json written")
    return data


def main():
    hist = load_history()
    new = make_2569(hist)
    write_xlsx(hist + new)
    shift = write_shift_log()
    big_path = OUT / "Monthly_Ops_Report_2569-09_FULL.docx"
    if "--no-big" in sys.argv and big_path.exists():
        big = round(big_path.stat().st_size / 1e6, 1)
    else:
        big = write_big_docx()
    d = dashboard_data(new, shift, big)
    for s in d["sites"]:
        print(s["code"], s["sep"]["vol_var"], s["sep"]["unit_cost_var"], s["shift"])


if __name__ == "__main__":
    main()
