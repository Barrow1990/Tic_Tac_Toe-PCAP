from .boardPrint import boardSetup
from random import choice, sample

icons, board = boardSetup()


class player():
    __player = 1

    def __init__(self, name="Computer"):
        self.name = name
        self.token = self.token()
        player.__player += 1

    def token(self):
        if player.__player == 1:
            token = 'x'
        elif player.__player == 2:
            token = 'o'
        return token

def quantity_of_players():
    while True:
        quantity_of_players = input("How Many Players? (1 or 2) ")
        if quantity_of_players in ['0', '1', '2']:
            return int(quantity_of_players)

def setupPlayers(quantity_of_players):
    if quantity_of_players == 0:
        player1 = player('Computer1')
        player2 = player('Computer2')
    elif quantity_of_players == 1:
        player1 = player(input("Player 1 Name: "))
        player2 = player('Computer1')
    else:
        player1 = player(input("Player 1 Name: "))
        player2 = player(input("Player 2 Name: "))
    return player1, player2

def samePlayers():
    while True:
        answer = input("Do you want to Keep the Same Players? (yes/no) ").lower()
        if answer == 'yes':
            answer = True
            break
        elif answer == 'no':
            answer = False
            break
    return answer