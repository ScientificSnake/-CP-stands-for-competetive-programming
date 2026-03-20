import sys

string = input()

openStrands = set()


crossedPairs = 0

for char in string:
    if char not in openStrands:
        openStrands.add(char)
    else:
        openStrands.remove(char)
        crossedPairs += len(openStrands)
print(crossedPairs)