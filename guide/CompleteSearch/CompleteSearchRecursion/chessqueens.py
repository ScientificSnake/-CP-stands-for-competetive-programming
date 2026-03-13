# read the chess board
reservedCount = 0
Oboard = {}
for line_num in range(8):
    line = input()
    for index, char in enumerate(line):
        if char == '*':
            reservedCount += 1
            Oboard[(index, line_num)] = '*'
        else:
            Oboard[(index, line_num)] = '.'

solutions = set()

def boardNotValid(board: dict, addedQueen):
    for key, val in board:
        if val != 'q':
            continue
        if key == addedQueen:
            continue
        x1, y1 = addedQueen
        x2, y2 = key

        xdif = abs(x1 - x2)
        ydif = abs(y1 - y2)

        if ydif == 0 or xdif == 0:
            return False
        if ydif == xdif:
            return False
    return True

def addQueens(i : int, board: dict, added : tuple = None):
    # check if board valid
    if i != 0:
        if boardNotValid(board, added):
            return # kill it
    if i == 8:
        # log queen positions
        queenPosTup = tuple(sorted([key for key in board if board[key] == 'q']))
        solutions.add(queenPosTup)
        return
    
    xcoord = i
    for ycoord in range(8):
        if board[(xcoord, ycoord)] in ['*', 'q']:
            continue
        newboard = board.copy()
        newboard[(xcoord, ycoord)] = 'q'
        addQueens(i+1, newboard, added=(xcoord, ycoord))
addQueens(i=0, board= Oboard)
print(len(solutions))


