import sys

def unshuffle(after, shuffle2):
    ogcows = [0] * n

    for index, intstruction in enumerate(shuffle2):
        ogcows[index] = after[intstruction-1]
    after = ogcows

sys.stdin = open("shuffle.in", 'r')
sys.stdout = open("shuffle.out", 'w')

n = int(input())

shuffle = [int(x) for x in input().split()]
aftercows = [int(y) for y in input().split()]

for i in range(3):
    unshuffle(aftercows, shuffle)

for i in aftercows:
    print(i)