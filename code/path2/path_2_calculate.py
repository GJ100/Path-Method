# Path two calculation program

from path1 import path_1_calculate
from functools import reduce


class Path2Calculate:
    def __init__(self):
        self.firstRes = dict()
        self.secondRes = dict()
        self.returnRes = dict()  # return the result for the next path calculation

    def addtwodimdict(self, thedict, key_a, key_b, val):
        """ Using double dictionary structure to save data """
        if key_a in thedict:
            thedict[key_a].update({key_b: val})
        else:
            thedict.update({key_a: {key_b: val}})

    def getScores(self, w1, w2):
        """ Calculate the score of the corresponding path """
        Fw = 2.26 * 2
        score = round((float(w1) * float(w2)) ** Fw,
                      6)  # Keep six decimal places
        return score

    def first(self, typedic, typeSimdic):
        """
        The results from phenotype to phenotype were calculated
        Implementation of "A->B->Bpros"
        """
        for key_a in typedic:
            for key_b in typedic:
                if key_a != key_b:
                    for pro_b in typedic[key_b]:
                        if key_a in self.firstRes and pro_b in self.firstRes[key_a]:
                            self.firstRes[key_a][pro_b] += float(
                                self.getScores(typeSimdic[key_a][key_b], 1))
                        else:
                            self.addtwodimdict(self.firstRes, key_a, pro_b, self.getScores(
                                typeSimdic[key_a][key_b], 1))

    def second(self, typedic, networkdic):
        """
        The results from phenotype to phenotype were calculated
        Implementation of "A->A.pros->pro2"
        """
        for key_a in typedic:
            for pro_a in typedic[key_a]:
                if pro_a in networkdic:
                    for pro2 in networkdic[pro_a]:
                        if key_a in self.secondRes and pro2 in self.secondRes[key_a]:
                            self.secondRes[key_a][pro2] += float(self.getScores(1, networkdic[pro_a][pro2]))
                        else:
                            self.addtwodimdict(self.secondRes, key_a, pro2, self.getScores(1, networkdic[pro_a][pro2]))

    def Calculate(self, typedic, typeSimdic, networkdic):
        """Path 2 calculate function """
        # get the return result of path1
        path1 = path_1_calculate.Path1Calculate()
        path1.Calculate(typedic, typeSimdic)
        res1 = path1.returnData()
        self.first(typedic, typeSimdic)  # A->B->Bpros
        self.second(typedic, networkdic)  # A->Apros->pro2
        self.returnRes = reduce(self.MergeDictionary, [self.firstRes, self.secondRes, res1])

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
            print("In the case of path 2, the result from starting point " +
                  start + " to protein " + end + " is: " + str(self.returnRes[start][end]))
        else:
            print("There was no relationship between terminal protein " +
                  end + " and starting phenotype " + start + " in path 2, as 0")

    def returnData(self):
        """ The result returned is that the starting point is phenotype and the ending is protein """
        return self.returnRes
