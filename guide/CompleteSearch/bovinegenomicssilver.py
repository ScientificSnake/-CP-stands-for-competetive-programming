from itertools import combinations as combo

Ncows, Mgenes = [int(x) for x in input().split()]

spottyCows = [input() for x in range(Ncows)]
plainCows = [input() for x in range(Ncows)]
result = 0
for gene1, gene2, gene3 in combo(range(Mgenes), 3):
    spottyCowGenes = {([cow][gene1], [cow][gene2], [cow][gene3]) for cow in spottyCows}
    plainCowGenes = {([cow][gene1], [cow][gene2], [cow][gene3]) for cow in plainCows}
    if spottyCowGenes.isdisjoint(plainCowGenes):
        result += 1
print(result)