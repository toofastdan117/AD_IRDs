# Autosomal Dominant Inherited Retinal Disease Missense Classifier Benchmarking
### Date Created: 10/6/2023
### Author: Daniel Brock
### Publication: Comparative analysis of in-silico tools in identifying pathogenic variants in dominant inherited retinal diseases. **Brock DC**, Wang M, Hussain HMJ, Rauch DE, Marra M, Pennesi ME, Yang P, Everett L, Ajlan RS, Colbert J, Porto FBO, Matynia A, Gorin MB, Koenekoop RK, Lopez I, Sui R, Zou G, Li Y, Chen R. *Human Molecular Genetics*. March 7, 2024. [doi:10.1093/hmg/ddae028](https://doi.org/10.1093/hmg/ddae028)
### Purpose: To benchmark newer missense classifiers against older, historically used classifiers and to identify autosomal dominant (AD) inherited retinal diseases (IRDs) in a cohort of undiagnosed patients. 

**Descriptions of what individual scripts accomplish:**

1. 01_ClinVar_VCF_Parser.ipynb: Parses through a VCF file from ClinVar and selects variants as described in the methods.
2. 02_annovar_script.sh: Annotates variants from ClinVar using ANNOVAR.
3. 03_ClinVar_ROC_AUC_calcs.ipynb: Calculates ROC and AUC for each model and exports results as csv files.
4. 04_ClinVar_ROC_AUC_plotter.Rmd: Plotting ROC Curves using ggplot.
5. 05_classifier_thresholds.ipynb: Calculates min and max thresholds for labeling variants as likely-pathogenic or likely-benign for the top-performing classifiers.
6. 06_patient_parser.sh, 07_patient_avinput.py, and 08_patient_concatenator.py: Annotates 1,013 IRD patient variants using ANNOVAR and exports results as a csv.
7. 09_Patient_Analysis.ipynb and 10_Patient_Analysis.Rmd: Plotting trends in how patient variants were classified.

The main results of the benchmarking can be summarized in Figure 2: 

![Figure 2 ROC-AUC](figures/Figure%202_GitHub.jpg)