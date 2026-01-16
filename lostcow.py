import sys

sys.stdin = open("lostcow.in", "r")
sys.stdout = open("lostcow.out", "w")


farmerpos, cowpos = [int(x) for x in input().split()]

if cowpos < farmerpos:
    cowLessThanFarmer = True
else:
    cowLessThanFarmer = False

totalDistMoved = 0

pow_of_two = 1
direction = 1
last_move = 0

while(True):
    farmerpos += (direction * pow_of_two) + (last_move * direction)
    totalDistMoved += abs(direction * pow_of_two) + abs(last_move * direction)

    last_move = abs(direction * pow_of_two)

    direction *= -1
    pow_of_two *= 2

    if (cowLessThanFarmer):
        if farmerpos <= cowpos:
            totalDistMoved -= abs(farmerpos - cowpos)
            break
    else:
        if farmerpos >= cowpos:
            totalDistMoved -= abs(farmerpos - cowpos)
            break

print(totalDistMoved)