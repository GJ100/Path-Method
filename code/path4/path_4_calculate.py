# Path four calculation program

from path3 import path_3_calculate
from functools import reduce


class Path4Calculate:
    def __init__(self):
        self.firstRes = dict()
        self.secondRes = dict()
        self.thirdRes = dict()
        self.fourthRes = dict()
        self.fifthRes = dict()
        self.sixthRes = dict()
        self.seventhRes = dict()
        self.eighthRes = dict()
        self.returnRes = dict()

    def addtwodimdict(self, thedict, key_a, key_b, val):
        """ Using double dictionary structure to save data """
        if key_a in thedict:
            thedict[key_a].update({key_b: val})
        else:
            thedict.update({key_a: {key_b: val}})

    def getScores(self, w1, w2, w3, w4):
        """ Calculate the score of the corresponding path """
        Fw = 2.26 * 4
        # Keep six decimal places
        score = round((float(w1) * float(w2) * float(w3) * float(w4)) ** Fw, 6)
        return score

    def first(self, typedic, typeSimdic):
        """
        The results from phenotype to phenotype were calculated
        Implementation of "A->B->C->D->Dpros"
        """
        for key_a in typedic:
            for key_b in typedic:
                if key_a != key_b:
                    for key_c in typedic:
                        if key_a != key_c and key_b != key_c:
                            for key_d in typedic:
                                if key_a != key_d and key_b != key_d and key_c != key_d:
                                    for pro_d in typedic[key_d]:
                                        if key_a in self.firstRes and pro_d in self.firstRes[key_a]:
                                            self.firstRes[key_a][pro_d] = self.firstRes[key_a][pro_d] + float(self.getScores(
                                                typeSimdic[key_a][key_b], typeSimdic[key_b][key_c], typeSimdic[key_c][key_d], 1))
                                        else:
                                            self.addtwodimdict(self.firstRes, key_a, pro_d, self.getScores(
                                                typeSimdic[key_a][key_b], typeSimdic[key_b][key_c], typeSimdic[key_c][key_d], 1))

    def second(self, typedic, typeSimdic, networkdic):
        """
        The results from phenotype to phenotype were calculated
        Implementation of "A->B->C->Cpros->pro2"
        """
        for key_a in typedic:
            for key_b in typedic:
                if key_a != key_b:
                    for key_c in typedic:
                        if key_a != key_c and key_b != key_c:
                            for pro_c in typedic[key_c]:
                                if pro_c in networkdic:
                                    for pro_2 in networkdic[pro_c]:
                                        if key_a in self.secondRes and pro_2 in self.secondRes[key_a]:
                                            self.secondRes[key_a][pro_2] = self.secondRes[key_a][pro_2] + float(self.getScores(
                                                typeSimdic[key_a][key_b], typeSimdic[key_b][key_c], 1, networkdic[pro_c][pro_2]))
                                        else:
                                            self.addtwodimdict(self.secondRes, key_a, pro_c, self.getScores(
                                                typeSimdic[key_a][key_b], typeSimdic[key_b][key_c], 1, networkdic[pro_c][pro_2]))

    def third(self, typedic, typeSimdic):
        """
        The results from phenotype to phenotype were calculated
        Implementation of "A->B->Bpros->C->Cpros"
        """
        for key_a in typedic:
            for key_b in typedic:
                if key_a != key_b:
                    for key_c in typedic:
                        if key_a != key_c and key_b != key_c:
                            for pro_b in typedic[key_b]:
                                if pro_b in typedic[key_c]:
                                    for pro_c in typedic[key_c]:
                                        if pro_b != pro_c:
                                            if key_a in self.thirdRes and pro_c in self.thirdRes[key_a]:
                                                self.thirdRes[key_a][pro_c] += float(
                                                    self.getScores(typeSimdic[key_a][key_b], 1, 1, 1))
                                            else:
                                                self.addtwodimdict(self.thirdRes, key_a, pro_c, float(
                                                    self.getScores(typeSimdic[key_a][key_b], 1, 1, 1)))

    def fourth(self, typedic, typeSimdic, networkdic):
        """
        The results from phenotype to phenotype were calculated
        Implementation of "A->B->Bpros->pro2->pro2_2"
        """
        for key_a in typedic:
            for key_b in typedic:
                if key_a != key_b:
                    for pro_b in typedic[key_b]:
                        if pro_b in networkdic:
                            for pro2 in networkdic[pro_b]:
                                if pro2 in networkdic:
                                    for pro2_2 in networkdic[pro2]:
                                        if pro2_2 != pro_b:
                                            if key_a in self.fourthRes and pro2_2 in self.fourthRes[key_a]:
                                                self.fourthRes[key_a][pro2_2] += float(self.getScores(
                                                    typeSimdic[key_a][key_b], 1, networkdic[pro_b][pro2], networkdic[pro2][pro2_2]))
                                            else:
                                                self.addtwodimdict(self.fourthRes, key_a, pro2_2, self.getScores(
                                                    typeSimdic[key_a][key_b], 1, networkdic[pro_b][pro2], networkdic[pro2][pro2_2]))

    def fifth(self, typedic, typeSimdic):
        """
        The results from phenotype to phenotype were calculated
        Implementation of "A->Apros->B->C->Cpros"
        """
        for key_a in typedic:
            for key_b in typedic:
                if key_a != key_b:
                    for pro_a in typedic[key_a]:
                        if pro_a in typedic[key_b]:
                            for key_c in typedic:
                                if key_a != key_c and key_b != key_c:
                                    for pro_c in typedic[key_c]:
                                        if key_a in self.fifthRes and pro_c in self.fifthRes[key_a]:
                                            self.fifthRes[key_a][pro_c] += float(
                                                self.getScores(1, 1, typeSimdic[key_b][key_c], 1))
                                        else:
                                            self.addtwodimdict(self.fifthRes, key_a, pro_c, self.getScores(
                                                1, 1, typeSimdic[key_b][key_c], 1))

    def sixth(self, typedic, typeSimdic, networkdic):
        """
        The results from phenotype to phenotype were calculated
        Implementation of "A->Apros->B->Bpros->pro2"
        """
        for key_a in typedic:
            for key_b in typedic:
                if key_a != key_b:
                    for pro_a in typedic[key_a]:
                        if pro_a in typedic[key_b]:
                            for pro_b in typedic[key_b]:
                                if pro_a != pro_b:
                                    if pro_b in networkdic:
                                        for pro2 in networkdic[pro_b]:
                                            if key_a in self.sixthRes and pro2 in self.sixthRes[key_a]:
                                                self.sixthRes[key_a][pro2] += float(
                                                    self.getScores(1, 1, 1, networkdic[pro_b][pro2]))
                                            else:
                                                self.addtwodimdict(
                                                    self.sixthRes, key_a, pro2, self.getScores(1, 1, 1, networkdic[pro_b][pro2]))

    def seventh(self, typedic, networkdic):
        """
        The results from phenotype to phenotype were calculated
        Implementation of "A->Apros->pro2->B->Bpros"
        """
        for key_a in typedic:
            for pro_a in typedic[key_a]:
                if pro_a in networkdic:
                    for pro2 in networkdic[pro_a]:
                        for key_b in typedic:
                            if key_a != key_b and pro2 in typedic[key_b]:
                                for pro_b in typedic[key_b]:
                                    if key_a in self.seventhRes and pro_b in self.seventhRes[key_a]:
                                        self.seventhRes[key_a][pro_b] += float(
                                            self.getScores(1, networkdic[pro_a][pro2], 1, 1))
                                    else:
                                        self.addtwodimdict(self.seventhRes, key_a, key_b, float(
                                            self.getScores(1, networkdic[pro_a][pro2], 1, 1)))

    def eighth(self, typedic, networkdic):
        """
        The results from phenotype to phenotype were calculated
        Implementation of "A->Apros->pro2->pro2_2->pro2_3"
        """
        for key_a in typedic:
            for pro_a in typedic[key_a]:
                if pro_a in networkdic:
                    for pro2 in networkdic[pro_a]:
                        if pro2 in networkdic:
                            for pro2_2 in networkdic[pro2]:
                                if pro2_2 != pro_a and pro2_2 in networkdic:
                                    for pro2_3 in networkdic[pro2_2]:
                                        if key_a in self.eighthRes and pro2_3 in self.eighthRes[key_a]:
                                            self.eighthRes[key_a][pro2_3] += float(self.getScores(
                                                1, networkdic[pro_a][pro2], networkdic[pro2][pro2_2], networkdic[pro2_2][pro2_3]))
                                        else:
                                            self.addtwodimdict(self.eighthRes, key_a, pro2_3, self.getScores(
                                                1, networkdic[pro_a][pro2], networkdic[pro2][pro2_2], networkdic[pro2_2][pro2_3]))

    def Calculate(self, typedic, typeSimdic, networkdic):
        """Path 4 calculate function """
        # get the return result of path3
        path3 = path_3_calculate.Path3Calculate()
        path3.Calculate(typedic, typeSimdic, networkdic)
        res3 = path3.returnData()
        self.first(typedic, typeSimdic)  # A->B->C->D->Dpros
        self.second(typedic, typeSimdic, networkdic)  # A->B->C->Cpros->pro2
        self.third(typedic, typeSimdic)  # A->B->Bpros->C->Cpros
        # A->B->Bpros->pro2->pro2_2
        self.fourth(typedic, typeSimdic, networkdic)
        self.fifth(typedic, typeSimdic)  # A->Apros->B->C->Cpros
        self.sixth(typedic, typeSimdic, networkdic)  # A->Apros->B->Bpros
        self.seventh(typedic, networkdic)  # A->Apros->pro2->B->Bpros
        self.eighth(typedic, networkdic)  # A->Apros->pro2->pro2_2->pro2_3
        self.returnRes = reduce(self.MergeDictionary,
                                [self.firstRes, self.secondRes, self.thirdRes, self.fourthRes, self.fifthRes, 
                                self.sixthRes, self.seventhRes, self.eighthRes, res3])

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
                  end + " and starting phenotype " + start + " in path 4, as 0")