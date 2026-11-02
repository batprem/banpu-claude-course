#!/usr/bin/env python3
"""Add the 'Artifact ที่ใช้ใน Workshop นี้' box (clickable public links) to a module's workshop sheet.

Idempotent: an existing box (marker class ws-artifacts) is replaced, never duplicated.
The box is a <div> placed just before the first page card, so page counts do not change.
Usage: python3 tools/add_workshop_links.py m1 [m2 ...]   (or import links_box/insert from Python)
"""
import pathlib
import re
import sys

ROOT = pathlib.Path(__file__).resolve().parent.parent

ARTIFACTS = {
    "m1": [("Data Traffic Light", "https://claude.ai/artifact/F9jhpdSui1ybEe4M794LvZ", "เกม 15 ใบ: ข้อมูลนี้ใส่ Claude ได้ไหม (รอบ 1)")],
    "m2": [("Workshop Companion", "https://claude.ai/artifact/Vyp7t1u44Ga5W4YbpuMYdP", "checklist และปุ่ม copy prompt ตลอด workshop"),
           ("Excel Detective", "https://claude.ai/artifact/1ytRQDkazJW4Xw24zZwkLu", "Workshop B: ตรวจว่า Claude จับกับดักไฟล์ Excel ครบไหม"),
           ("Prompt Playground", "https://claude.ai/artifact/LQ7Mh4vNj4syXPARm6ucV8", "ดูตัวอย่าง prompt before/after"),
           ("Prototype Gallery", "https://claude.ai/artifact/3s1YpuHwGK7QvSn7ogm2Aq", "Workshop A: โหวต 1 สไตล์ก่อนสร้างทั้ง deck")],
    "m3": [("Connector Mission", "https://claude.ai/artifact/F4gquxgXQwnB8cSTo3hsBq", "ภารกิจ Connector SharePoint/Outlook ทีละด่าน")],
    "m4": [("Monthly Ops Dashboard", "https://claude.ai/artifact/5wEyprUmbagfBfBXXe4SJP", "dashboard ตัวอย่าง ไว้เทียบกับของเรา"),
           ("Output Picker", "https://claude.ai/artifact/S47Pyq2mMTUk85nZ2HQL67", "เกม 10 ข้อ: งานนี้ควรออกมาเป็นอะไร")],
    "m5": [("Skill Security Checklist", "https://claude.ai/artifact/8M5tgdbZfTgxtFuFkjXqqn", "ล่าธงแดง Skill ปลอม + Checklist แล้ว Export PDF")],
    "m6": [("Automation Card", "https://claude.ai/artifact/HFdt3zwrfBgErGfv6q5TUk", "ออกแบบงานอัตโนมัติ 6 ช่อง + quiz")],
    "m7": [("Show & Share Board", "https://claude.ai/artifact/VncwbAfqEmSuDFBtGfx5uy", "การ์ดทีม โหวต rubric และ timer")],
    "m8": [("Security & Usage Quiz", "https://claude.ai/artifact/L6PcYj1MiRy7Aah9cUVgsv", "ควิซ 18 ข้อ + Traffic Light รอบสุดท้าย"),
           ("แผน 30 วัน", "https://claude.ai/artifact/Dn5jDTNdz6YBP8DT23T7Nt", "วางแผน 30 วันของฉัน แล้ว Export PDF")],
}

BOX_RE = re.compile(r'<div class="ws-artifacts"[^>]*>.*?<!-- /ws-artifacts -->\n?', re.S)
FIRST_CARD = re.compile(r'<section[^>]*class="[^"]*\bcard\b[^"]*"[^>]*data-page="1"[^>]*>|<section[^>]*class="[^"]*\bcard\b[^"]*"[^>]*>')


def esc(s):
    return s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")


def links_box(mod):
    items = "".join(
        f'<li style="margin:6px 0;line-height:1.5">'
        f'<a href="{url}" target="_blank" rel="noopener" style="color:#0684C9;font-weight:700;text-decoration:underline">{esc(name)} ↗</a>'
        f' <span style="color:#3D3839">— {esc(desc)}</span>'
        f'<br><span style="font-size:13px;color:#5E5859;word-break:break-all">{url}</span></li>'
        for name, url, desc in ARTIFACTS[mod])
    return (
        '<div class="ws-artifacts" style="background:#FFF3D1;color:#231F20;border:1px solid #F2D58A;border-left:8px solid #FFD066;'
        'border-radius:12px;padding:14px 18px;margin:16px 0 20px;break-inside:avoid">'
        '<p style="margin:0 0 6px;font-weight:700;font-size:17px;color:#231F20">🔗 Artifact ที่ใช้ใน Workshop นี้</p>'
        '<p style="margin:0 0 6px;font-size:14px;color:#3D3839">คลิกเพื่อเปิดในแท็บใหม่ · ทุกลิงก์เปิดได้ด้วยลิงก์นี้ (Anyone with the link)</p>'
        f'<ul style="margin:0;padding-left:20px;font-size:16px">{items}</ul>'
        '</div><!-- /ws-artifacts -->\n'
    )


def insert(html, mod):
    html = BOX_RE.sub("", html)
    m = FIRST_CARD.search(html)
    if not m:
        raise SystemExit(f"{mod}: no page card found")
    return html[:m.start()] + links_box(mod) + html[m.start():]


def main(mods):
    for mod in mods:
        p = ROOT / "materials" / mod / "artifacts" / "workshop-sheet.html"
        before = p.read_text(encoding="utf-8")
        after = insert(before, mod)
        p.write_text(after, encoding="utf-8")
        urls = re.findall(r'href="(https://claude\.ai/artifact/\w+)"', BOX_RE.search(after).group(0))
        print(f"{mod}: box with {len(urls)} link(s); boxes in file={after.count('class=\"ws-artifacts\"')}; changed={after != before}")


if __name__ == "__main__":
    main(sys.argv[1:])
