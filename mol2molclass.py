# 10/03/2022 7:51PM
# Atom, Bond

import numpy as np


class Atom:

    def __init__(self, atom_info):
        items = atom_info.split()
        self.AtInd = items[0]
        self.AtName = items[1]
        self.AtCoord = np.array([float(x) for x in items[2:5]])
        self.AtType = items[5]


class Bond:

    def __init__(self, bond_info):
        items = bond_info.split()
        self.BdAt1 = items[1]
        self.BdAt2 = items[2]
        self.BdType = items[3]

