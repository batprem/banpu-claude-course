#!/usr/bin/env python3
"""Folder-restructure demo: ~1,500 small files from พ.ศ. 2562–2569 with messy names.

Writes out/messy_folder/ (gitignored). Files are tiny but valid (xlsx, docx, pdf, csv, txt, png)
and their modified time is set to the year they "belong" to, so Claude can reason from
names, dates, sizes and duplicates. 100% synthetic.

Usage: python3 materials/m2/data/generate_messy_folder.py [--count 1500] [--out messy_folder]
       learner sample for workshop page 6: --count 100 --out messy_folder_sample
"""
import datetime as dt
import os
import pathlib
import random
import shutil
import sys
import zipfile

from openpyxl import Workbook

HERE = pathlib.Path(__file__).resolve().parent
rng = random.Random(1500)

TH_MONTH = ["ม.ค.", "ก.พ.", "มี.ค.", "เม.ย.", "พ.ค.", "มิ.ย.", "ก.ค.", "ส.ค.", "ก.ย.", "ต.ค.", "พ.ย.", "ธ.ค."]
EN_MONTH = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
SITES = ["ภูผาทอง", "ดอยหินดำ", "ผาแดง", "ลำน้ำใส", "ทุ่งทอง", "แสงตะวัน", "SiteA", "Site B", "PDG", "LNS"]
TOPICS = [
    ("รายงานประจำเดือน", "xlsx"), ("Monthly report", "xlsx"), ("สรุปประชุม", "docx"), ("MOM", "docx"),
    ("Budget", "xlsx"), ("งบประมาณ", "xlsx"), ("ใบเสนอราคา_สมมติ", "pdf"), ("สัญญา supplier สมมติ", "pdf"),
    ("Safety inspection", "pdf"), ("ตรวจความปลอดภัย", "docx"), ("export_sap_สมมติ", "csv"), ("KPI", "xlsx"),
    ("รูปหน้างาน", "png"), ("IMG_", "png"), ("notes", "txt"), ("แผนซ่อมบำรุง", "xlsx"), ("Presentation draft", "pdf"),
]
SUFFIX = ["", "", "", "_final", "_FINAL", "_final_v2", " (1)", " (2)", "_แก้ไข", "_ล่าสุด", "_ล่าสุดจริง", "-old",
          "_v3", " - Copy", "_ส่งพี่", "_draft", "_rev1", "_ok"]
FOLDERS = ["", "", "งานเก่า", "New folder", "New folder (2)", "รวมไฟล์", "Desktop backup", "จากอีเมล",
           "ไม่รู้", "temp", "2563", "ปี64", "FY2565", "รายงาน", "Report", "ส่วนตัว_ห้ามลบ", "งานพี่ต้อมสมมติ"]


def date_text(y_be, m):
    y_ce = y_be - 543
    style = rng.randrange(7)
    return [f"{TH_MONTH[m - 1]}{str(y_be)[2:]}", f"{EN_MONTH[m - 1]} {y_ce}", f"{y_ce}{m:02d}",
            f"{m}-{y_be}", f"{rng.randint(1, 28)}-{m}-{str(y_be)[2:]}", f"{y_be}_{m:02d}",
            f"Q{(m - 1) // 3 + 1} {y_ce}"][style]


def minimal_pdf(text):
    stream = f"BT /F1 14 Tf 72 760 Td ({text}) Tj ET".encode("latin-1", "replace")
    objs = [b"<< /Type /Catalog /Pages 2 0 R >>", b"<< /Type /Pages /Kids [3 0 R] /Count 1 >>",
            b"<< /Type /Page /Parent 2 0 R /MediaBox [0 0 595 842] /Resources << /Font << /F1 5 0 R >> >> /Contents 4 0 R >>",
            b"<< /Length %d >>\nstream\n" % len(stream) + stream + b"\nendstream",
            b"<< /Type /Font /Subtype /Type1 /BaseFont /Helvetica >>"]
    out, offs = bytearray(b"%PDF-1.4\n"), []
    for i, o in enumerate(objs, 1):
        offs.append(len(out))
        out += b"%d 0 obj\n" % i + o + b"\nendobj\n"
    xref = len(out)
    out += b"xref\n0 %d\n0000000000 65535 f \n" % (len(objs) + 1)
    out += b"".join(b"%010d 00000 n \n" % o for o in offs)
    out += b"trailer\n<< /Size %d /Root 1 0 R >>\nstartxref\n%d\n%%%%EOF\n" % (len(objs) + 1, xref)
    return bytes(out)


