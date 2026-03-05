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
allpiecesList = {}
workingShifts = []
sides = []
for piecenum in range(1,Kpieces+1): # start at 1
    mainPiece = readNextPiece()
    workingShifts.clear()
    ups.clear()
    ups.append(mainPiece)
    #up 
    upindex = 0
    piece = mainPiece
    while True:
        if any(piece[:4]):
            break
        piece = piece[4:]
        piece.extend([False] * 4)
        ups.append(piece.copy())
    # down
    piece = mainPiece
    while True:
        if any(piece[-4:]):
            break
        piece = piece[:-4]
        [piece.insert(0, False) for _ in range(Nsize)]
        ups.append(piece.copy())
    workingShifts.extend(ups)
    sides.clear()
    for spiece in ups:
        piece = spiece
        spiece : list
        # shift right
        while True:
            if any(piece[Nsize-1::Nsize]):
                break
            for line in range(Nsize):
                piece.pop((Nsize * (line+1)) -1)
                piece.insert(Nsize * line, False)  
            sides.append(piece.copy())
        piece = spiece
        while True:
            if any(piece[::Nsize]):
                break
            for line in range(Nsize):
                piece.pop(Nsize *line)
                piece.insert((Nsize * (line+1)) - 1, False)
            sides.append(piece.copy())
        workingShifts.extend(sides)
    allpiecesList[piecenum] = list(set(tuple(i) for i in workingShifts))

round1candidates = {key : set(allpiecesList[val]) for key, val in allpiecesList.items()}

# check each possible transformed piece and see if it could be part of the bull

def couldBeBull(piece: list):
    for index, tile in enumerate(piece):
        if tile:
            if not bull[index]:
                return False
    return True

round2candidates = [i for i in round1candidates if couldBeBull(i)]
pass


