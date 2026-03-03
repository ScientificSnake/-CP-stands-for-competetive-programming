Nsize, Kpieces = [int(x) for x in input().split()]

def readNextPiece() -> list:
    piece = []
    for _ in range(Nsize):
        for char in input():
            if char == "#":
                piece.append(True)
            else:
                piece.append(False)
    return piece

bull = readNextPiece()
ups = []
workingShifts = []
sides = []
for i in range(1,Kpieces+1): # start at 1
    mainPiece = readNextPiece()
    workingShifts.clear()
    ups.clear()
    ups.append(workingShifts)
    #up 
    upindex = 0
    piece = mainPiece
    while True:
        cant = False
        for i in Nsize:
            if piece[i]:
                cant = True
                break
        if cant:
            break
        piece = piece[4:]
        piece.extend([False] * 4)
        ups.append(piece)
    # down
    piece = mainPiece
    while True:
        cant = False
        for i in Nsize:
            if piece[-i]:
                cant = True
                break
        if cant:
            break
        piece = piece[:4]
        [piece.insert(0, False) for _ in range(Nsize)]
        ups.append(piece)
    workingShifts.extend(ups)
    sides.clear()
    for spiece in ups:
        piece = spiece
        piece : list
        # shift right
        while True:
            cant = False
            for i in Nsize:
                if piece[(Nsize * i) - 1]:
                    cant = True
                    break
            if cant:
                break
            for line in range(Nsize):
                piece.pop((Nsize * (line+1)) -1)
                piece.insert(Nsize * line)

    
        


