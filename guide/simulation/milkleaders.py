import sys

sys.stdin = open("measurement.in", 'r')
sys.stdout = open('measurement.out', 'w')


entryDict = {}
days = []

Nentries = int(input())

for _ in range(Nentries):
    day, cowName, change = input().split()
    day = int(day)
    change = int(change)

    entryDict[day] = [cowName, change]
    days.append(day)

days.sort()
curLeaders = ['Elsie', 'Mildred', 'Bessie']

cows = {
    'Elsie' : 7,
    'Mildred' : 7,
    'Bessie' : 7
}

def updateLeaders(curleaders, displayChanges):
    newLeaders = []

    newLead = max(cows.values())
    for cow, val in cows.items():
        if val == newLead:
            newLeaders.append(cow)
    if newLeaders == curleaders:
        return newLeaders, displayChanges
    else:
        return newLeaders, displayChanges + 1
displayChangesG = 0

for day in days:
    cowName, change = entryDict[day]
    cows[cowName] += change
    curLeaders, displayChangesG = updateLeaders(curLeaders, displayChangesG)

print(displayChangesG)
