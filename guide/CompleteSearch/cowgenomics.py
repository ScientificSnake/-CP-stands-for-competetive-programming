import sys

sys.stdin = open("cownomics.in", 'r')
sys.stdout = open("cownomics.out", "w")

Ncows, Mgenes = [int(x) for x in input().split()]

spottedCows = []
plaincows = []

for _ in range(Ncows):
    spottedCows.append(input())

for _ in range(Ncows):
    plaincows.append(input())

possiblegenes = 0
for geneColumn in range(Mgenes):
    spotCowsGenes = set()
    plainCowsGenes = set()
    for cow in range(Ncows):
        spotCowsGenes.add(spottedCows[cow][geneColumn])
        plainCowsGenes.add(plaincows[cow][geneColumn])
    if set.isdisjoint(spotCowsGenes, plainCowsGenes):
        possiblegenes += 1
print(possiblegenes)