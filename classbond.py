# 10/03/2022 7:51PM
# Class Bond from Tripos MOL2 files


class Bond:

    def __init__(self, bond_info):
        items = bond_info.split()
        self.BdAt1 = items[1]
        self.BdAt2 = items[2]
        self.BdType = items[3]