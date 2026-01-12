import sys

sys.stdin = open("speeding.in", "r")
sys.stdout = open("speeding.out", "w")

n, m = [int(x) for x in input().split()]

speedlimits = list()

curd = 0

for _ in range(n):
    dist, lim = [int(x) for x in input().split()]
    speedlimits.append([curd + dist, lim])
    curd += dist
infraction = 0

speedsegs = []

for _ in range(m):
    speedsegs.append([int(x) for x in input().split()])

i = 0
x, y = speedsegs[i]
i += 1
curdist = x
rollover = True
for distend, limit in speedlimits:
    if rollover:
        dist = x
        speed = y
        speeding = speed - limit
    if (infraction < speeding):
        infraction = speeding
    while (curdist < distend):
        dist, speed = speedsegs[i]
        i += 1
        speeding = speed - limit
        if (infraction < speeding):
            infraction = speeding
        curdist += dist
        x = dist
        y = speed
    if curdist > distend:
        speed = y
        dist = x
        rollover = True
    else:
        rollover = False


print(infraction)
