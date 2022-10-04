# 10/03/2022 8:47PM
# Class Molgraph for bonds from Tripos MOL2 files

# graph class from https://medium.com/geekculture/how-to-represent-a-graph-data-structure-in-python-9f0df57e33a2
# undirected, weighted graph


class MolGraph:

    def __init__(self, mol2mol):
        self.graph = dict()

        for atom in mol2mol.atoms:
            self.graph[atom.AtInd] = []

        for bond in mol2mol.bonds:
            self.graph[bond.BdAt1].append((bond.BdAt2, bond.BdType))
            self.graph[bond.BdAt2].append((bond.BdAt1, bond.BdType))

    def isbonded(self,a1,a2):
        return a2.AtInd in [x[0] for x in self.graph[a1.AtInd]]

    def isbondedby(self,a1,a2,btype):
        return (a2.AtInd,btype) in self.graph[a1.AtInd]

    def countbond(self,a,btype):
        return len([x for x in self.graph[a.AtInd] if x[1]==btype])

    def returnbonds(self,a):
        return self.graph[a.AtInd]