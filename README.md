# SAQS: Single Atom Query Selector

This is the first project I created with PyCharm and shared on Github. 

I made this convenient function (Selector, in main.py) to find a single atom from a multi-structure Tripos MOL2 file generated from MOE Dock by specification of atom type and bond type. 

## Dependency

Python3, numpy. 


## Inputs

The Selector function requires two inputs:

1. A MOL2 file

Instead of using the SMILES/SMARTS description (which sometimes does not corrrespond to the permutation of ligand atoms in the output structure file), I made it read the topology information from the bond section of the MOL2 file and store as a graph. 

2. A query file

The Selector function currently takes simple query that includes atom type (of the target and bonded atoms) and bond type. 


## Expected outcome

The expected outcome is the coordinates of the hit atoms and will be saved to a CSV file. 

If multiple hits exist, all of them will be returned and each in new a row. 


## Usage of io.py

```
python3 io.py -q query.txt -m dock.mol2 -o output.csv
```

Options: -s Write scores; -a Write all properties

```
python3 io.py -q query.txt -m dock.mol2 -o output.csv -s
```


## Comments and possible improvements

I used to hard-code the chemical features when looking for atoms of interest in my own docking analysis. I was hoping other members in my lab could do the same without having to code it themselves. Thus, I made the Selector works for simple but general specification of atom type and bond type. 

There can be (and in many cases there need to be) more complicated queries, for example, to select one of the two amine groups on a benzene ring. To distinguish the two, we must either:

(1) establish a numbering rule that works consistently for all compounds in our library, or, 

(2) find where the difference occurs down the chain of bonded atoms. Some of the graph-based methods such as counting the shortest distance between two nodes might be useful.  
