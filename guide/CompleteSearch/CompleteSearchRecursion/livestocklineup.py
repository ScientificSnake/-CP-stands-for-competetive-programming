# 8 Factorial recursion, all 40320
# Prune out branches that have a cow B that needs to be next to A in XBX

import sys
sys.stdin = open("lineup.in", 'r')
sys.stdout = open("lineup.out", "w")

Nconstraints = int(input())
constraints = {}
ccows = set()

for _ in range(Nconstraints):
    string = input().split()
    cow1, cow2 = string[0], string[-1]

    try:
        constraints[cow1].append(cow2)
    except:
        constraints[cow1] = [cow2]
    try:
        constraints[cow2].append(cow1)
    except:
        constraints[cow2] = [cow1]

    ccows.add(cow1)
    ccows.add(cow2)

cows = ["Bessie", "Buttercup", "Belinda", "Beatrice", "Bella", "Blue", "Betsy", "Sue"]
cows.sort()

solutions = []

def recurse_permutations(i : int, cur: list, left: list):
    # checks here
    if i == 8:
        solutions.append(cur)
        return
    for c in range(len(left)):
        newcur = cur.copy()
        newcur.append(left[c])
        newleft = left.copy()
        newleft.pop(c)
        recurse_permutations(i+1, newcur, newleft)

def getadjs(cow:str, solu:list) -> tuple:
    cowind = solu.index(cow)
    if cowind == 0:
        return (solu[1])
    elif cowind == 7:
        return (solu[6])
    else:
        return (solu[cowind-1], solu[cowind+1])

recurse_permutations(0, [], cows.copy())

for solution in solutions:
    fail = False
    for cow, adjs in constraints.items():
        if fail:
            break
        for adj in adjs:
            if adj not in getadjs(cow, solution):
                fail = True
                break
    if fail:
        continue
    string = "\n".join(solution)
    print(string)
    break


