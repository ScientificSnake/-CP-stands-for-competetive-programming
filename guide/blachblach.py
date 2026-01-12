import sys

sys.stdin = open("buckets.in", "r")
sys.stdout = open("buckets.out", "w")

listofrows = []

for i in range(10):
    s = input()
    s.rstrip()
    listofrows.append(s)

for yval, row in enumerate(listofrows):
    for xval, char in enumerate(row):
        if char == "B":
            barnx = xval
            barny = yval
        elif char == "R":
            rockx = xval
            rocky = yval
        elif char == "L":
            lakex = xval
            lakey = yval

xdist = abs(barnx - lakex)
ydist = abs(barny - lakey)

totaldist = xdist + ydist - 1

if (xdist == 0) and (rockx == barnx):
    highbound = max(lakey, barny)
    lowbound = min(lakey, barny)
    if (rocky < highbound) and (rocky > lowbound):
        print(totaldist + 2)
    else:
        print(totaldist)
elif ydist == 0 and (rocky == barny):
    highbound = max(lakex, barnx)
    lowbound = min(lakex, barnx)
    if (rockx < highbound) and (rockx > lowbound):
        print(totaldist + 2)
    else:
        print(totaldist)
else:
    print(totaldist)