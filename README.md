English|中文

# 										Abstract

Identification of protein phenotype is an essential and challenge problem in modern genetics. Such problem is related to some serious diseases, including cancers, HIV and so on. The factors of genotype and environment increase the difficulties in determining the phenotype of proteins. The experiment methods to achieve such goal are always time-consuming and expensive. In this study, we proposed a network computational method to identify novel phenotypic annotations of proteins. To execute such method, a heterogeneous network was constructed, which contained three sub-networks: protein network, phenotypic type network, and protein-phenotypic type network. The method tried to find out all paths with limited length, which connected one protein and one phenotypic type. A scoring scheme was adopted to count obtained paths and induced a score to indicate the associations between them. The ROC and PR curve analyses were done to evaluate the performance of the method, indicating the utility of the method. Finally, our method was superior to other network methods, which incorporated popular network algorithms.



### This program is used to calculate the matching value in each path starting from phenotype and ending at protein, Relevant explanations are as follows:

## 1. About files

##### The files needed for running the program are placed in the network folder of the project, the test file data is placed in the example folder, and all file formats are in csv format (with',' as the separator). For the convenience of calculation, the phenotype number is from A to K, and the protein number From 0 to 6573, each document is explained as follows:

a.	Supp-S1.csv: Eleven phenotypes and their annotation proteins

b.	ID_Supp-S1.csv: Phenotype with renumbering and its annotated protein

c.	Combine_Score.csv: The binding value between each protein in the protein network

d.	ID_Combine_Score.csv: The binding value between each protein in the protein network with renumbering

e.	ID_Combine_Score_Test.csv: In order to save test time, 300 data selected from the "ID_Combine_Score.csv" file are used for testing.

## 2. About the program

### a. Environment:

The environment used by the program is: Windows 10 64-bit, based on Anaconda's Python 3.7.5 version, and the compiler uses VS Code.

### b. Input:

You need to give a starting phenotype and an ending protein. If you use renumbered files, such as phenotype:'A' and protein: '2271', if you use original data files, such as phenotype: ‘Conditional phenotypes’ and protein: 'YAL002W', plus which path needs to be calculated, such as: 4

##### *Note: If you do not use renumbered files, please replace the read files with unnumbered files in the program*

### c. Output 

The matching value of this path is based on the input phenotype as the starting point and the input protein as the end point.

### d. Notes on the program:

The annotation in the program such as: A->Apros->pro2, which means that the starting point is phenotype A, and the end point is the protein on the protein network when the annotation protein of phenotype A reaches

### e. Remarks

The program provides a copy of test data. In order to facilitate inspection and testing, it takes a lot of time to verify the complete data (estimated from half a month)









### 本程序是用来计算起点为表型，终点是蛋白的在各路径下的匹配值，相关说明如下：

## 1. 关于文件

##### 程序运行所需要的文件都放在该项目network文件夹中，测试文件数据放在example文件夹中，且所有文件格式都是csv格式（以’,‘为间隔符），为了方便计算，将表型编号为从A到K，蛋白编号为0到6573，各文件解释如下：

a.	Supp-S1.csv：十一个表型与其注释蛋白

b.	ID_Supp-S1.csv：带有重新编号的表型与其注释蛋白

c.	Combine_Score.csv：蛋白网络中每个蛋白之间的结合值

d.	ID_Combine_Score.csv：带有重新编号的蛋白网络中每个蛋白之间的结合值

e.	ID_Combine_Score_Test.csv：为了节省测试时间，从“ID_Combine_Score.csv”文件中选取的300个数据进行测试使用。

## 2. 关于程序

### a. 环境：

该程序所使用环境为：Windows 10 64-bit，基于Anaconda的Python 3.7.5版本，编译器使用的是 VS Code。

### b. 输入：

需要给定一个起点表型和一个终点蛋白，如果你使用重新编号的文件，如表型：‘A’和蛋白：’2271’，如果你使用原数据文件，如表型‘Conditional phenotypes’和蛋白：‘YAL002W’，再加上需要在哪条路径下计算，如：4

注意：如果不使用重新编号的文件，请在程序中将读取的文件替换成未编号的文件

### c. 输出：

以该起点和该终点在这条路径下的匹配值。

### d. 注释：

程序中的注释如：A->Apros->pro2，代表着起点是表型A，通过表型A的注释蛋白到达终点为蛋白网络上的蛋白

## 3. 备注：

该程序提供了一份测试数据，为了方便检验和测试，如需验证完整的数据需要大量的时间（估算半个月起）
