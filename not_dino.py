def game():
    BLATANT_DINO_KNOCKOFF

def dino():
    print("***********************************************")
    print("***************NOT THE DINO GAME***************")
    print("Do you want to play the dino game? Y/N")
    resp = input()
    if resp == "N" or resp == "n":
        print("Good this is nothing like it.")
        input()
        game()
    elif resp == "Y" or resp == "y":
        print("This might be a bit disappointing then.")
        input()
    else:
        print("what")
        print("I guess that's a no...")
        input()