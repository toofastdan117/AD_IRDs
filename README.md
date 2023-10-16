# Autosomal Dominant Inherited Retinal Disease Missense Classifier Benchmarking
### Date Created: 10/6/2023
### Author: Daniel Brock
### Purpose: To benchmark newer missense classifiers against older, historically used classifiers and to identify autosomal dominant (AD) inherited retinal diseases (IRDs) in a cohort of undiagnosed patients. 

**Descriptions of what individual scripts accomplish:**

1. ClinVar_VCF_Parser.ipynb: Parses through a VCF file from ClinVar and selects variants as described in the methods.
2. annovar_script.sh: Annotates variants from ClinVar using ANNOVAR.
3. ClinVar_ROC_AUC_calcs.ipynb: Calculates ROC and AUC for each model and exports results as csv files.
4. ClinVar_ROC_AUC_plotter.Rmd: Plotting ROC Curves using ggplot.
5. classifier_thresholds.ipynb: Calculates min and max thresholds for labeling variants as likely-pathogenic or likely-benign for the top-performing classifiers.
6. patient_parser.sh, patient_avinput.py, and patient_concatenator.py: Annotates 1,013 IRD patient variants using ANNOVAR and exports results as a csv.
7. Patient_Analysis.Rmd and Patient_Analysis.ipynb: Plotting trends in how patient variants were classified.

The main results of the benchmarking can be summarized in figure 2: 

![Figure 2 ROC-AUC](figures/Artboard%202.jpg)