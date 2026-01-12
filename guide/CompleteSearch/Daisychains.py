from itertools import combinations_with_replacement as comborep
nflowers = int(input())

flowers = [int(x) for x in input().split()]

avgflowers = 0

for i, j in comborep(range(nflowers), 2):
    floweravg = sum(flowers[i:j+1])/(j - i + 1)
    for flower in flowers[i:j+1]:
        if flower == floweravg:
            avgflowers += 1
            break
print(avgflowers)