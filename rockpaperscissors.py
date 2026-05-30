import random;
def rps ():
    random_number = random.randint(1, 3)
    print("Please enter your move")
    print("🪨 📄 ✂️")
    move = input()
    c = 0
    p = 0
    if random_number == 1:
        print("vs.")
        print("🪨")
    elif random_number == 2:
        print("vs.")
        print("📄")
    else:
        print("vs.")
        print("✂️")

    if move == "🪨":
        if random_number == 1:
            print("It's a tie!")
        elif random_number == 2:
            print("Computer Wins!")
            c += 1
        else:
            print("You win!")
            p += 1
    elif move == "📄":
        if random_number == 2:
            print("It's a tie!")
        elif random_number == 3:
            print("Computer Wins!")
            c += 1
        else:
            print("You win!")
            p += 1
    elif move == "✂️":
        if random_number == 3:
            print("It's a tie!")
        elif random_number == 1:
            print("Computer Wins!")
            c += 1
        else:
            print("You win!")
            p += 1
    else:
        print("Wait...That's not a move")
        c, p = rps()

    return c, p


def game ():
    print("How many rounds would you like to play?")
    num_rounds = int(input())
    player_score = 0
    comp_score = 0
    while num_rounds > 0:
        print("Number of rounds left: " + str(num_rounds))
        print("Current Score " + str(player_score) + " - " + str(comp_score))
        comp_add, p_add = rps()
        player_score += p_add
        comp_score += comp_add
        num_rounds -= 1

    print("Final Score " + str(player_score) + " - " + str(comp_score))
    if player_score > comp_score:
        print("You won! 🎉")
    elif comp_score > player_score:
        print("Yay I won!")
    else:
        print("Oh we tied. Good job!")

    print("Would you like to play again? Y/N")
    resp = input()
    if resp == "Y" or resp == "y":
        print("Yay!")
        game()
    elif resp == "N" or resp == "n":
        print("Oh okay :(")
        print("that's so sad")
        print("goodbye I guess")
        input()
    else:
        print("what")
        print("I guess that's a no...")
        input()


def rock_paper_scissors ():
    print("***********************************************")
    print("**************ROCK PAPER SCISSORS**************")
    print("Would you like to play rock paper scissors? Y/N")
    resp = input()
    if resp == "Y" or resp == "y":
        game()
    elif resp == "N" or resp == "n":
        print("Then why did you open this?")
        input()
        print("umm okay...")
        input()
    else:
        print("what")
        print("I guess that's a no...")
        input()
