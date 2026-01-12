t = int(input())

for _ in range(t):
    a, b, n = [int(n) for n in input().split(' ')]

    moves = 0

    if b >= a:
        moves = 1
    elif b * n <= a:
        moves = 1
    elif b * n > a and b < a:
        moves = 2

    print(moves)
