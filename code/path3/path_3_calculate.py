# Path three calculation program

from path2 import path_2_calculate
from functools import reduce


class Path3Calculate:
    def __init__(self):
        self.firstRes = dict()
        self.secondRes = dict()
        self.thirdRes = dict()
        self.fourthRes = dict()
        self.returnRes = dict()

    def addtwodimdict(self, thedict, key_a, key_b, val):
        """ Using double dictionary structure to save data """
        if key_a in thedict:
            thedict[key_a].update({key_b: val})
        else:
            thedict.update({key_a: {key_b: val}})

    def getScores(self, w1, w2, w3):
        """ Calculate the score of the corresponding path """
        Fw = 2.26 * 3
        score = round((float(w1) * float(w2) * float(w3)) ** Fw, 6)  # Keep six decimal places
        return score

    def first(self, typedic, typeSimdic):
        """
        The results from phenotype to phenotype were calculated
        Implementation of "A->B->C->Cpros"
        """
        for key_a in typedic:
            for key_b in typedic:
                if key_a != key_b:
                    for key_c in typedic:
                        if key_a != key_c and key_b != key_c:
                            for pro_c in typedic[key_c]:
                                if key_a in self.firstRes and pro_c in self.firstRes[key_a]:
                                    self.firstRes[key_a][pro_c] += float(self.getScores(
                                        typeSimdic[key_a][key_b], typeSimdic[key_b][key_c], 1))
                                else:
                                    self.addtwodimdict(self.firstRes, key_a, pro_c, float(
                                        self.getScores(typeSimdic[key_a][key_b], typeSimdic[key_b][key_c], 1)))

    def second(self, typedic, typeSimdic, networkdic):
        """
        The results from phenotype to phenotype were calculated
        Implementation of "A->B->Bpros->pro2"
        """
        for key_a in typedic:
            for key_b in typedic:
                if key_a != key_b:
                    for pro_b in typedic[key_b]:
                        if pro_b in networkdic:
                            for pro2 in networkdic[pro_b]:
                                if key_a in self.secondRes and pro2 in self.secondRes[key_a]:
                                    self.secondRes[key_a][pro2] += float(self.getScores(
                                        typeSimdic[key_a][key_b], 1, networkdic[pro_b][pro2]))
                                else:
                                    self.addtwodimdict(self.secondRes, key_a, pro2, float(
                                        self.getScores(typeSimdic[key_a][key_b], 1, networkdic[pro_b][pro2])))

    def third(self, typedic, typeSimdic):
        """
        The results from phenotype to phenotype were calculated
        Implementation of "A->Apros->B->Bpros"
        """
        for key_a in typedic:
            for key_b in typedic:
                if key_a != key_b:
                    for pro_a in typedic[key_a]:
                        if pro_a in typedic[key_b]:
                            for pro_b in typedic[key_b]:
                                if pro_a != pro_b:
                                    if key_a in self.thirdRes and pro_b in self.thirdRes[key_a]:
                                        self.thirdRes[key_a][pro_b] += float(
                                            self.getScores(1, 1, 1))
                                    else:
                                        self.addtwodimdict(
                                            self.thirdRes, key_a, pro_b, float(self.getScores(1, 1, 1)))

    def fourth(self, typedic, networkdic):
        """
        The results from phenotype to phenotype were calculated
        Implementation of "A->Apros->pro2->pro2_2"
        """
        for key_a in typedic:
            for pro_a in typedic[key_a]:
                if pro_a in networkdic:
                    for pro2 in networkdic[pro_a]:
                        if pro2 in networkdic:
                            for pro2_2 in networkdic[pro2]:
                                if pro2_2 != pro_a and key_a in self.fourthRes and pro2_2 in self.fourthRes[key_a]:
                                    self.fourthRes[key_a][pro2_2] += float(self.getScores(
                                        1, networkdic[pro_a][pro2], networkdic[pro2][pro2_2]))
                                else:
                                    self.addtwodimdict(self.fourthRes, key_a, pro2_2, self.getScores(
                                        1, networkdic[pro_a][pro2], networkdic[pro2][pro2_2]))

    def Calculate(self, typedic, typeSimdic, networkdic):
        """Path 3 calculate function """
        # get the return result of path2
        path2 = path_2_calculate.Path2Calculate()
        path2.Calculate(typedic, typeSimdic, networkdic)
        res2 = path2.returnData()
        self.first(typedic, typeSimdic)  # A->B->C->Cpros
        self.second(typedic, typeSimdic, networkdic)# A->B->Bpros->pro2
        self.third(typedic, typeSimdic)  # A->Apros->B->Bpros
        self.fourth(typedic, networkdic)  # A->Apros->pro2->pro2_2
        self.returnRes = reduce(self.MergeDictionary, [self.firstRes, self.secondRes, self.thirdRes, self.fourthRes, res2])

    def MergeDictionary(self, dict1, dict2):
        """ Merge the result dictionaries """
        for key_2, val_2 in dict2.items():
            for key_2_2, val_2_2 in val_2.items():
                if key_2 in dict1 and key_2_2 in dict1[key_2]:
                    dict1[key_2][key_2_2] += val_2_2
                else:
                    self.addtwodimdict(dict1, key_2, key_2_2, val_2_2)
        return dict1

    def printResult(self, start, end):
        """ Print the result of path 2 """
        if start in self.returnRes and end in self.returnRes[start]:
            print("In the case of path 3, the result from starting point " +
                  start + " to protein " + end + " is: " + str(self.returnRes[start][end]))
        else:
            print("There was no relationship between terminal protein " +
                  end + " and starting phenotype " + start + " in path 3, as 0")

    def returnData(self):
        """ The result returned is that the starting point is phenotype and the ending is protein """
        return self.returnRes
