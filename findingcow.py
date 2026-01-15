# Source: https://usaco.guide/general/io

import sys

# sys.stdin = open("lostcow.in", "r")
# sys.stdout = open("lostcow.out", "w")

x, y = [int(x) for x in input().split()]

curlocation = x

movement = 1
sign = 1

total_moved = 0

vtocow = y -x
if vtocow < 0:
    dtocow = -1
else:
    dtocow = 1

while True:
    curlocation += sign * movement
    total_moved += movement

    curvtocow = y-curlocation

    if (curvtocow < 0):
        sign2 = -1
    else:
        sign2 = 1

    if sign2 != dtocow:
        overshoot = abs(curlocation - y)
        break

    movement *= 2*movement
    sign *= -1
print(total_moved - overshoot)
        
