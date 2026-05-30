import random
from rockpaperscissors import *
from tictactoe import *
def start ():
    print("What game would you like to play?")
    print(" 1) ROCK PAPER SCISSORS \n 2) TIC TAC TOE \n 3) RANDOM")
    resp = input()
    if resp == 1:
        rock_paper_scissors()
    if resp == 2:
        tic_tac_toe()
    if resp == 3:
        resp = random(1,2)
        if resp == 1:
            rock_paper_scissors()
        if resp == 2:
            tic_tac_toe()


print("********************************************************************************")
print("********************************************************************************")
print("****************************COMMAND LINE GAMES**********************************")
start()


