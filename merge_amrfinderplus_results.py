#!/usr/bin/env python3
"""
merge_amrfinderplus_results.py

Combine all *_amr_results.tsv files into one table and add a Sample_ID column.
"""

from pathlib import Path
import pandas as pd

# ── 1. Path to your AMRFinderPlus result files ──────────────────────────────────
INPUT_DIR   = Path("/home/manueljara/Documents/0_ML_AMR_project/AMR_identification/amrfinder_results_plus_protein")
OUTPUT_FILE = Path("combined_amrfinderplus_results.csv")  # change to .tsv if preferred

# If results are inside sub-directories under INPUT_DIR, flip this to True
RECURSIVE = False            # set True if you have nested folders

# ── 2. Collect matching files ───────────────────────────────────────────────────
pattern = "**/*_amr_results.tsv" if RECURSIVE else "*_amr_results.tsv"
tsv_files = sorted(INPUT_DIR.glob(pattern))

if not tsv_files:
    raise SystemExit(f"No files matched {pattern} under {INPUT_DIR}")

print(f"Found {len(tsv_files)} result files.")

# ── 3. Read, label, accumulate ─────────────────────────────────────────────────
dfs = []
for tsv in tsv_files:
    df = pd.read_csv(tsv, sep="\t")
    sample_id = tsv.name.replace("_amr_results.tsv", "")
    df.insert(0, "Sample_ID", sample_id)
    dfs.append(df)

# ── 4. Concatenate and save ────────────────────────────────────────────────────
combined = pd.concat(dfs, ignore_index=True)

sep = "\t" if OUTPUT_FILE.suffix.lower() == ".tsv" else ","
combined.to_csv(OUTPUT_FILE, sep=sep, index=False)

print(f"Combined table saved to {OUTPUT_FILE}  "
      f"(rows: {combined.shape[0]}, columns: {combined.shape[1]})")
