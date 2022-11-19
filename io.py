# 11/18/2022 7:37PM
# Read-and-Write (User Interface)

from saqs import parsequery, Selector
from mol2parser import *
import getopt, sys, csv
import numpy as np


def main():

    help_msg = "Usage: python3 io.py -q query.txt -m dock.mol2 -o output.csv\n\
            Options: -s/--scores Write scores\n\
            Options: -a/--all Write all properties"
    try:
        opts, args = getopt.getopt(sys.argv[1:], "hq:m:o:sa", ["help", "query=", "mol2file=", "output=", "scores", "all"])
        if len(opts)==0:
            print(help_msg)
            sys.exit()
    except getopt.GetoptError as err:
        # print help information and exit:
        print(help_msg)
        print(err)  # will print something like "option -a not recognized"
        sys.exit(2)

    qfile = "query.txt"
    mol2file = "dock.mol2"
    ofile = "output.csv"
    write_scores = False
    write_all = False

    for o, a in opts:
        if o in ("-h", "--help"):
            print(help_msg)
            sys.exit()
        elif o in ("-q", "--query"):
            qfile = a
        elif o in ("-m", "--mol2file"):
            mol2file = a
        elif o in ("-o", "--output"):
            ofile = a
        elif o in ("-s", "--scores"):
            write_scores = True
        elif o in ("-a", "--all"):
            write_all = True
        else:
            assert False, "unhandled option"

    myquery = parsequery(qfile)

    with open(ofile, 'w', newline='') as csvfile:
        csvwriter = csv.writer(csvfile, delimiter=',')
        pose_list = splitmol2(mol2file)

        if len(pose_list) == 0:
            print("Could not parse input mol2. Is it empty?")
            sys.exit()

        if write_all:
            header = list(pose_list[0].propertydic.keys())
            header.extend(["x", "y", "z"])
        else:
            if write_scores:
                header = ["S", "x", "y", "z"]
            else:
                header = ["x", "y", "z"]
        csvwriter.writerow(header)

        for pose in pose_list:
            pose_propvals = []
            for val in pose.propertydic.values():
                if np.isnan(np.nan):
                    pose_propvals.extend([''])
                else:
                    pose_propvals.extend([val])
            pose_score = [pose.propertydic["S"]]
            sel_atom = Selector(pose, myquery)

            if len(sel_atom) == 0:
                sele_coord = [np.array([np.nan, np.nan, np.nan])]
            else:
                sele_coord = []
                for atom in sel_atom:
                    sele_coord.append([x for x in atom.AtCoord])

            for coordarray in sele_coord:
                if write_all:
                    row = pose_propvals
                    row.extend(coordarray)
                else:
                    if write_scores:
                        row = pose_score
                        row.extend(coordarray)
                    else:
                        row = coordarray
                csvwriter.writerow(row)


if __name__ == "__main__":
    main()
