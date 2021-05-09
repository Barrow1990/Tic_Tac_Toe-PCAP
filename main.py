#! /usr/bin/python3
from modules.boardPrint import printPrep as printBoard, boardSetup
from modules.player import *
from modules.game import *

icons, board = boardSetup()


def main(player1, player2):
    while True:
        for player in [player1, player2]:
            printBoard(board)
            if player.name[0:8] == 'Computer':
                computer(player, board, icons)
            else:
                playermove(player, board, icons)
            winner = isWinner(player, board, icons)
            if winner:
                printBoard(board)
                break
            if len(availableMoves(board, icons)) == 0:
                printBoard(board)
                print('Tie Game!!')
                winner = True
                break
        if winner:
            if playAgain():
                if samePlayers():
                    main(player1, player2)
                else:
                    setupGame()
            break

player1, player2 = setupGame()
main(player1, player2)