import sys

sys.stdin = open("bcs.in", "r")
sys.stdout = open("bcs.out", "w")


Nsize, Kpieces = [int(x) for x in input().split()]

def readNextPiece() -> list:
    piece = []
    for _ in range(Nsize):
        s = input()
        for char in s:
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
        if any(piece[:Nsize]):
            break
        piece = piece[Nsize:]
        piece.extend([False] * Nsize)
        ups.append(piece.copy())
    # down
    piece = mainPiece
    while True:
        if any(piece[-Nsize:]):
            break
        piece = piece[:-Nsize]
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
    allpiecesList[piecenum] = tuple(set(tuple(i) for i in workingShifts))

round1candidates = {key : set(val) for key, val in allpiecesList.items()}

# check each possible transformed piece and see if it could be part of the bull

def couldBeBull(piece: list):
    for index, tile in enumerate(piece):
        if tile:
            if not bull[index]:
                return False
    return True

round2candidates = {}
for key in round1candidates.keys():
    round2candidates[key] = []
    for candidate in round1candidates[key]:
        if couldBeBull(candidate):
            round2candidates[key].append(candidate)

def sumToBull(p1: list, p2 : list):
    together = []
    for index, (p1char, p2char) in enumerate(zip(p1, p2)):
        if p1char and p2char:
            return False
        
        if p1char or p2char:
            together.append(True)
        else:
            together.append(False)
    return (together == bull)

final_candidates = []

for key in round2candidates:
    for item in round2candidates[key]:
        final_candidates.append((key, item))
done = False
for i in range(len(final_candidates)):
    if done:
        break
    for j in range(i, len(final_candidates)):
        p1origin, p1val = final_candidates[i]
        p2origin, p2val = final_candidates[j]

        if p1origin == p2origin:
            continue

        if sumToBull(p1val, p2val):
            print(f"{p1origin} {p2origin}")
            done = True
            break
