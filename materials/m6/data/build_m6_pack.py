#!/usr/bin/env python3
"""Assemble the M6 learner pack (workshop route B = local folder).

Output: materials/m6/data/pack/ (committed, so it is in the repo ZIP learners download:
banpu-claude-course-master/materials/m6/data/pack/ = the Cowork folder for route B).
  input/m3_outlook/*.eml        read-only COPY of materials/m3/data/pack/outlook (20 emails)
  input/m3_sharepoint/*.csv     read-only COPY of Project_Tracker.csv + Issue_Log.csv from M3
  input/meeting_notes/*.md      6 synthetic meeting notes (written here by gen_m6_data.py)
  input/watchlist.md, input/news_fallback.md   (written here by gen_m6_data.py)
  output/                       the only place a scheduled task may write
The repo ZIP is the original (copy-before-write): re-extract it to reset the folder.
If a learner has a report from M4 (materials/m4/data/pack/output/), they copy it into input/m4_report/ themselves.

Run: python3 materials/m6/data/gen_m6_data.py && python3 materials/m6/data/build_m6_pack.py
"""
import pathlib
import shutil

HERE = pathlib.Path(__file__).resolve().parent
M3 = HERE.parents[1] / "m3" / "data" / "pack"
OUT = HERE / "pack"


def main():
    inp = OUT / "input"
    for d in (inp / "m3_outlook", inp / "m3_sharepoint", inp / "m4_report", OUT / "output"):
        if d.exists():
            shutil.rmtree(d)
    shutil.copytree(M3 / "outlook", inp / "m3_outlook", ignore=shutil.ignore_patterns("mailbox_index.csv"))
    (inp / "m3_sharepoint").mkdir(parents=True)
    for name in ("Project_Tracker.csv", "Issue_Log.csv"):
        shutil.copy2(M3 / "sharepoint" / name, inp / "m3_sharepoint" / name)
    (inp / "m4_report").mkdir()
    (inp / "m4_report" / "README.txt").write_text(
        "วางรายงานที่ทำเสร็จใน M4 ไว้ที่นี่ (ถ้ามี) · ไม่มีก็ข้ามได้\n", encoding="utf-8")
    (OUT / "output").mkdir()
    (OUT / "output" / "README.txt").write_text(
        "ผลลัพธ์ของ Workshop M6 (ร่างรายงาน · Automation Card PDF) เก็บที่นี่\n", encoding="utf-8")
    (OUT / "อ่านก่อน.txt").write_text(
        "M6 pack · ข้อมูลสมมติทั้งหมด\n"
        "1) ใน Cowork เลือกโฟลเดอร์ banpu-claude-course-master/materials/m6/data/pack (ZIP ที่ดาวน์โหลดคือต้นฉบับ)\n"
        "2) Scheduled task อ่านได้เฉพาะ input/ และเขียนได้เฉพาะ output/\n"
        "3) task ที่ใช้โฟลเดอร์ในเครื่อง รันเฉพาะตอนเครื่องเปิดและ Claude Desktop เปิดอยู่\n",
        encoding="utf-8")
    n = sum(1 for p in OUT.rglob("*") if p.is_file())
    print(f"{n} files in {OUT}")


if __name__ == "__main__":
    main()
