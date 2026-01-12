t = int(input())

for _ in range(t):
    cpp = input()
    bf, gf = input().split()

    bfl = list(bf)
    gfl = list(gf)

    gfl.sort()
    bfl.sort()

    if gfl == bfl:
        print("yes")
    else:
        print('no')