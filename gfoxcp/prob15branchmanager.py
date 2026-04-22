from sys import stdin
from math import isfinite

inputdata = stdin.read().splitlines()

initer = iter(inputdata) 
ttests = int(next(initer))

class nodes():
    def __init__(self) -> None:
        self.cons = []
        self.pcon1 = float('inf')
        self.pcon2 = float('inf')

    
    def addcon(self, to:int):
        self.cons.append(to)
        if to < self.pcon1:
            # push down
            self.pcon2 = self.pcon1
            self.pcon1 = to
        else:
            if to < self.pcon2:
                self.pcon2 = to


for _ in range(ttests):
    ncities, mpeople = [int(x) for x in next(initer).split()]
    citylist = [nodes() for _ in range(ncities)]

    for _ in range(ncities-1):
        a, b = [int(x) for x in next(initer).split()]
        citylist[a-1].addcon(b-1)

    alrpathed = [False] * (ncities)
    validfor = [set() for _ in range(ncities)]
    for i in range(ncities):
        if alrpathed[i]:
            continue
        running = []

        targetnode = i

        while True:
            alrpathed[targetnode] = True
            running.append(targetnode)
            for prev in running:
                validfor[prev].add(targetnode)
            
            if isfinite(citylist[targetnode].pcon1):
                targetnode = int(citylist[targetnode].pcon1)
            else:
                break

    mainroute = validfor[0]
    people = []
    for _  in range(mpeople):
        people.append(int(next(initer)))
    
    count = 0
    for person in people:
        if person in validfor[0]:
            count += 1
    
    for index, node in enumerate(mainroute):
        garset = 

    

    
