#!/usr/bin/env python3
"""Rebuild materials/SOURCES.md from every materials/m*/SOURCES.md table (renumbered, module-prefixed)."""
import pathlib, re
root = pathlib.Path(__file__).resolve().parent.parent / "materials"
head = (root / "SOURCES.md").read_text(encoding="utf-8").split("| # |")[0]
rows, n = [], 0
for f in sorted(root.glob("m[0-9]/SOURCES.md")):
    mod = f.parent.name.upper()
    for line in f.read_text(encoding="utf-8").splitlines():
        cells = [c.strip() for c in line.strip().strip("|").split("|")]
        if len(cells) >= 7 and re.fullmatch(r"\d+", cells[0]):
            n += 1
            rows.append(f"| {n} | {cells[1]} | {mod}: {cells[2]} | " + " | ".join(cells[3:7]) + " |")
out = head + "| # | Item | Used in | URL | Author / owner | Licence / usage rights | Accessed |\n|---|---|---|---|---|---|---|\n" + "\n".join(rows) + "\n"
(root / "SOURCES.md").write_text(out, encoding="utf-8")
print(f"{n} sources merged")
