import sys

sys.stdin = open('cbarn.in', 'r')
sys.stdout = open("cbarn.out", 'w')

def movement_sum(rooms: list) -> int:
    sum = 0
    for i, cows in enumerate(rooms):
        sum += i*cows
    return sum

rooms = []

n = int(input())

for _ in range(n):
    rooms.append(int(input()))

def cycleList(l: list):
    temp = l.pop(len(l)-1)
    l.insert(0, temp)

possibles = []

for _ in range(n):
    possibles.append(movement_sum(rooms))
    cycleList(rooms)
print(min(possibles))

