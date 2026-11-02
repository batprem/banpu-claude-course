#!/usr/bin/env python3
"""Assemble the learner "M2 pack" in data/pack/input/ (committed, so it is in the repo ZIP learners
download: banpu-claude-course-master/materials/m2/data/pack/ = the Cowork folder).

  input/workshop_b_scattered/          written here by generate_core_pack.py
  input/messy_folder_sample/           copy of out/messy_folder_sample (generate_messy_folder.py --count 100 --out messy_folder_sample)
  input/production_shift_log_2566-2568.csv, input/annual_review_synthetic_320p.pdf   copies from generate_big_files.py
  output/                              where learners' results go

Usage: python3 materials/m2/data/build_m2_pack.py   (after the generators)
"""
import pathlib
import shutil

HERE = pathlib.Path(__file__).resolve().parent
SRC = HERE / "out"
DST = HERE / "pack" / "input"


def main():
    if (DST / "messy_folder_sample").exists():
        shutil.rmtree(DST / "messy_folder_sample")
    shutil.copytree(SRC / "messy_folder_sample", DST / "messy_folder_sample")
    for f in ["production_shift_log_2566-2568.csv", "annual_review_synthetic_320p.pdf"]:
        shutil.copy2(SRC / f, DST / f)
    total = sum(p.stat().st_size for p in DST.rglob("*") if p.is_file())
    print(f"{DST}: {sum(1 for p in DST.rglob('*') if p.is_file())} files, {total / 1e6:.1f} MB")


if __name__ == "__main__":
    main()
