"""Usaco bronze normal dif from https://usaco.guide """

import sys

sys.stdin = open("traffic.in", 'r')
sys.stdout = open ("traffic.out", 'w')

nmiles = int(input())

miles = []

for _ in range(nmiles):
    s = input().split()
    miles.append([s[0], int(s[1]), int(s[2])])

cmin = 1
cmax = 2

inmin = 0
inmax = float("infinity")

for i in range(nmiles-1, -1, -1):
    if miles[i][0] == "off":
        inmin += miles[i][cmin]
        inmax += miles[i][cmax]
    elif miles[i][0] == "on":
        inmin -= miles[i][cmax]
        inmax -= miles[i][cmin]
        inmin = max(0, inmin)
    else:
        inmin = max(inmin, miles[i][cmin])
        inmax = min(inmax, miles[i][cmax])

outmin = 0
outmax = float("infinity")

for i in range(nmiles):
    if miles[i][0] == "on":
        outmin += miles[i][cmin]
        outmax += miles[i][cmax]
    elif miles[i][0] == "off":
        outmin -= miles[i][cmax]
        outmax -= miles[i][cmin]
        outmin = max(outmin, 0)
    else:
        outmin = max(outmin, miles[i][cmin])
        outmax = min(outmax, miles[i][cmax]) 

print(inmin, inmax)
print(outmin, outmax)

