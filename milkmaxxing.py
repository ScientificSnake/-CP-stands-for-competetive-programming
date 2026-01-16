import sys

sys.stdin = open("mixmilk.in", "r")
sys.stdout = open("mixmilk.out", "w")

c1, m1 = [int(x) for x in input().split()]
c2, m2 = [int(x) for x in input().split()]
c3, m3 = [int(x) for x in input().split()]

capacities = {c1, c2, c3}
milklevels = {m1, m2, m3}

for i in range(100):
    origin =  i % 3
    target = (i + 1) % 3

    to_move = min()
    
