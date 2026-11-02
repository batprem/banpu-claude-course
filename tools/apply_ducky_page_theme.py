#!/usr/bin/env python3
"""Apply the Ducky Engineer (วิศวกรเป็ด) theme to a learner page (workshop sheet or interactive Artifact).

Mechanical, idempotent changes only (behaviour and content are untouched):
- font: IBM Plex Sans Thai -> Sarabun (Google Fonts link and font-family stacks; IBM Plex Mono is kept)
- palette: ink #1F2933 -> #231F20, paper #FAF8F3 -> #F4F4F4, warning accent #F2A541 -> duck yellow #FFD066
  (role colours #E4572E / #2E86AB / #3BA55C are kept, as AGENTS.md requires)
- logo: a small round Ducky badge, bottom-right on screen, top-right in print/PDF, embedded as a data URI
  so the page needs no asset store (keeps public sharing possible)

Usage: python3 tools/apply_ducky_page_theme.py materials/m2/artifacts/workshop-sheet.html [...]
"""
import pathlib
import re
import sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
LOGO = (ROOT / "materials/_shared/ducky-logo-160.datauri.txt").read_text(encoding="ascii").strip()
MARK = "ducky-badge"

HEX = [("#1F2933", "#231F20"), ("#1f2933", "#231F20"),
       ("#FAF8F3", "#F4F4F4"), ("#faf8f3", "#F4F4F4"),
       ("#F2A541", "#FFD066"), ("#f2a541", "#FFD066")]

STYLE = (
    "<style>"
    ".ducky-badge{position:fixed;right:16px;bottom:16px;width:56px;height:56px;padding:4px;box-sizing:border-box;"
    "border-radius:50%;background:#FFFDF8;box-shadow:0 2px 8px rgba(35,31,32,.18);z-index:50;object-fit:contain}"
    ".pdf-export .ducky-badge{position:absolute;top:8px;right:8px;bottom:auto}"
    "@media print{.ducky-badge{position:absolute;top:0;right:0;bottom:auto;box-shadow:none}}"
    "</style>"
)


def theme(text: str) -> str:
    text = text.replace("family=IBM+Plex+Sans+Thai", "family=Sarabun")
    text = re.sub(r"(['\"])IBM Plex Sans Thai\1", r"\1Sarabun\1", text)
    text = text.replace("IBM Plex Sans Thai", "Sarabun")
    for old, new in HEX:
        text = text.replace(old, new)
    if MARK not in text:
        badge = f'{STYLE}\n<img class="{MARK}" src="{LOGO}" alt="Ducky Engineer · วิศวกรเป็ด">\n'
        # Insert before the first <script> that follows the page markup, else before </body>, else at the end.
        m = re.search(r"</body>", text, re.I)
        text = text[:m.start()] + badge + text[m.start():] if m else text.rstrip() + "\n" + badge
    return text


def main(paths):
    for p in map(pathlib.Path, paths):
        before = p.read_text(encoding="utf-8")
        after = theme(before)
        if after != before:
            p.write_text(after, encoding="utf-8")
        left = [h for h, _ in HEX if h in after]
        print(f"{p}: {'themed' if after != before else 'unchanged'}; badge={'yes' if MARK in after else 'no'}; "
              f"Sarabun={'Sarabun' in after}; old hex left={left or 'none'}")


if __name__ == "__main__":
    main(sys.argv[1:])
