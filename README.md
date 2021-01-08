
# 										Abstract

Identification of protein phenotype is an essential and challenge problem in modern genetics. Such problem is related to some serious diseases, including cancers, HIV and so on. The factors of genotype and environment increase the difficulties in determining the phenotype of proteins. The experiment methods to achieve such goal are always time-consuming and expensive. In this study, we proposed a network computational method to identify novel phenotypic annotations of proteins. To execute such method, a heterogeneous network was constructed, which contained three sub-networks: protein network, phenotypic type network, and protein-phenotypic type network. The method tried to find out all paths with limited length, which connected one protein and one phenotypic type. A scoring scheme was adopted to count obtained paths and induced a score to indicate the associations between them. The ROC and PR curve analyses were done to evaluate the performance of the method, indicating the utility of the method. Finally, our method was superior to other network methods, which incorporated popular network algorithms.

![Figure-3](https://github.com/GJ100/Path-Method/blob/main/Figure%203.jpg)

### This program is to evaluate the association between one protein and one phenotype in a heterogeneous network. Relevant explanations are as follows:

## 1. About files

##### The network data for running the program are placed in the “network” folder of the project. Due to the large size of the network, which need long time to run the program, we also provide small network data that are available in the “example” folder. All data files are in csv format (with comma as the separator). For concision, eleven phenotypes are coded by letters from A to K, respectively, and proteins are numbered by integers between 0 and 6573. The description of each document is as follows:

a. Supp-S1.csv: Validated association between proteins and phenotypes.

b. ID_Supp-S1.csv: Validated association between proteins and phenotypes, where proteins are encoded by integers and phenotypes are represented by letters. 

c. Combine_Score.csv: The data file containing the edge information of the network. 

d. ID_Combine_Score.csv: The data file containing the edge information of the network, where proteins are encoded by integers and phenotypes are represented by letters. 

e. ID_Combine_Score_Test.csv: The data file for the small network. 

## 2. About the program

### a. Environment:

Windows 10 64-bit

Anaconda with Python 3.7.5 version

Compiler with VS Code

### b. Input:

One phenotype

One protein

The path length limitation parameter

Network data file

### c. Output 

The association score of the input.

## Reference

Jian Gao, Bin Hu, Lei Chen, A path-based method for identification of protein phenotypic annotations, submitted.
