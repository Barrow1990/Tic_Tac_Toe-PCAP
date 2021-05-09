#! /usr/bin/python3
from .player import quantity_of_players, setupPlayers
from random import choice

def setupGame():
    qop = quantity_of_players()
    player1, player2 = setupPlayers(qop)
    return player1, player2

def availableMoves(board, icons):
    available_moves = [key + 1 for key, value in board.items() if value == icons.get('blank')]
    return available_moves

def playermove(player, board, icons):
    move = validateMove(availableMoves(board, icons), player)
    board.update({move - 1: icons.get(player.token)})
    return move

def validateMove(available_moves, player):
    moves = [str(x) for x in range(1, 11)]
    while True:
        move = input(f"Please Choose A Num {player.name} '{player.token}': {available_moves}: ")
        if move in moves:
            if int(move) in available_moves:
                return int(move)

def isWinner(player, board, icons):
    nb = [value for value in board.values()]
    icon = icons.get(player.token)
    if ((nb[0] == icon and nb[1] == icon and nb[2] == icon) or
        (nb[3] == icon and nb[4] == icon and nb[5] == icon) or
        (nb[6] == icon and nb[7] == icon and nb[8] == icon) or
        
        (nb[0] == icon and nb[3] == icon and nb[6] == icon) or
        (nb[1] == icon and nb[4] == icon and nb[7] == icon) or
        (nb[2] == icon and nb[5] == icon and nb[8] == icon) or
        
        (nb[0] == icon and nb[5] == icon and nb[8] == icon) or
        (nb[2] == icon and nb[5] == icon and nb[6] == icon)):
        print(f"{player.name} is the Winner!!!")
        return True
    else:
        return False

def playAgain():
    while True:
        answer = input("Do you want to play again? (yes/no) ").lower()
        if answer == 'yes':
            answer = True
            break
        elif answer == 'no':
            answer = False
            break
    return answer

def computer(player, board, icons):
    am = availableMoves(board, icons)
    if 5 in am:
        move = 5
    elif 1 in am or 3 in am or 6 in am or 9 in am:
        move = choice(am)
    elif 2 in am or 4 in am or 6 in am or 8 in am:
        move = choice(am)
    else:
        return

    board.update({move - 1: icons.get(player.token)})