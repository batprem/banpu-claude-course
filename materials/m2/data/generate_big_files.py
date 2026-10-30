#!/usr/bin/env python3
"""Real-volume files for the "limits & workarounds" lesson (gitignored outputs, 100% synthetic).

  out/production_shift_log_2566-2568.csv   ~200,000 rows (3 mines × 1,096 days × 3 shifts × 20 trucks)
  out/annual_review_synthetic_320p.pdf     320-page English "annual review" of a fictional company,
                                           with a few planted facts (see FACTS below) for retrieval tests

Usage: python3 materials/m2/data/generate_big_files.py [--csv-only | --pdf-only]
"""
import csv
import datetime as dt
import pathlib
import random
import sys

HERE = pathlib.Path(__file__).resolve().parent
OUT = HERE / "out"
rng = random.Random(200_000)

MINES = [("A", "PhuPhaThong"), ("B", "DoiHinDam"), ("C", "PhaDaeng")]
FACTS = {  # page -> sentence; use these to check whether Claude really read the right section
    47: "Clause 9.3: the fictional supplier pays a late-delivery penalty of 0.15% of the shipment value per day, capped at 10%.",
    188: "The PhaDaeng haul road was resurfaced in May 2025 at a cost of 46.2 million THB (fictional).",
    301: "Board note: the fictional company targets a 12% cut in diesel use per tonne by 2570.",
}


def write_csv():
    path = OUT / "production_shift_log_2566-2568.csv"
    start = dt.date(2023, 1, 1)
    n = 0
    with open(path, "w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        w.writerow(["date", "site_code", "site", "shift", "truck_id", "material", "loads", "tonnes",
                    "diesel_l", "downtime_min", "operator_id"])
        for d in range(1096):
            day = start + dt.timedelta(days=d)
            rain = 6 <= day.month <= 10
            for code, site in MINES:
                for shift in ("D", "N", "G"):
                    for t in range(1, 21):
                        loads = max(0, int(rng.gauss(14 if not rain else 11, 3)))
                        tonnes = round(loads * rng.uniform(88, 96), 1)
                        down = rng.choice([0, 0, 0, 0, 15, 30, 45, 90]) + (60 if rain and rng.random() < .2 else 0)
                        w.writerow([day.isoformat(), code, site, shift, f"{code}-HT{t:02d}",
                                    "coal" if rng.random() < .8 else "overburden", loads, tonnes,
                                    round(tonnes * rng.uniform(0.9, 1.3), 1), down, f"OP{rng.randint(1000, 1999)}"])
                        n += 1
    print(f"{path}: {n:,} rows, {path.stat().st_size / 1e6:.1f} MB")


def pdf_text(s):
    return s.replace("\\", "\\\\").replace("(", "\\(").replace(")", "\\)")


def write_pdf(pages=320):
    path = OUT / "annual_review_synthetic_320p.pdf"
    chapters = ["Chair's letter", "Market review: thermal coal", "Market review: power", "Supplier contracts",
                "Operations: mines", "Operations: power plants", "Renewables", "Safety", "Environment",
                "People", "Financial statements (fictional)", "Notes to accounts", "Appendix"]
    contents = []
    for p in range(1, pages + 1):
        ch = chapters[min(len(chapters) - 1, (p - 1) * len(chapters) // pages)]
        lines = [f"Fictional Energy Co. (synthetic) - Annual Review 2568 - page {p}", f"Chapter: {ch}", ""]
        if p == 1:
            lines += ["THIS DOCUMENT IS SYNTHETIC TRAINING DATA. No real company, site or figure."]
        for i in range(38):
            if p in FACTS and i == 20:
                lines.append(FACTS[p])
            else:
                a, b = rng.randint(100, 9999), round(rng.uniform(-9, 12), 1)
                lines.append(f"{ch} item {i + 1}: indicator {a:,} units, change {b:+.1f}% versus prior year; "
                             f"see note {rng.randint(1, 40)}.")
        y = 800
        ops = ["BT /F1 9 Tf"]
        for k, line in enumerate(lines):
            size = 13 if k < 2 else 9
            ops.append(f"/F1 {size} Tf 1 0 0 1 50 {y} Tm ({pdf_text(line)}) Tj")
            y -= 19 if k < 2 else 18.5
        ops.append("ET")
        contents.append("\n".join(ops).encode("latin-1"))

    objs = {1: b"<< /Type /Catalog /Pages 2 0 R >>", 3: b"<< /Type /Font /Subtype /Type1 /BaseFont /Helvetica >>"}
    kids = []
    for i, c in enumerate(contents):
        page_id, content_id = 4 + 2 * i, 5 + 2 * i
        kids.append(f"{page_id} 0 R")
        objs[page_id] = (f"<< /Type /Page /Parent 2 0 R /MediaBox [0 0 595 842] "
                         f"/Resources << /Font << /F1 3 0 R >> >> /Contents {content_id} 0 R >>").encode()
        objs[content_id] = b"<< /Length %d >>\nstream\n" % len(c) + c + b"\nendstream"
    objs[2] = f"<< /Type /Pages /Kids [{' '.join(kids)}] /Count {len(kids)} >>".encode()
    out, offs = bytearray(b"%PDF-1.4\n"), {}
    for i in sorted(objs):
        offs[i] = len(out)
        out += b"%d 0 obj\n" % i + objs[i] + b"\nendobj\n"
    xref, size = len(out), max(objs) + 1
    out += b"xref\n0 %d\n0000000000 65535 f \n" % size
    out += b"".join(b"%010d 00000 n \n" % offs[i] for i in range(1, size))
    out += b"trailer\n<< /Size %d /Root 1 0 R >>\nstartxref\n%d\n%%%%EOF\n" % (size, xref)
    path.write_bytes(out)
    print(f"{path}: {pages} pages, {path.stat().st_size / 1e6:.1f} MB · planted facts on pages {sorted(FACTS)}")


if __name__ == "__main__":
    OUT.mkdir(exist_ok=True)
    if "--pdf-only" not in sys.argv:
        write_csv()
    if "--csv-only" not in sys.argv:
        write_pdf()
