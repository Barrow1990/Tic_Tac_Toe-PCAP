#! /usr/bin/python3
from random import choice

icons = {
    "blank": ["      ", "      ", "      ", "      ", "      "],
    "o": [" **** ", "*    *", "*    *", "*    *", " **** "],
    "x":   ["*    *", " *  * ", "  **  ", " *  * ", "*    *"]}

board = {}
for x in range(9):
    board.update({x: icons.get('blank')})


def printBoardBasic(board):
    for key, value in board.items():
        print(key, value)


def printBoardLong(board):
    for key, value in board.items():
        for num, row in enumerate(value):
            print(num, row)
        print()


def printPrep(board):
    row = [["" for x in range(3)] for x in range(17)]
    for key, value in board.items():
        for num, rows in enumerate(value):
            if key < 3:
                row[num][key] = rows
            elif key < 6:
                row[num + 6][key - 3] = rows
            elif key < 9:
                row[num + 12][key - 6] = rows

    for row_num, row_item in enumerate(row):
        if row_num in [5, 11]:
            for x in range(3):
                row[row_num][x] = '------'

    printBoard(row)


def printBoard(row):
    for row_num, row_item in enumerate(row):
        if row_num in [5, 11]:
            print('-|-'.join(row_item))
        else:
            print(' | '.join(row_item))


