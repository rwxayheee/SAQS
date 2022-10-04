# 10/03/2022 7:51PM
# Class Atom from Tripos MOL2 files

import numpy as np


class Atom:

    def __init__(self, atom_info):
        items = atom_info.split()
        self.AtInd = items[0]
        self.AtName = items[1]
        self.AtCoord = np.array([float(x) for x in items[2:5]])
        self.AtType = items[5]