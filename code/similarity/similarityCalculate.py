# A program for calculating phenotypic similarity

class Similarity_Calculate:
    # Jaccard相关系数
    def jaccard(self, x, y):
        inter = len(set.intersection(*[set(x), set(y)]))
        union_card = len(set.union(*[set(x), set(y)]))
        return inter/float(union_card)


    def addDict(self, thedict, key_a, val):
        if key_a in thedict:
            thedict[ key_a ].update({val})
        else:
            thedict.update({key_a: {val}})
    
    def dataProcess(self, phenotype):
        typedic = dict()
        for i in range(len(phenotype)):
            self.addDict(typedic, phenotype['type'][i], phenotype['ID'][i])

        result = []
        for key_a in typedic:
            for key_b in typedic:
                result.append([key_a, key_b, self.jaccard(typedic[key_a], typedic[key_b])])
        return result