### Python Script to parse annatated csv files from annovar and merge them into a centralized csv file with a patient ID column
### Author: Daniel Brock
### Date 7/13/2023

# Importing required packages
import os
import glob
import pandas as pd

# Setting working directory
cwd = os.getcwd()
print("\nYour python script is in this directory: {}".format(cwd))



# List of patient avinput files
patient_av_files = glob.glob(cwd+"/patient_output/*.avinput")

# Looping through avinput files, importing dfs, and appending to a list
patient_av_list = []
for av in patient_av_files:
    try:
        df = pd.read_table(av, header=None, names=['Chr', 'Start', 'End', 'Ref', 'Alt', 'Patient_ID', 'Geno', 'Genotype', 
                                                   'alt_reads', 'ref_reads', 'total_reads', 'gnomad_WES_AC', 'gnomad_WGS_AC', 
                                                   'gnomad_WES_AF', 'gnomad_WGS_AF', 'gnomad_WES_AN', 'gnomad_WGS_AN'])
        patient_av_list.append(df)
    except:
        print("{} failed table parsing, likely due to no input in .final.analysis file".format(av))

# Concatenating avinput files
patient_avinput = pd.concat(patient_av_list, axis=0)
print("\nThe shape of the merged avinput files is: {}".format(str(patient_avinput.shape)))



# List of patient annotated csv files from ANNOVAR
annovar_files = glob.glob(cwd+"/annovar_results/*.csv")

# Looping through csv files, importing dfs, and appending to a list
annovar_df_list = []
for ann in annovar_files:
    try:
        patient_id = ann.split("/")[-1].replace(".hg19_multianno.csv", "")
        df = pd.read_csv(ann, na_values=".")
        df["Patient_ID"] = patient_id
        IDs = df.pop("Patient_ID")
        df.insert(5, "Patient_ID", IDs)
        annovar_df_list.append(df)
    except:
        print("{} failed csv parsing, likely due to no input in .final.analysis file".format(ann))

# Concatenating csv ANNOVAR files
patient_annovar = pd.concat(annovar_df_list, axis=0)
print("\nThe shape of the merged annovar files is: {}".format(str(patient_annovar.shape)))



# Merging patient annotated df from ANNOVAR with avinput files to get info about read count and allele frequency
final_df = pd.merge(patient_avinput, patient_annovar, on=['Chr', 'Start', 'End', 'Ref', 'Alt', 'Patient_ID'])



# Displaying finalized results and exporting
print("\nInfo about merged and finalized df:")
print(final_df.shape)
print(final_df.head())
final_df.to_csv(cwd+"/annovar_patient_data.csv", index=False)
print("\nDone with Script!")