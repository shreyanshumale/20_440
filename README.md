Overview
This repository contains data/scripts pertaining to the course project for 20.440. This project tries to build upon the model proposed by Łuksza and Lässig to determine fitness values for each strain in a predictive way. The repository contains data, scripts and the corresponding figures. We use data from NextStrain on mutation-summary of around ~400,000 SARS-CoV2 sequences collected over the past 2 years to identify mutational hotpsots in the SPike protein region of the virus.
- Data
We use data from NextStrain on mutation-summary of around ~400,000 SARS-CoV2 sequences collected over the past 2 years to identify mutational hotpsots in the SPike protein region of the virus. 
- Folder structure
The data/ folder contains strain a tree file for phylogeny of the strains and a download_links.txt file that has links to the mutation-summary.tsv and aligned-sequences.fasta.xz files on the nextstrain server. The user must download these and store them in the data folder in thier local cloned repos before running the scripts.
- Installation
The scripts are written in python and require a working python3 with seaborn, matplotlib and pandas packages as additional dependencies.

Citations:
1. Łuksza et al., (Nature 2014) https://www.nature.com/articles/nature13087
2. Hadfield et al. (Bioinformatics 2018) https://academic.oup.com/bioinformatics/article/34/23/4121/5001388?login=true

