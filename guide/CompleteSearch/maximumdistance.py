import itertools

n = int(input())

xcoords = [int(x) for x in input().split()]
ycoords = [int(x) for x in input().split()]

maxsquared = 0
e = itertools.combinations(range(n), 2)
for i1, i2 in e:
    xdist = abs(xcoords[i1] - xcoords[i2])
    ydist = abs(ycoords[i1] - ycoords[i2])
    # a^2 + b^2 = c^2

    maxsquared = max(pow(xdist,2) + pow(ydist, 2), maxsquared)
print(maxsquared)