def minimal_docx(path, text):
    ct = ('<?xml version="1.0" encoding="UTF-8"?><Types xmlns="http://schemas.openxmlformats.org/package/2006/content-types">'
          '<Default Extension="rels" ContentType="application/vnd.openxmlformats-package.relationships+xml"/>'
          '<Default Extension="xml" ContentType="application/xml"/>'
          '<Override PartName="/word/document.xml" ContentType="application/vnd.openxmlformats-officedocument.wordprocessingml.document.main+xml"/></Types>')
    rels = ('<?xml version="1.0" encoding="UTF-8"?><Relationships xmlns="http://schemas.openxmlformats.org/package/2006/relationships">'
            '<Relationship Id="rId1" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/officeDocument" Target="word/document.xml"/></Relationships>')
    doc = ('<?xml version="1.0" encoding="UTF-8"?><w:document xmlns:w="http://schemas.openxmlformats.org/wordprocessingml/2006/main">'
           f'<w:body><w:p><w:r><w:t>{text}</w:t></w:r></w:p></w:body></w:document>')
    with zipfile.ZipFile(path, "w", zipfile.ZIP_DEFLATED) as z:
        z.writestr("[Content_Types].xml", ct)
        z.writestr("_rels/.rels", rels)
        z.writestr("word/document.xml", doc)


PNG_1PX = bytes.fromhex("89504e470d0a1a0a0000000d4948445200000001000000010806000000"
                        "1f15c4890000000d49444154789c6360f8cfc0000003010100c9fe92ef0000000049454e44ae426082")


def write_file(path, ext, title, y_be, m):
    if ext == "xlsx":
        wb = Workbook()
        ws = wb.active
        ws.append(["หัวข้อ", "เดือน", "ค่า (สมมติ)"])
        for i in range(rng.randint(3, 15)):
            ws.append([title, f"{TH_MONTH[m - 1]} {y_be}", rng.randint(1000, 999999)])
        wb.save(path)
    elif ext == "docx":
        minimal_docx(path, f"{title} — {TH_MONTH[m - 1]} {y_be} (เอกสารจำลอง)")
    elif ext == "pdf":
        path.write_bytes(minimal_pdf(f"Synthetic document {y_be - 543}-{m:02d} (fictional)"))
    elif ext == "csv":
        lines = ["doc_no,item,amount_thb"] + [f"S{rng.randint(10000, 99999)},item{i},{rng.randint(100, 90000)}"
                                              for i in range(rng.randint(5, 40))]
        path.write_text("\n".join(lines), encoding="utf-8")
    elif ext == "png":
        path.write_bytes(PNG_1PX)
    else:
        path.write_text(f"{title}\nบันทึกจำลอง {TH_MONTH[m - 1]} {y_be}\n", encoding="utf-8")


def main():
    n = int(sys.argv[sys.argv.index("--count") + 1]) if "--count" in sys.argv else 1500
    OUT = HERE / "out" / (sys.argv[sys.argv.index("--out") + 1] if "--out" in sys.argv else "messy_folder")
    if OUT.exists():
        shutil.rmtree(OUT)
    OUT.mkdir(parents=True)
    made = 0
    while made < n:
        y_be = rng.choices(range(2562, 2570), weights=[6, 8, 10, 12, 14, 16, 18, 12])[0]
        m = rng.randint(1, 10 if y_be == 2569 else 12)   # course runs Oct 2569: no future files
        topic, ext = rng.choice(TOPICS)
        if topic == "IMG_":
            name = f"IMG_{rng.randint(1000, 9999)}.{ext}"
        else:
            parts = [topic, rng.choice(SITES) if rng.random() < .6 else "", date_text(y_be, m)]
            rng.shuffle(parts)
            sep = rng.choice(["_", " ", "-", ""])
            name = sep.join(p for p in parts if p) + rng.choice(SUFFIX) + "." + ext
        if rng.random() < .04:
            name = "Copy of " + name
        folder = OUT
        for _ in range(rng.choice([0, 1, 1, 2, 3])):
            folder = folder / rng.choice(FOLDERS)
        folder.mkdir(parents=True, exist_ok=True)
        path = folder / name
        if path.exists():
            continue
        write_file(path, ext, topic, y_be, m)
        ts = dt.datetime(y_be - 543, m, rng.randint(1, 28), rng.randint(8, 19)).timestamp()
        os.utime(path, (ts, ts))
        made += 1
    total = sum(p.stat().st_size for p in OUT.rglob("*") if p.is_file())
    print(f"{OUT}: {made} files, {total / 1e6:.1f} MB")


if __name__ == "__main__":
    main()
