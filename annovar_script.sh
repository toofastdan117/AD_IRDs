#!/bin/sh

### Script to run ANNOVAR ###

# File dictortory to ANNOVAR folder
ANNOVAR="/home/reach17/Documents/BCM/lab_rotations/Chen/AD_IRD_Predictor/ANNOVAR/"

# File directory to input/output folder
input_output="/home/reach17/Documents/BCM/lab_rotations/Chen/AD_IRD_Predictor/manuscript/GitHub/annovar_files/"

# Selecting only files with the extension ".avinput" within input_output directory
avinput_files=$(ls $input_output | grep ".avinput")
echo $avinput_files

# Looping for each patient's avinput file and annotating with MutScore using ANNOVAR
perl ${ANNOVAR}table_annovar.pl ${input_output}${avinput_files} ${ANNOVAR}humandb/ -buildver hg19 -out ${input_output}clinvar_filt_retnet_annotated -remove -protocol refGene,dbscsnv11,dbnsfp42a,mutscore -operation gx,f,f,f -nastring . -csvout -polish -xref ${ANNOVAR}example/gene_xref.txt

# Finishing the script
echo "\nDone with ANNOVAR annotation!"