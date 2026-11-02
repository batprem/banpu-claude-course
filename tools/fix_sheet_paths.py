#!/usr/bin/env python3
"""Make material paths in the workshop sheets match the GitHub repo, as clickable links.

For each <code>…</code> outside prompts (<pre>), scripts, styles and the ws-artifacts box:
- repo material  -> <a class="repo-link" href="…/blob|tree/master/<path>"><code><shown text></code></a>
                    (shown text = the real repo path, unless a short name is kept on purpose)
- built file not kept in git (gitignored ZIP/large data) -> name kept, plus a link to the script/folder it is built from
- learner working paths (Documents/…, input/, output/…), e-mails, code tokens -> unchanged (not repo materials)
Every target is checked against `git ls-files`. Runs once per file (skips a file that already has repo links).
Usage: python3 tools/fix_sheet_paths.py m1 … m8      (M7: called by build_workshop_sheet.py instead)
"""
import pathlib
import re
import subprocess
import sys
import urllib.parse

ROOT = pathlib.Path(__file__).resolve().parent.parent
REPO = "https://github.com/batprem/banpu-claude-course"
BRANCH = "master"  # the repo's only branch (there is no 'main')

# text in <code> -> (repo path, shown text or None = show the repo path) ; ("GEN", source path, note) for built files
M = {
    "m1": {"artifacts/data-traffic-light.html": ("materials/m1/artifacts/data-traffic-light.html", None),
           "data-traffic-light.html": ("materials/m1/artifacts/data-traffic-light.html", None)},
    "m2": {"workshop_b_scattered/": ("materials/m2/data/workshop_b_scattered", "workshop_b_scattered/"),
           "เก่า_ไม่ใช้/": ("materials/m2/data/workshop_b_scattered/เก่า_ไม่ใช้", "เก่า_ไม่ใช้/"),
           "messy_folder_sample/": ("GEN", "materials/m2/data/generate_messy_folder.py", "สร้างด้วย"),
           "input/messy_folder_sample": ("GEN", "materials/m2/data/generate_messy_folder.py", "สร้างด้วย")},
    "m3": {"artifacts/connector-mission.html": ("materials/m3/artifacts/connector-mission.html", None),
           "M3_SamplePack.zip": ("GEN", "materials/m3/data/pack", "ZIP ของโฟลเดอร์"),
           "M3_SamplePack/": ("GEN", "materials/m3/data/pack", "= โฟลเดอร์")},
    "m4": {"energy_prices_public_2023-2026.csv": ("materials/m4/data/energy_prices_public_2023-2026.csv", None),
           "ops_monthly_2566-2569.xlsx": ("materials/m4/data/ops_monthly_2566-2569.xlsx", None),
           "shift_log_2568-2569.csv": ("GEN", "materials/m4/data/gen_m4_data.py", "สร้างด้วย"),
           "Monthly_Ops_Report_2569-09_FULL.docx": ("GEN", "materials/m4/data/gen_m4_data.py", "สร้างด้วย"),
           "m3_outlook/*.eml": ("GEN", "materials/m3/data/pack/outlook", "จาก"),
           "m3_sharepoint/*.csv": ("GEN", "materials/m3/data/pack/sharepoint", "จาก")},
    "m5": {"SKILL.md": ("materials/m5/skill-example/banpu-standard-report/SKILL.md", None),
           "banpu-standard-report/": ("materials/m5/skill-example/banpu-standard-report", "banpu-standard-report/"),
           "skill-example/banpu-standard-report/": ("materials/m5/skill-example/banpu-standard-report", "materials/m5/skill-example/banpu-standard-report/"),
           "examples/example-report-site-b.md": ("materials/m5/skill-example/banpu-standard-report/examples/example-report-site-b.md", None),
           "skill-audit-sample/": ("materials/m5/skill-audit-sample", "materials/m5/skill-audit-sample/"),
           "skill-security-checklist.html": ("materials/m5/artifacts/skill-security-checklist.html", None),
           "solar_F_2023_2025.xlsx": ("materials/m2/data/workshop_b_scattered/solar_F_2023_2025.xlsx", None),
           "materials/m2/data/workshop_b_scattered/": ("materials/m2/data/workshop_b_scattered", "materials/m2/data/workshop_b_scattered/"),
           "banpu-standard-report.zip": ("GEN", "materials/m5/skill-example/README.md", "ZIP ของโฟลเดอร์ skill · วิธีสร้าง")},
    "m6": {},
    "m7": {"artifacts/show-share-board.html": ("materials/m7/artifacts/show-share-board.html", None),
           "data/out/M7_uc1…uc5.zip": ("GEN", "materials/m7/data/gen_m7_data.py", "สร้างด้วย"),
           "BRIEF.md": ("materials/m7/data", "BRIEF.md"),
           "M7_uc1_contract_summary.zip": ("GEN", "materials/m7/data/uc1_contract_summary", "ZIP ของโฟลเดอร์"),
           "M7_uc2_incident_weekly.zip": ("GEN", "materials/m7/data/uc2_incident_weekly", "ZIP ของโฟลเดอร์"),
           "M7_uc3_esg_consolidation.zip": ("GEN", "materials/m7/data/uc3_esg_consolidation", "ZIP ของโฟลเดอร์"),
           "M7_uc4_meeting_actions.zip": ("GEN", "materials/m7/data/uc4_meeting_actions", "ZIP ของโฟลเดอร์"),
           "M7_uc5_energy_market_brief.zip": ("GEN", "materials/m7/data/uc5_energy_market_brief", "ZIP ของโฟลเดอร์"),
           "contract_register.csv": ("materials/m7/data/uc1_contract_summary/contract_register.csv", "contract_register.csv"),
           "contracts/": ("materials/m7/data/uc1_contract_summary/contracts", "contracts/"),
           "incident_log.csv": ("materials/m7/data/uc2_incident_weekly/incident_log.csv", "incident_log.csv"),
           "emails/": ("materials/m7/data/uc2_incident_weekly/emails", "emails/"),
           "emission_factors_SYNTHETIC.csv": ("materials/m7/data/uc3_esg_consolidation/emission_factors_SYNTHETIC.csv", "emission_factors_SYNTHETIC.csv"),
           "esg_targets_2568.csv": ("materials/m7/data/uc3_esg_consolidation/esg_targets_2568.csv", "esg_targets_2568.csv"),
           "meetings/": ("materials/m7/data/uc4_meeting_actions/meetings", "meetings/"),
           "action_tracker_sharepoint_list_export.csv": ("materials/m7/data/uc4_meeting_actions/action_tracker_sharepoint_list_export.csv", "action_tracker_sharepoint_list_export.csv"),
           "owners.md": ("materials/m7/data/uc4_meeting_actions/owners.md", "owners.md"),
           "news_snippets_SYNTHETIC.csv": ("materials/m7/data/uc5_energy_market_brief/news_snippets_SYNTHETIC.csv", "news_snippets_SYNTHETIC.csv"),
           "prices_weekly_SYNTHETIC.csv": ("materials/m7/data/uc5_energy_market_brief/prices_weekly_SYNTHETIC.csv", "prices_weekly_SYNTHETIC.csv"),
           "internal_view.md": ("materials/m7/data/uc5_energy_market_brief/internal_view.md", "internal_view.md")},
    "m8": {"artifacts/plan-30-days.html": ("materials/m8/artifacts/plan-30-days.html", None),
           "artifacts/security-quiz.html": ("materials/m8/artifacts/security-quiz.html", None),
           "plan-30-days.html": ("materials/m8/artifacts/plan-30-days.html", None),
           "security-quiz.html": ("materials/m8/artifacts/security-quiz.html", None)},
}
for mod in M:  # every sheet's prompts.md means its own module's file
    M[mod]["prompts.md"] = (f"materials/{mod}/prompts.md", None)

