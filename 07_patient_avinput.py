### Python Script to parse txt files and convert them to avinput
### Author: Daniel Brock
### Date 7/13/2023

# Importing required packages
import os
import glob
import re
import pandas as pd
import numpy as np

# Setting working directory
cwd = os.getcwd()
print("Your python script is in this directory: {}".format(cwd))

# List of all patient txt files
patient_txt_files = glob.glob(cwd+"/patient_output/*.txt")

# Looping through each extracted patient txt file 
for f in patient_txt_files:
    try:
        # Reading the df, cleaning up any rows with NA values, and reorganizing/making new columns
        df = pd.read_table(f, sep="\t", na_values=".")
        df = df.dropna(axis=0, how="all") #dropping any rows with all NaN values
        df.columns = ['Chr', 'Start', 'End', 'Ref', 'Alt', 'Geno', 'gnomad_WES', 'gnomad_WGS']
        df[['Genotype', 'alt_reads', 'ref_reads', 'total_reads', 'delete']] = df["Geno"].str.split(":", expand=True)
        
        # Finding allele count, frequency, and number from whole exome seq (WES) data
        gnomad_WES_AC = []
        gnomad_WES_AF = []
        gnomad_WES_AN = []
        for wes in df["gnomad_WES"]:
            try:
                allele_count = float(re.findall(pattern=r"AC:([-+]?\d*\.?\d+(?:[eE][-+]?\d+)?);", string=wes)[0])
                gnomad_WES_AC.append(allele_count)
            except:
                gnomad_WES_AC.append(np.nan)
            try:
                allele_freq = float(re.findall(pattern=r"AF:([-+]?\d*\.?\d+(?:[eE][-+]?\d+)?);", string=wes)[0])
                gnomad_WES_AF.append(allele_freq)
            except:
                gnomad_WES_AF.append(np.nan)
            try:
                allele_number = float(re.findall(pattern=r"AN:([-+]?\d*\.?\d+(?:[eE][-+]?\d+)?);", string=wes)[0])
                gnomad_WES_AN.append(allele_number)
            except:
                gnomad_WES_AN.append(np.nan)
        df["gnomad_WES_AC"] = gnomad_WES_AC
        df["gnomad_WES_AF"] = gnomad_WES_AF
        df["gnomad_WES_AN"] = gnomad_WES_AN
        
        # Finding allele count, frequency, and number from whole genome seq (WGS) data
        gnomad_WGS_AC = []
        gnomad_WGS_AF = []
        gnomad_WGS_AN = []
        for wgs in df["gnomad_WGS"]:
            try:
                allele_count = float(re.findall(pattern=r"AC:([-+]?\d*\.?\d+(?:[eE][-+]?\d+)?);", string=wgs)[0])
                gnomad_WGS_AC.append(allele_count)
            except:
                gnomad_WGS_AC.append(np.nan)
            try:
                allele_freq = float(re.findall(pattern=r"AF:([-+]?\d*\.?\d+(?:[eE][-+]?\d+)?);", string=wgs)[0])
                gnomad_WGS_AF.append(allele_freq)
            except:
                gnomad_WGS_AF.append(np.nan)
            try:
                allele_number = float(re.findall(pattern=r"AN:([-+]?\d*\.?\d+(?:[eE][-+]?\d+)?);", string=wgs)[0])
                gnomad_WGS_AN.append(allele_number)
            except:
                gnomad_WGS_AN.append(np.nan)
        df["gnomad_WGS_AC"] = gnomad_WGS_AC
        df["gnomad_WGS_AF"] = gnomad_WGS_AF
        df["gnomad_WGS_AN"] = gnomad_WGS_AN
        
        # Deleting unessesary columns
        df = df.drop(["delete", "gnomad_WES", "gnomad_WGS"], axis=1)
        
        # Converting start/end and other columns to integers (otherwise ANNOVAR won't work)
        df[["Start", "End", "alt_reads", "ref_reads", "total_reads"]] = df[["Start", "End", "alt_reads", "ref_reads", "total_reads"]].astype(int)
        
        # Making a patient ID column
        patient_ID = f.split("/")[-1].replace(".txt", "")
        df["Patient_ID"] = patient_ID
        
        # Reorganizing columns
        df = df[['Chr', 'Start', 'End', 'Ref', 'Alt', 'Patient_ID', 'Geno', 'Genotype', 'alt_reads', 'ref_reads', 'total_reads', 
                'gnomad_WES_AC', 'gnomad_WGS_AC', 'gnomad_WES_AF', 'gnomad_WGS_AF', 'gnomad_WES_AN', 'gnomad_WGS_AN']]
        
        # Displaying the results
        print("\n"+patient_ID)
        print(df.shape)
        print(df.head())

        # Exporting to avinput (input for ANNOVAR)
        df.to_csv(cwd+"/patient_output/"+patient_ID+".avinput", sep="\t", header=False, index=False)

    # Except to catch .final.analysis files with no data in them
    except:
        print("{} failed table parsing, likely due to no input in .final.analysis file".format(f))

print("\nDone with Python Script")