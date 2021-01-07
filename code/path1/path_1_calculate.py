# Path one calculation program


class Path1Calculate:
    """ Path 1 class """
    def __init__(self):
        self.firstRes = dict()

    def addtwodimdict(self, thedict, key_a, key_b, val):
        """ Using double dictionary structure to save data """
        if key_a in thedict:
            thedict[key_a].update({key_b: val})
        else:
            thedict.update({key_a: {key_b: val}})

    def first(self,typedic):
        """ The results were calculated from phenotype to phenotype proteins """
        for key_type in typedic:
            for val_pro in typedic[key_type]:
                self.addtwodimdict(self.firstRes, key_type, val_pro, 1)

    def Calculate(self, typedic, typeSimdic):
        """Path 1 calculate function """
        self.first(typedic)

    def printResult(self, start, end):
        """ Print the result of path 1 """
        if start in self.firstRes and end in self.firstRes[start]:
            print("In the case of path 1, the result from starting point " +
                start + " to protein " + end + " is: " + str(self.firstRes[start][end]))
        else:
            print("There was no relationship between terminal protein " +
                  end + " and starting phenotype " + start + " in path 1, as 0")
    
    def returnData(self):
        """ The result returned is that the starting point is phenotype and the ending is protein  """
        return self.firstRes
