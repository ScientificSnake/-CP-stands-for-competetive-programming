def main():
    sides = [int(x) for x in input().split()]
    x1, y1, x2, y2, x3, y3 = sides
    rects = (x1,y1), (x2, y2), (x3,y3)
    total_area = (x1*y1) + (x2*y2) + (x3*y3)

    s = pow(total_area, (0.5))
    s:float
    if not s.is_integer():
        print(-1)
        return
    s = int(s)
    
    if s not in sides:
        # cannot be flat stack or corner
        print(-1)
        return
    
    # Flat stack case
    if sides.count(s) == 3:
        remainingsides = sides.copy()
        [remainingsides.remove(s) for i in range(3)]

        if sum(remainingsides) == s:
            print(s)
            for side, letter in zip(remainingsides, ['A', 'B', 'C']):
                [print(letter * s) for i in range(side)]
            return
            
    # Corner case
    # look for the s in sides to be the big piece

    bigPiece = rects[(sides.index(s)//2)]
    if bigPiece[1] == s:
        bigPiece = (bigPiece[1], bigPiece[0])

    bcOptions = [0,1,2]
    BigPieceIndex = bcOptions.pop(sides.index(s)//2)

    for bFlip in [False, True]:  # you see i was too lazy to do 3 bit bit mask
        for cFlip in [False,True]:
            for BCFlip in [False,True]:
                ax, ay = bigPiece
                if BCFlip:
                    bx, by = rects[bcOptions[0]]
                    cx, cy = rects[bcOptions[1]]
                else:
                    bx, by = rects[bcOptions[1]]
                    cx, cy = rects[bcOptions[0]]
                
                if bFlip:
                    bx, by = by, bx
                if cFlip:
                    cx, cy = cy, cx

                # Now The checks

                if ay + by != s:
                    continue
                if cy != by:
                    continue
                if bx + cx != s:
                    continue

                # success just print it out
                print(s)
                bigLetter = ['A', 'B', 'C'][BigPieceIndex]
                if BCFlip:
                    bletter = ['A', 'B', 'C'][bcOptions[0]]
                    cletter = ['A', 'B', 'C'][bcOptions[1]]
                else:
                    bletter = ['A', 'B', 'C'][bcOptions[1]]
                    cletter = ['A', 'B', 'C'][bcOptions[0]]
                
                [print(bigLetter*s) for i in range(ay)]

                for i in range(by):
                    print((bletter*bx) + (cletter * cx))
                return
    print(-1)

main()
