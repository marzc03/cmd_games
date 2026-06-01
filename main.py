import random
import time
from rockpaperscissors import rock_paper_scissors
from tictactoe import tic_tac_toe
from starfall import starfall
from story import story
from not_dino import dino
def start ():
    print("What game would you like to play?")
    print(" 1) ROCK PAPER SCISSORS \n 2) TIC TAC TOE \n 3) STARFALL (PREVIEW ONLY) \n 4) SOME STORY GAME (PREVIEW ONLY) \n 5) NOT THE DINO GAME (PREVIEW ONLY) \n 6) RANDOM")
    resp = int(input())
    if resp == 1:
        rock_paper_scissors()
    elif resp == 2:
        tic_tac_toe()
    elif resp == 3:
        starfall()
    elif resp == 4:
        story()
    elif resp == 5:
        dino()
    else:
        print("Oh so random.")
        print("Risky")
        print("Well...")
        print("3")
        time.sleep(1)
        print("2")
        time.sleep(1)
        print("1")
        time.sleep(1)
        resp = random.randint(1,5)
        if resp == 1:
            rock_paper_scissors()
        if resp == 2:
            tic_tac_toe()
        if resp == 3:
            starfall()
        if resp == 4:
            story()
        if resp == 5:
            dino()
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