_files = None


def repo_files():
    global _files
    if _files is None:
        out = subprocess.run(["git", "-c", "core.quotepath=off", "ls-files"], cwd=ROOT, capture_output=True, text=True, check=True).stdout
        _files = set(out.splitlines())
    return _files


def gh_url(path):
    files = repo_files()
    if path in files:
        kind = "blob"
    elif any(f.startswith(path + "/") for f in files):
        kind = "tree"
    else:
        raise SystemExit(f"not in repo: {path}")
    return f"{REPO}/{kind}/{BRANCH}/{urllib.parse.quote(path)}"


A = 'class="repo-link" target="_blank" rel="noopener" style="color:#0684C9;text-decoration:underline"'
PROTECT = re.compile(r'<pre[^>]*>.*?</pre>|<script.*?</script>|<style.*?</style>|<div class="ws-artifacts".*?<!-- /ws-artifacts -->|<a\b[^>]*>.*?</a>', re.S)


def fix(html, mod):
    """Return (html, changes) with the module's path map applied outside protected regions."""
    mapping = M[mod]
    changes = []
    out, pos = [], 0
    for prot in list(PROTECT.finditer(html)) + [None]:
        end = prot.start() if prot else len(html)
        seg = html[pos:end]

        def repl(m):
            text = m.group(1)
            key = re.sub(r"<[^>]+>", "", text)
            if key not in mapping:
                return m.group(0)
            v = mapping[key]
            if v[0] == "GEN":
                _, src, note = v
                changes.append((key, f"(built, not in git) {note} {src}"))
                return (f'{m.group(0)} <a {A} href="{gh_url(src)}">({note} <code>{src}</code>)</a>')
            path, shown = v
            shown = shown or path
            changes.append((key, path))
            return f'<a {A} href="{gh_url(path)}"><code>{shown}</code></a>'

        out.append(re.sub(r"<code>(.*?)</code>", repl, seg))
        if prot:
            out.append(prot.group(0))
            pos = prot.end()
    return "".join(out), changes


def main(mods):
    for mod in mods:
        p = ROOT / "materials" / mod / "artifacts" / "workshop-sheet.html"
        html = p.read_text(encoding="utf-8")
        if 'class="repo-link"' in html:
            print(f"{mod}: already has repo links, skipped")
            continue
        new, changes = fix(html, mod)
        p.write_text(new, encoding="utf-8")
        seen = {}
        for k, v in changes:
            seen.setdefault((k, v), 0)
            seen[(k, v)] += 1
        print(f"== {mod}: {len(changes)} reference(s) linked")
        for (k, v), n in seen.items():
            print(f"   {k}  ->  {v}" + (f"  (x{n})" if n > 1 else ""))


if __name__ == "__main__":
    main(sys.argv[1:])
