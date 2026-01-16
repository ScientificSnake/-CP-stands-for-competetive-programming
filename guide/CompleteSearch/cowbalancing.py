"""

idea -> only iterate through relavent fence x and ys -> any cow +- 1

then check

"""

import sys

sys.stdin = open("balancing.in", "r")
sys.stdout = open("balancing.out", "w")

Ncows, Bbounds = [int(x) for x in input().split()]

relevantFenceXs = set()
relevantFenceYs = set()

cows = []


for cow in range(Ncows):
    x, y = [int(x) for x in input().split()]
    cows.append((x,y))

    relevantFenceXs.add(x-1)
    relevantFenceXs.add(x+1)
    relevantFenceYs.add(y-1)
    relevantFenceYs.add(y+1)

def checkBalance(fencex, fencey) -> int:
    bLeft = 0
    bRight = 0
    tLeft = 0
    tRight = 0

    for cowx, cowy in cows:
        if cowx < fencex: # LEFT
            if cowy < fencey: # bottoms
                bLeft += 1
            else:
                tLeft += 1
        else:
            if cowy < fencey:
                bRight += 1
            else:
                tRight += 1
    return max([tRight, tLeft, bRight, bLeft])


bestSol = int(Ncows) # startin assumption garunteed it will be better than this

for x in relevantFenceXs:
    for y in relevantFenceYs:
        maxLoad = checkBalance(x,y)
        if maxLoad < bestSol:
            bestSol = maxLoad

print(bestSol)
        
    
