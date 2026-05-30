import random
import time
from rockpaperscissors import rock_paper_scissors
from tictactoe import tic_tac_toe
def start ():
    print("What game would you like to play?")
    print(" 1) ROCK PAPER SCISSORS \n 2) TIC TAC TOE \n 3) RANDOM")
    resp = int(input())
    if resp == 1:
        rock_paper_scissors()
    if resp == 2:
        tic_tac_toe()
    if resp == 3:
        print("Oh risky")
        print("Well...")
        print("3")
        time.sleep(1)
        print("2")
        time.sleep(1)
        print("1")
        time.sleep(1)
        resp = random.randint(1,2)
        if resp == 1:
            rock_paper_scissors()
        if resp == 2:
            tic_tac_toe()
    print("Play a different game? Y/N")
    resp = input()
    if resp == "Y" or resp == "y":
        print("Yes!")
        start()
    elif resp == "N" or resp == "n":
        print("Okay")
        time.sleep(5)
    else:
        print("what")
        print("I guess that's a no...")
        time.sleep(5)



print("********************************************************************************")
print("********************************************************************************")
print("****************************COMMAND LINE GAMES**********************************")
start()


