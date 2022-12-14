# 10/03/2022 10:28PM
# Single Atom Query Selector

from mol2parser import *
from auxclass import Query
import csv


def parsequery(query_file):
    with open(query_file,'r') as f:
        query_lines = f.readlines()
    return Query(query_lines)


def Selector(mol2mol,query):

    atoms = mol2mol.atoms
    sel1 = []
    for atom in atoms:
        if atom.AtType == query.atype:
            sel1.append(atom)
    sel2 = []

    for atom in sel1:
        abtypelist = []
        for bond in mol2mol.molgraph.returnbonds(atom):
            abtypelist.append((mol2mol.atomdic[bond[0]].AtType,bond[1]))
        flag = 1
        for conn in query.bonded:
            if conn not in abtypelist:
                flag = flag*0
            else:
                abtypelist.remove(conn)
        if flag==1:
            sel2.append(atom)

    return sel2


def main(qfile,mol2file,ofile):
    myquery = parsequery(qfile)
    with open(ofile, 'w', newline='') as csvfile:
        csvwriter = csv.writer(csvfile, delimiter=',')
        for pose in splitmol2(mol2file):
            sel_atom = Selector(pose,myquery)
            for atom in sel_atom:
                csvwriter.writerow(atom.AtCoord) # writes plain atomic coords


if __name__ == '__main__':
    main('example/query-aldehyde.txt','example/dock-aldehyde.mol2','example/output-aldehyde.csv')
