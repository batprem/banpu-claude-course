#!/usr/bin/env python3
"""Add the Thai "เตรียมไฟล์" setup box (download + extract the repo ZIP) to a module's workshop sheet.

Learners download https://github.com/batprem/banpu-claude-course (Code > Download ZIP) and extract it,
which gives banpu-claude-course-master/. Every learner-local path in the sheets starts there.
Idempotent: an existing box (marker class ws-setup) is replaced. Placed right after the
'Artifact ที่ใช้ใน Workshop นี้' box (tools/add_workshop_links.py), before the first page card.
Usage: python3 tools/add_setup_step.py m1 [m2 ...]   (M7: called by build_workshop_sheet.py instead)
"""
import pathlib
import re
import sys
import urllib.parse

ROOT = pathlib.Path(__file__).resolve().parent.parent
REPO = "https://github.com/batprem/banpu-claude-course"
ZIP_URL = f"{REPO}/archive/refs/heads/master.zip"
Z = "banpu-claude-course-master"
A = 'class="repo-link" target="_blank" rel="noopener" style="color:#0684C9;text-decoration:underline"'


def folder(path, suffix=""):
    """Local path shown as the extracted-ZIP path, linked to the same folder on GitHub."""
    return f'<a {A} href="{REPO}/tree/master/{urllib.parse.quote(path)}"><code>{Z}/{path}{suffix}</code></a>'


USE = {
    "m1": f"ไม่ต้องใช้ไฟล์ในเครื่อง (เกมอยู่ใน Artifact ด้านบน) · prompt ทั้งหมดอยู่ที่ <code>{Z}/materials/m1/prompts.md</code>",
    "m2": f"ใน Cowork เลือกโฟลเดอร์ {folder('materials/m2/data/pack')} — <code>input/</code> = ข้อมูลสมมติ · <code>output/</code> = ที่เก็บผลลัพธ์",
    "m3": f"เส้นทาง B (ไม่มี test tenant): ใน Cowork เลือกโฟลเดอร์ {folder('materials/m3/data/pack')} (<code>outlook/</code> + <code>sharepoint/</code>)",
    "m4": f"ใน Cowork เลือกโฟลเดอร์ {folder('materials/m4/data/pack')} — <code>input/</code> 27 ไฟล์ (มีไฟล์ใหญ่ 11 MB และ 37 MB) · <code>output/</code> = ที่เก็บผลลัพธ์",
    "m5": f"Skill ตัวอย่าง: {folder('materials/m5/skill-example/banpu-standard-report')} · Skill ปลอมสำหรับตรวจ: {folder('materials/m5/skill-audit-sample')} · ไฟล์ทดสอบ: {folder('materials/m2/data/pack/input/workshop_b_scattered')}",
    "m6": f"เส้นทาง B: Cowork และ Scheduled task ใช้โฟลเดอร์ {folder('materials/m6/data/pack')} — อ่าน <code>input/</code> · เขียนได้เฉพาะ <code>output/</code>",
    "m7": f"แต่ละทีมใช้โฟลเดอร์โจทย์ใน {folder('materials/m7/data')} (<code>uc1_…</code> ถึง <code>uc5_…</code>) แล้วสร้างโฟลเดอร์ย่อย <code>output/</code> ข้างใน · ทีม BYO สร้างโฟลเดอร์ใหม่ <code>{Z}/materials/m7/capstone_&lt;ทีม&gt;/</code>",
    "m8": f"ไม่ต้องใช้ไฟล์ในเครื่อง (ใช้ Artifact ด้านบน) · ถ้าเปิด Artifact ไม่ได้ ใช้ไฟล์ใน {folder('materials/m8/artifacts')}",
}

BOX_RE = re.compile(r'<div class="ws-setup"[^>]*>.*?<!-- /ws-setup -->\n?', re.S)
AFTER = "<!-- /ws-artifacts -->\n"


def setup_box(mod):
    return (
        '<div class="ws-setup" style="background:#FFFDF8;color:#231F20;border:1px solid #CFE6F5;border-left:8px solid #0684C9;'
        'border-radius:12px;padding:14px 18px;margin:0 0 20px;break-inside:avoid">'
        '<p style="margin:0 0 6px;font-weight:700;font-size:17px;color:#231F20">🧰 เตรียมไฟล์ก่อนเริ่ม (ทำครั้งเดียว ใช้ได้ทั้งวัน · 2 นาที)</p>'
        '<ol style="margin:0;padding-left:22px;font-size:16px;line-height:1.55">'
        f'<li>ดาวน์โหลด ZIP ของ repo: เปิด <a href="{REPO}" target="_blank" rel="noopener" style="color:#0684C9;font-weight:700;text-decoration:underline">github.com/batprem/banpu-claude-course ↗</a>'
        f' → ปุ่ม <b>Code</b> → <b>Download ZIP</b> (หรือ <a href="{ZIP_URL}" target="_blank" rel="noopener" style="color:#0684C9;text-decoration:underline">ลิงก์ดาวน์โหลดตรง</a>)'
        f'<br><span style="font-size:13px;color:#5E5859;word-break:break-all">{ZIP_URL}</span></li>'
        f'<li>คลิกขวาไฟล์ ZIP → <b>Extract All</b> (Mac: ดับเบิลคลิก) ไว้ใน Documents → ได้โฟลเดอร์ <code>{Z}/</code></li>'
        f'<li>Workshop นี้ใช้: {USE[mod]}</li>'
        '</ol>'
        '<p style="margin:8px 0 0;font-size:14px;color:#3D3839">ZIP คือต้นฉบับ (copy-before-write): ถ้าไฟล์เสียหรืออยากเริ่มใหม่ ให้แตก ZIP ใหม่ · ถ้าแตกไว้แล้วตั้งแต่โมดูลก่อน ข้ามข้อ 1–2 ได้ · ข้อมูลทั้งหมดเป็นข้อมูลสมมติ</p>'
        '</div><!-- /ws-setup -->\n'
    )


def insert(html, mod):
    html = BOX_RE.sub("", html)
    i = html.find(AFTER)
    if i < 0:
        raise SystemExit(f"{mod}: run add_workshop_links.py first (no ws-artifacts box)")
    i += len(AFTER)
    return html[:i] + setup_box(mod) + html[i:]


def main(mods):
    for mod in mods:
        p = ROOT / "materials" / mod / "artifacts" / "workshop-sheet.html"
        before = p.read_text(encoding="utf-8")
        after = insert(before, mod)
        p.write_text(after, encoding="utf-8")
        print(f"{mod}: setup boxes={after.count('class=\"ws-setup\"')} changed={after != before}")


if __name__ == "__main__":
    main(sys.argv[1:])
