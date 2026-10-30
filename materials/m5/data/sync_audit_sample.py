#!/usr/bin/env python3
"""Embed the fake third-party Skill (skill-audit-sample/) and its red flags
(data/audit_flags.json) into artifacts/skill-security-checklist.html.

Edit the sample files or the flags JSON, then run:
    python3 materials/m5/data/sync_audit_sample.py
Each flag's "match" must appear on exactly one line of its file.
"""
import json
import pathlib
import re
import sys

M5 = pathlib.Path(__file__).resolve().parent.parent
SAMPLE = M5 / "skill-audit-sample"
FLAGS = M5 / "data" / "audit_flags.json"
HTML = M5 / "artifacts" / "skill-security-checklist.html"
START, END = "/*AUDIT_DATA_START*/", "/*AUDIT_DATA_END*/"


def build():
    spec = json.loads(FLAGS.read_text(encoding="utf-8"))
    files = []
    for rel in spec["files"]:
        lines = (SAMPLE / rel).read_text(encoding="utf-8").rstrip("\n").split("\n")
        files.append({"path": rel, "lines": lines})
    by_path = {f["path"]: f["lines"] for f in files}
    flags = []
    for fl in spec["flags"]:
        hits = [i for i, line in enumerate(by_path[fl["file"]]) if fl["match"] in line]
        if len(hits) != 1:
            sys.exit(f"{fl['id']}: match {fl['match']!r} found on {len(hits)} lines of {fl['file']}")
        flags.append({**fl, "line": hits[0]})
    return {"categories": spec["categories"], "files": files, "flags": flags}


def main():
    data = json.dumps(build(), ensure_ascii=False).replace("</", "<\\/")
    page = HTML.read_text(encoding="utf-8")
    pattern = re.escape(START) + r".*?" + re.escape(END)
    if not re.search(pattern, page, re.S):
        sys.exit(f"markers not found in {HTML}")
    page = re.sub(pattern, lambda _: f"{START}{data}{END}", page, flags=re.S)
    HTML.write_text(page, encoding="utf-8")
    print(f"{HTML}: embedded {len(json.loads(data)['flags'])} flags")


if __name__ == "__main__":
    main()
