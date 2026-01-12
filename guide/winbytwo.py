gamestr = input()

winner = None
targetindex = 0

apoints = 0
bpoints = 0

while winner is None:
    player = gamestr[targetindex]
    points = int(gamestr[targetindex + 1])

    if player == 'A':
        apoints += points
    else:
        bpoints += points

    if apoints >= 11 and (apoints - bpoints) >= 2:
        winner = 'A'
    elif bpoints >= 11 and (bpoints - apoints) >= 2:
        winner = 'B'
    
    targetindex += 2

print(winner)