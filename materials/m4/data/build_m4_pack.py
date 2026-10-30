#!/usr/bin/env python3
"""Assemble the learner "M4 pack" (upload to the training SharePoint site; learners copy it to
Documents/Claude-Workshop/M4/input/). Reads M2/M3 data read-only. Output: data/out/M4_pack/input/ (gitignored).

Run gen_m4_data.py first. Usage: python3 materials/m4/data/build_m4_pack.py
"""
import pathlib
import shutil

HERE = pathlib.Path(__file__).resolve().parent
M3 = HERE.parent.parent / "m3" / "data" / "pack"
DST = HERE / "out" / "M4_pack" / "input"


def main():
    if DST.exists():
        shutil.rmtree(DST)
    DST.mkdir(parents=True)
    for f in ["ops_monthly_2566-2569.xlsx", "energy_prices_public_2023-2026.csv"]:
        shutil.copy2(HERE / f, DST / f)
    for f in ["shift_log_2568-2569.csv", "Monthly_Ops_Report_2569-09_FULL.docx"]:
        shutil.copy2(HERE / "out" / f, DST / f)
    shutil.copytree(M3 / "sharepoint", DST / "m3_sharepoint",
                    ignore=shutil.ignore_patterns("*.xlsx"))  # Capex tracker is M3-only
    shutil.copytree(M3 / "outlook", DST / "m3_outlook")
    total = sum(p.stat().st_size for p in DST.rglob("*") if p.is_file())
    print(f"{DST}: {sum(1 for p in DST.rglob('*') if p.is_file())} files, {total / 1e6:.1f} MB")


if __name__ == "__main__":
    main()
