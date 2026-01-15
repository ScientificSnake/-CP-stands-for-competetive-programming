import sys

sys.stdin = open("shell.in", "r")
sys.stdout = open("shell.out", "w")

scores = {1: 0, 2: 0, 3:0}
t = int(input())

poss = {1 : 1, 2:2, 3:3}
for _ in range(t):
    a, b, g = [int(x) for x in input().split()]

    for i in range(3):
        if a == poss[i+1]:
            poss[i+1] = b
        elif b == poss[i+1]:
            poss[i+1] = a
        if poss[i+1]== g:
            scores[i+1] += 1
print(max(scores.values()))