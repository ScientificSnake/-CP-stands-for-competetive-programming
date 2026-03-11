# read the chess board
reservedCount = 0
Oboard = {}
for line_num in enumerate(range(8)):
    line = input()
    for index, char in enumerate(line):
        if char == '*':
            reservedCount += 1
            board[(index, line)] = '*'

solutions = set()

def addQueen(i : int, board: dict):
    # check if board valid
    if boardNotValid(board):
        return # kill it
    
    if i == 8:
        # log queen positions
        queenPosTup = (key for key in board if board[key] == 'q')
        solutions.add(queenPosTup)

    possibleNexts = 0

            

