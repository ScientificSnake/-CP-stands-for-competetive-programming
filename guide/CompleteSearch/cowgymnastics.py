from itertools import combinations as combos

import sys

sys.stdin = open('gymnastics.in', "r")
sys.stdout = open('gymnastics.out', "w")

kpractices, ncows = [int(x) for x in input().split()]

valid = set(combos(range(1, ncows+1), 2))

# get initial states

increasers = set()

cows = list(range(1, ncows+ 1))

firstLine = [int(x) for x in input().split()]
for i, j in valid:
    if firstLine.index(i) < firstLine.index(j):
        increasers.add((i, j))
    # also add to valid
    # valid.add((firstLine[i], firstLine[j]))

# now check next lines
newvalid = set()
positions = {}
for _ in range(kpractices-1): # -1 because we already scane firstline
    # only check valid by reverse iterating and removing those which aren't
    line = [int(x) for x in input().split()]
    newvalid = set()
    for index, cow in enumerate(line):
        positions[cow] = index
    for cow1, cow2 in valid:
        if positions[cow1] < positions[cow2]:
            if (cow1, cow2) in increasers:
                newvalid.add((cow1, cow2))
        else:
            if (cow1, cow2) not in increasers:
                newvalid.add((cow1, cow2))
    valid = newvalid
print(len(valid))


