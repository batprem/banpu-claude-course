#!/usr/bin/env python3
"""Check rewritten speaker notes of a Slides deck against git HEAD.

Usage: python3 tools/check_notes.py m1 [--base <git rev>]
- every slide in deck.json order exists and has exactly one <aside> as the section's last child
- everything outside <aside>…</aside> is byte-identical to the file at the base revision (default HEAD)
- each aside has exactly one line '----------', non-empty script above it and tips below it, ≤ 4000 chars
"""
import json
import pathlib
import re
import subprocess
import sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
mod = sys.argv[1]
base = sys.argv[sys.argv.index("--base") + 1] if "--base" in sys.argv else "HEAD"
deck = ROOT / "materials" / mod / "deck" / "project"
order = json.loads((deck / "deck.json").read_text(encoding="utf-8"))["order"]
ASIDE = re.compile(r"<aside>(.*?)</aside>", re.S)
problems, changed, thai_chars = [], 0, []
for sid in order:
    rel = f"materials/{mod}/deck/project/slides/{sid}.html"
    text = (ROOT / rel).read_text(encoding="utf-8")
    asides = ASIDE.findall(text)
    if len(asides) != 1 or not re.search(r"</aside>\s*</section>\s*$", text):
        problems.append((sid, "aside count/position")); continue
    note = asides[0]
    try:
        old = subprocess.run(["git", "show", f"{base}:{rel}"], cwd=ROOT, capture_output=True, text=True, check=True).stdout
    except subprocess.CalledProcessError:
        problems.append((sid, f"not in {base}")); continue
    if ASIDE.sub("<aside></aside>", text) != ASIDE.sub("<aside></aside>", old):
        problems.append((sid, "slide content changed outside <aside>"))
    if ASIDE.findall(old) and ASIDE.findall(old)[0] != note:
        changed += 1
    lines = note.split("\n")
    seps = [i for i, l in enumerate(lines) if l.strip() == "----------"]
    if len(seps) != 1:
        problems.append((sid, f"separator lines={len(seps)}")); continue
    script = "\n".join(lines[:seps[0]]).strip()
    tips = "\n".join(lines[seps[0] + 1:]).strip()
    if not script or not tips:
        problems.append((sid, "empty script or tips"))
    if len(note) > 4000:
        problems.append((sid, f"aside {len(note)} chars > 4000"))
    if re.search(r"(?i)samsung", note):
        problems.append((sid, "mentions Samsung"))
    thai_chars.append(len(script))
print(f"{mod}: slides={len(order)} notes changed={changed} script chars min/median/max="
      f"{min(thai_chars) if thai_chars else 0}/{sorted(thai_chars)[len(thai_chars)//2] if thai_chars else 0}/{max(thai_chars) if thai_chars else 0}")
print("problems:", problems or "none")
