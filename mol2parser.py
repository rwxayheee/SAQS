# 10/03/2022 6:47PM
# Parsing Tripos MOL2 files generated from MOE Dock (io_trps.svl 2020.11)

from mol2molclass import Atom, Bond
from auxclass import MolGraph


class Pose:

    def __init__(self, mol2block):
        self.datablock = mol2block

        self.atomblock = mol2block[mol2block.index('@<TRIPOS>ATOM\n') + 1:\
                                   mol2block.index('@<TRIPOS>BOND\n')]
        self.atoms = []
        for line in self.atomblock:
            self.atoms.append(Atom(line))

        atom_dic = {}
        for atom in self.atoms:
            atom_dic[atom.AtInd] = atom
        self.atomdic = atom_dic

        self.bondblock = mol2block[mol2block.index('@<TRIPOS>BOND\n') + 1:\
                                   mol2block.index('@<TRIPOS>SUBSTRUCTURE\n')]
        self.bonds = []
        for line in self.bondblock:
            self.bonds.append(Bond(line))

        self.propertyblock = mol2block[mol2block.index('@<TRIPOS>PROPERTY_DATA\n') + 1:]

        prop_dic = {}
        for line in self.propertyblock:
            if '\t|\t' in line:
                items = line.split('\t|\t')
                if len(items) > 1:
                    prop_dic[items[0]] = ','.join(items[1])
                else:
                    prop_dic[items[0]] = ''
        self.propertydic = prop_dic

        self.molgraph = MolGraph(self)


def splitmol2(mol2file):

    with open(mol2file, 'r') as f:
        datalines = f.readlines()

    poselist = []
    singleblock = []
    for line in datalines:
        if line == '@<TRIPOS>MOLECULE\n':
            if len(singleblock) > 0:
                poselist.append(Pose(singleblock))
                singleblock = []
        singleblock.append(line)
    if len(singleblock) > 0:
        poselist.append(Pose(singleblock))

    return poselist
