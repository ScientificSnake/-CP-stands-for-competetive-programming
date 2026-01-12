t = int(input())

for _ in range(t):
    maxMoves, dx, dy = [int(i) for i in input().split()]

    dx = abs(dx)
    dy = abs(dy)

    moveList = input()

    diags = 0

    # how many 8s
    for char in moveList:
        if char == '8':
            diags += 1

    if dx > diags:
        dx -= diags
    else:
        dx = 0
    if dy > diags:
        dy -= diags
    else:
        dy = 0

    if not (dx == 0 and dy == 0):
        if (dx + dy) <= (maxMoves - diags):
            print('yes')
        else:
            print('no')
    else:
        print("yes")

