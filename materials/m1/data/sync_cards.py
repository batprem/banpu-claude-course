#!/usr/bin/env python3
"""Copy traffic_light_cards.json into the Data Traffic Light Artifact.

Edit the JSON (add cards, e.g. M8 extras with "module": "M8"), then run:
  python3 materials/m1/data/sync_cards.py [path/to/cards.json] [path/to/game.html]
Defaults: this folder's traffic_light_cards.json → ../artifacts/data-traffic-light.html.
M8 can pass its own JSON and output path to build a variant without touching M1 files.
"""
import json
import pathlib
import re
import sys

HERE = pathlib.Path(__file__).parent
src = pathlib.Path(sys.argv[1]) if len(sys.argv) > 1 else HERE / "traffic_light_cards.json"
html_path = pathlib.Path(sys.argv[2]) if len(sys.argv) > 2 else HERE.parent / "artifacts" / "data-traffic-light.html"

data = json.loads(src.read_text(encoding="utf-8"))
ids = [c["id"] for c in data["cards"]]
assert len(ids) == len(set(ids)), "duplicate card id"
for c in data["cards"]:
    assert c["answer"] in data["levels"], f"{c['id']}: answer must be one of {list(data['levels'])}"

block = json.dumps(data, ensure_ascii=False, indent=1).replace("</", "<\\/")
page = html_path.read_text(encoding="utf-8")
page, n = re.subn(r'(<script type="application/json" id="cards-data">\n).*?(\n</script>)',
                  lambda m: m.group(1) + block + m.group(2), page, flags=re.S)
assert n == 1, "cards-data block not found"
html_path.write_text(page, encoding="utf-8")
print(f"{html_path}: {len(ids)} cards")
