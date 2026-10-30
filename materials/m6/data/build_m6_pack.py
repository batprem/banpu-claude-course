#!/usr/bin/env python3
"""Assemble the M6 learner pack (workshop route B = local folder).

Output: materials/m6/data/out/M6_pack/  (+ M6_pack.zip) — gitignored, rebuild any time.
  input/m3_outlook/*.eml        read-only COPY of materials/m3/data/pack/outlook (20 emails)
  input/m3_sharepoint/*.csv     read-only COPY of Project_Tracker.csv + Issue_Log.csv from M3
  input/meeting_notes/*.md      6 synthetic meeting notes (from gen_m6_data.py)
  input/watchlist.md, input/news_fallback.md
  output/                       empty — the only place a scheduled task may write
Learners copy M6_pack/ to Documents/Claude-Workshop/M6/ (copy-before-write).
If a learner has a report from M4 (Documents/Claude-Workshop/M4/output/), they copy it into input/m4_report/ themselves.

Run: python3 materials/m6/data/gen_m6_data.py && python3 materials/m6/data/build_m6_pack.py
"""
import pathlib
import shutil

HERE = pathlib.Path(__file__).resolve().parent
M3 = HERE.parents[1] / "m3" / "data" / "pack"
PACK = HERE / "pack"
OUT = HERE / "out" / "M6_pack"


def main():
    if OUT.exists():
        shutil.rmtree(OUT)
    inp = OUT / "input"
    shutil.copytree(M3 / "outlook", inp / "m3_outlook", ignore=shutil.ignore_patterns("mailbox_index.csv"))
    (inp / "m3_sharepoint").mkdir(parents=True)
    for name in ("Project_Tracker.csv", "Issue_Log.csv"):
        shutil.copy2(M3 / "sharepoint" / name, inp / "m3_sharepoint" / name)
    shutil.copytree(PACK / "meeting_notes", inp / "meeting_notes")
    for name in ("watchlist.md", "news_fallback.md"):
        shutil.copy2(PACK / name, inp / name)
    (inp / "m4_report").mkdir()
    (inp / "m4_report" / "README.txt").write_text(
        "วางรายงานที่ทำเสร็จใน M4 ไว้ที่นี่ (ถ้ามี) · ไม่มีก็ข้ามได้\n", encoding="utf-8")
    (OUT / "output").mkdir()
    (OUT / "output" / ".keep").write_text("", encoding="utf-8")
    (OUT / "อ่านก่อน.txt").write_text(
        "M6 pack · ข้อมูลสมมติทั้งหมด\n"
        "1) คัดลอกทั้งโฟลเดอร์ไปที่ Documents/Claude-Workshop/M6/\n"
        "2) Scheduled task อ่านได้เฉพาะ input/ และเขียนได้เฉพาะ output/\n"
        "3) task ที่ใช้โฟลเดอร์ในเครื่อง รันเฉพาะตอนเครื่องเปิดและ Claude Desktop เปิดอยู่\n",
        encoding="utf-8")
    zip_path = shutil.make_archive(str(OUT), "zip", OUT.parent, OUT.name)
    n = sum(1 for p in OUT.rglob("*") if p.is_file())
    print(f"wrote {n} files → {OUT} and {zip_path}")


if __name__ == "__main__":
    main()
