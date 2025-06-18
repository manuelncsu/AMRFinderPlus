# AMR/virulence genes identification using AMRFinderPlus

## Create a new environment and install AMRFinderPlus using Mamba
mamba create -n amrfinder \
             python=3.11 \
             ncbi-amrfinderplus \
             -y

## activate it whenever you want to run the tool
conda activate amrfinder

## Before running the bash code
create a folder called "genomes" and add the following three genome annotation files (.fna.gz, .faa.gz, and .gff.gz). 
One for each isolate.

Run the bash code
Enjoy!
