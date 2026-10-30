#!/usr/bin/env python3
"""Public external source for the M4 workshop (source 5 of 5): monthly energy prices.

Downloads three IMF Primary Commodity Prices series from FRED (St. Louis Fed) and writes
  energy_prices_public_2023-2026.csv   (committed, ~4 KB; re-run the week of training)

Series (monthly averages, USD):
  PCOALAUUSDM  Global price of Coal, Australia          USD / metric ton
  POILBREUSDM  Global price of Brent Crude              USD / barrel
  PNGASJPUSDM  Global price of LNG, Asia (Japan)        USD / million BTU
Source: International Monetary Fund, Global price series, retrieved from FRED,
Federal Reserve Bank of St. Louis — https://fred.stlouisfed.org/series/<ID>  (see m4/SOURCES.md)

Usage: python3 materials/m4/data/fetch_energy_prices.py [--offline]
  --offline  rebuild the CSV from the raw PCOALAUUSDM.csv etc. already in raw/ (no network)
"""
import csv
import pathlib
import sys
import urllib.request

HERE = pathlib.Path(__file__).resolve().parent
RAW = HERE / "raw"
OUT = HERE / "energy_prices_public_2023-2026.csv"
SERIES = [
    ("PCOALAUUSDM", "coal_aus_usd_per_t", "Coal, Australia (USD/t)"),
    ("POILBREUSDM", "brent_usd_per_bbl", "Brent crude (USD/bbl)"),
    ("PNGASJPUSDM", "lng_asia_usd_per_mmbtu", "LNG Asia/Japan (USD/MMBtu)"),
]
URL = "https://fred.stlouisfed.org/graph/fredgraph.csv?id={}&cosd=2023-01-01"


def main():
    RAW.mkdir(exist_ok=True)
    table = {}
    for sid, col, _ in SERIES:
        raw = RAW / f"{sid}.csv"
        if "--offline" not in sys.argv:
            with urllib.request.urlopen(URL.format(sid), timeout=60) as r:
                raw.write_bytes(r.read())
        with open(raw, encoding="utf-8") as f:
            for row in csv.DictReader(f):
                v = row[sid].strip()
                if v and v != ".":
                    table.setdefault(row["observation_date"][:7], {})[col] = round(float(v), 2)
    with open(OUT, "w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        w.writerow(["month"] + [c for _, c, _ in SERIES] + ["source"])
        for m in sorted(table):
            w.writerow([m] + [table[m].get(c, "") for _, c, _ in SERIES]
                       + ["IMF Primary Commodity Prices via FRED (fred.stlouisfed.org)"])
    print(f"{OUT}: {len(table)} months, last = {max(table)}")


if __name__ == "__main__":
    main()
