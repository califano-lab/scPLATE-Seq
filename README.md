# This repository contains Python scripts used for scPLATE-Seq data processing
# 
#
# demultiplex.py
# Python scripts for demultiplexing sequencing result into individual .fastq files corresponding to each well
# Inputs:
# --workDir, -d: Working directory
# --barcodeInfo, -i: Tab-delimated text file specifying barcode-well correspondence, with barcodes (8nt) in 1st and wells in 2nd column
# --seqFastq, -s: Multiplexed sequencing result in .fastq file containing the mappable (5') reads
# --barcodeFastq. -b: Multiplexed sequencing result in .fastq file containing the barcoding (3') reads
# --prefix, -p: Prefix of demultiplexed .fastq files
# Output:
# Individual .fastq files corresponding to each well
#
#
# CountUMI.py
# Python scripts for measuring transcripts per gene and mapped reads per gene for single well
# Input:
# --samFile, -i: Result of STAR alignment with option --quantMode TranscriptomeSAM and --clip5pNbases 8 (8nt unmappable barcodes)
# --umiFile, -u: Name of file containing transcripts per gene
# countFile, -c: Name of file containing mapped reads per gene
# --lenUMI, -l: UMI length
# hammingThreshold, -t: Hamming distance correction threshold, under which two UMIs are considered as from the same transcript, 0 if not applying hamming distance correction
# Outputs:
# Tab-delimated text files containing transcripts per gene and mapped reads per gene, with genes in 1st and values in 2nd column
