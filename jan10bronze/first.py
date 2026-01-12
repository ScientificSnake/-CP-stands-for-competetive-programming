import math
t = int(input())

for _ in range(t):

    startingAChips, startingBChips, Ca, Cb, Fa = [int(x) for x in input().split()]

    # start by exchaning chips you already can

    exchanges = startingBChips // Cb

    startingBChips -= exchanges * Cb
    startingAChips += exchanges * Ca

    neededAChips = Fa - startingAChips

    if neededAChips <= 0:
        print(0) # case where you already have enough chips
        continue

    bsets = math.ceil(neededAChips/Ca)

    maxBs = (bsets * Cb) - 1 - startingBChips

    maxAs = (neededAChips - (bsets - 1) * Ca) - 1

    if (Ca > Cb):
        if (maxBs < maxAs):
            extraBs = Cb - startingBChips -1
            extraBs = max(0, extraBs)
            ret = neededAChips - ((startingBChips // Cb) * Ca) + extraBs
            print(ret)
            continue

    if (maxBs < 0):
        print(0) # can instatnly trade in
        continue
    if (maxAs < 0 and maxBs <= 0):
        print(0)
        continue

    final = maxBs + maxAs + 1
    print(final)