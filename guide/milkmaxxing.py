import sys

sys.stdin = open("mixmilk.in", "r")
sys.stdout = open("mixmilk.out", "w")


c1, m1 = [int(x) for x in input().split()]
c2, m2 = [int(x) for x in input().split()]
c3, m3 = [int(x) for x in input().split()]

milklevels = [m1, m2, m3]
capacities = [c1, c2, c3]

for i in range(100):
    z = i % 3

    milkto = (z + 1) % 3
    milkfrom = z

    space = capacities[milkto] - milklevels[milkto]
    milktomove = min(space, milklevels[milkfrom])

    milklevels[milkfrom] -= milktomove
    milklevels[milkto] += milktomove

# no repeating checks because its naive

print(milklevels[0])
print(milklevels[1])
print(milklevels[2])