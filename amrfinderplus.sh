#!/bin/bash
# Before running this code create a folder called "genomes" and add
# the following genome annotation files (.fna.gz, .faa.gz, and .gff.gz)
# ADVANCED script using pre-annotated protein files (.faa.gz) for speed

# --- Setup ---
OUTDIR="amrfinder_results_plus_protein"
echo "Setting up output directory: $OUTDIR"
mkdir -p "$OUTDIR"


# --- Main Analysis Loop ---
echo "Starting protein-based AMRFinderPlus analysis on .faa.gz files..."
# Updated to loop over .faa.gz files
for protein_file in genomes/*.faa.gz; do
    [ -e "$protein_file" ] || continue

    # Updated to remove the .faa.gz suffix
    base_name=$(basename "$protein_file" .faa.gz)

    echo "--> Processing: $base_name with the --plus database"

    # Run AMRFinderPlus using protein input (-p)
    amrfinder \
      -p "$protein_file" \
      -O Salmonella \
      --plus \
      -o "$OUTDIR/${base_name}_amr_results.tsv"
done

echo "--- Analysis Complete! ---"
echo "Full results are in the '$OUTDIR' directory."