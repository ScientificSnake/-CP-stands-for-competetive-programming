import sys

sys.stdin = open("cowsignal.in", "r")
sys.stdout = open("cowsignal.out", "w")

m, n, k = [int(x) for x in input().split()]

lines = []

for _ in range(m):
    s = input()
    s.rstrip()
    lines.append(s)


for i in range(m):
    line = ''
    for char in lines[i]:
        line += char * k
    for j in range(k):
        print(line)