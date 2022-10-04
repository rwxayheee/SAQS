# 10/03/2022 9:43PM
# Class Query

# expected query
# ATOM C.2
# CONN H 1
# CONN C.3 1
# CONN O.2 2


class Query:

    def __init__(self, specs):
        self.atype = ''
        self.bonded = []
        for line in specs:
            if len(line.split()) > 0:
                items = line.split()
                if items[0] == 'ATOM':
                    self.atype = items[1]
                if items[0] == 'CONN':
                    self.bonded.append((items[1],items[2]))