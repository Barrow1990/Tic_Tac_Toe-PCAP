#! /usr/bin/python3

icons = {
    "blank": ["      ", "      ", "      ", "      ", "      "],
    "o": [" **** ", "*    *", "*    *", "*    *", " **** "],
    "x":   ["*    *", " *  * ", "  **  ", " *  * ", "*    *"]}

board = {}
for x in range(0, 10):
    if x == 0:
        continue
    elif x % 2 == 0:
        board.update({x: icons.get("x")})
    else:
        board.update({x: icons.get("o")})

def printBoardBasic(board):
    for key, value in board.items():
        print(key, value)

def printBoardLong(board):
    for key, value in board.items():
        for num, row in enumerate(value):
            print(num, row)
        print()

def printBoard(board):
    row = [["" for x in range(3)] for x in range(13)]
    for key, value in board.items():
        for num, rows in enumerate(value):
            for x in range(4):
                
            row[num][0], row[num][1], row[num][2], row[num][3] = rows[0]
            # print(num, rows)
            continue
    print("\nRows:")
    for x, r in enumerate(row):
        print(x, r)


printBoard(board)
print("\nBoard:")
for key, value in board.items():
    print(key, value)
