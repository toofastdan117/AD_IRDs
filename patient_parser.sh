#!/bin/sh

### Script to parse "final.analysis" patient files to annotated ANNOVAR csv files

# Entering the filepaths of the directory with patient "final.analysis" files, output folders, and ANNOVAR
patient_data_folder="/home/reach17/Documents/BCM/lab_rotations/Chen/AD_IRD_Predictor/2023-07-10_patient_MutScore_annotation/patient_data/"
patient_output_folder="/home/reach17/Documents/BCM/lab_rotations/Chen/AD_IRD_Predictor/2023-07-10_patient_MutScore_annotation/patient_output/"
patient_annovar_folder="/home/reach17/Documents/BCM/lab_rotations/Chen/AD_IRD_Predictor/2023-07-10_patient_MutScore_annotation/annovar_results/"
ANNOVAR="/home/reach17/Documents/BCM/lab_rotations/Chen/AD_IRD_Predictor/ANNOVAR/"

# Selecting only files with the extension ".final.analysis" within patient_data_folder
patient_files=$(ls $patient_data_folder | grep ".final.analysis")

# Looping for each patient file to extract the first 4 columns and drop any rows after encountering blanks rows (before duplicates)
for i in $patient_files
do
    #echo $i
    patient_id=$(echo $i | sed 's/\.final\.analysis$//')
    awk -F"\t" '{OFS="\t"; print $1, $2, $2, $3, $4, $5, $49, $50} /^$/{exit}' ${patient_data_folder}/${i} > ${patient_output_folder}/${patient_id}.txt
    echo "Extracted: $patient_id"
done

# Running a python script to clean exported txt files and convert to avinput
python patient_avinput.py
rm ${patient_output_folder}*.txt  #removing temporary txt files



### Running ANNOVAR on avinput files

# Selecting only files with the extension ".avinput" within patient_output_folder
patient_avinput_files=$(ls $patient_output_folder | grep ".avinput")

# Looping for each patient's avinput file and annotating with MutScore using ANNOVAR
for i in $patient_avinput_files
do
    #echo $i
    patient_id=$(echo $i | sed 's/\.avinput$//')
    echo "Running ANNOVAR on $patient_id"
    perl ${ANNOVAR}table_annovar.pl ${patient_output_folder}${i} ${ANNOVAR}humandb/ -buildver hg19 -out ${patient_annovar_folder}${patient_id} -remove -protocol refGene,dbscsnv11,dbnsfp42a,mutscore -operation gx,f,f,f -nastring . -csvout -polish -xref ${ANNOVAR}example/gene_xref.txt
done

rm ${patient_annovar_folder}*.invalid_input #removing invalid inputs to tidy things up

# Running a python script to merge all annotated patient data into a central csv
python patient_concatenator.py

# Finishing the script
echo "\nDone with patient variant extraction & annotation!"