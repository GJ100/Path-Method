# -*- coding: utf-8 -*-
# @Author  : JianGao
# @FileName: CalaulateMain.py
# @Software: VS Code
# @System: Windows 10 64-Bit
# @Environment:Python 3.7.5 based on Anaconda
from path1 import path_1_calculate
from path2 import path_2_calculate
from path3 import path_3_calculate
from path4 import path_4_calculate
from similarity import similarityCalculate
import pandas as pd
import time
import csv
import os


ROOT_PATH = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))
start = time.time()
""" 分别导入各路径计算程序 """


class PathCalculateMain:
    def __init__(self):
        self.typedic = dict()  # phenotype dic
        self.typeSimdic = dict()  # typeSim dic
        self.networkdic = dict()  # nertwork dic
        self.similary = similarityCalculate.Similarity_Calculate()  # calculate phenotypic similarity
        self.path_1 = path_1_calculate.Path1Calculate()
        self.path_2 = path_2_calculate.Path2Calculate()
        self.path_3 = path_3_calculate.Path3Calculate()
        self.path_4 = path_4_calculate.Path4Calculate()

    def readFiles(self):
        # Place phenotype file location here
        phenotype = pd.read_csv(os.path.join(ROOT_PATH, u'network\\ID_Supp-S1.csv'))
        # Place network file location here
        with open(os.path.join(ROOT_PATH, u'example\\ID_Combine_Score_Test.csv'),'r',newline='',encoding='utf-8') as f1:
            network = list(csv.reader(f1))
        f1.close()
        return phenotype, network

    def addDict(self, thedict, key_a, val):
        """ Using dictionary structure to save data """
        if key_a in thedict:
            thedict[key_a].update({val})
        else:
            thedict.update({key_a: {val}})

    def addtwodimdict(self, thedict, key_a, key_b, val):
        """ Using double dictionary structure to save data """
        if key_a in thedict:
            thedict[key_a].update({key_b: val})
        else:
            thedict.update({key_a: {key_b: val}})

    def createDict(self, phenotype, typeSim, network):
        """ Generate data into dictionary structure """
        for i in range(len(phenotype)):
            self.addDict(self.typedic, phenotype['type'][i], phenotype['ID'][i])
        print("phenotype dic has done")
        for j in range(len(typeSim)):
            self.addtwodimdict(self.typeSimdic, typeSim[j][0], typeSim[j][1], typeSim[j][2])
        print("typeSim dic has done")
        for k in range(1, len(network)):
            self.addtwodimdict(self.networkdic, network[k][3], network[k][4], network[k][2])
        print("network dic has done")

    def Protein(self, start, end, length, typedic, typeSimdic, networkdic):
        """ Call different path calculation functions according to different paths """
        if length == 1:
            self.path_1.Calculate(typedic, typeSimdic)
            self.path_1.printResult(start, end)
        if length == 2:
            self.path_2.Calculate(typedic, typeSimdic, networkdic)
            self.path_2.printResult(start, end)
        if length == 3:
            self.path_3.Calculate(typedic, typeSimdic, networkdic)
            self.path_3.printResult(start, end)
        if length == 4:
            self.path_4.Calculate(typedic, typeSimdic, networkdic)
            self.path_4.printResult(start, end)


if __name__ == "__main__":
    # The starting point is phenotype
    s = 'A'
    # The end point is protein
    e = '2271'
    # L is the path length
    L = 2
    obj_path = PathCalculateMain()
    phenotype, network = obj_path.readFiles()
    typeSim = obj_path.similary.dataProcess(phenotype)
    obj_path.createDict(phenotype, typeSim, network)
    obj_path.Protein(s, e, L, obj_path.typedic, obj_path.typeSimdic, obj_path.networkdic)
    # result is 195.001124

endtime = time.time()
print("This calculation takes " + str(endtime - start) + " second")
