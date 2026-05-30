import random
def print_board(board):
    print("\033[4m " + board[0] + " | "+  board[1] + " | " + board[2] + " \033[0m")
    print("\033[4m " + board[3] + " | "+  board[4] + " | " + board[5] + " \033[0m")
    print(" " + board[6] + " | "+  board[7] + " | " + board[8] + " ")

def win(board): #check this math bud
    i = 0
    while i < 9:
        if board[i] == board [i + 1] == board[i+2]:
            return board[i]
        i = i + 3
    i = 0
    while i < 3:
        if board[i] == board [i + 3] == board[i+6]:
            return board[i]
        i = i + 1
    if board[0] == board[4] ==board[8]:
        return board[0]
    elif board[2] == board[4] ==board[6]:
        return board[2]
    else:
        return False

def player_move(board):
    print("What space would you like to go in?")
    resp = int(input())
    if resp > 0 and resp < 10:
        if board[resp - 1] == "O":
            print("I already went there bud.")
            player_move(board)
        elif board[resp - 1] == "X":
            print("You already played that.")
            player_move(board)
        else:
            board[resp - 1] = "X"
    else:
        print("That's not even a move?")
        player_move(board)

def comp_move(board, move_number):
    move = -1
    m = random.randint(1,5)
    if move_number == 0: #FIRST MOVE ALWAYS IN CENTER X
        if m == 1 and board[0] != "X":
            return 0
        elif m == 2 and board[2] != "X":
            return 2
        elif m == 3 and board[4] != "X":
            return 4
        elif m == 4 and board[6] != "X":
            return 6
        elif m == 5 and board[8] != "X":
            return 8
        else:
            return comp_move(board, 0)
    else:
        if m == 1 and board[0] != "X" and board[0] != "O":
            move = 0
        elif m == 2 and board[2] != "X" and board[2] != "O":
            move = 2
        elif m == 3 and board[4] != "X" and board[4] != "O":
            move = 4
        elif m == 4 and board[6] != "X" and board[6] != "O":
            move =  6
        elif m == 5 and board[8] != "X" and board[8] != "O":
            move = 8
    
    #GOES TO CHECK TO BLOCK YOU
    #check horizontal
    i = 0
    while i < 9:
        if board[i] == board[i + 1] == "X" and (board[i + 2] != "O" and board[i + 2] != "X"):
            move = i + 2
        elif board[i] == board[i + 2] == "X" and (board[i + 1] != "O" and board[i + 1] != "X"):
            move = i + 1
        elif board[i+1] == board[i + 2] == "X" and (board[i] != "O" and board[i] != "X"):
            move = i
        i = i + 3
    i = 0
    #check vertical
    while i < 3:
        if board[i] == board[i + 3] == "X" and (board[i + 6] != "O" and board[i + 6] != "X"):
            move = i + 6
        elif board[i] == board[i + 6] == "X" and (board[i + 3] != "O" and board[i + 3] != "X"):
            move = i + 3
        elif board[i+6] == board[i + 3] == "X" and (board[i] != "O" and board[i] != "X"):
            move = i
        i = i + 1
    #check diagnal
    if (board[0] == "X" and board[4] == "X" ) and (board[8] != "O" and board[8] != "X"):
        move = 8
    elif (board[0] == "X" and board[8] == "X") and (board[4] != "O" and board[4] != "X"):
        move = 4
    elif (board[4] == "X" and board[8] == "X") and (board[0] != "O" and board[0] != "X"):
        move = 0
    elif (board[2] == "X" and board[4] == "X") and (board[6] != "O" and board[6] != "X"):
        move = 6
    elif (board[2] == "X" and board[6] == "X") and (board[4] != "O" and board[4] != "X"):
        move = 4
    elif (board[4] == "X" and board[6] == "X") and (board[2] != "O" and board[2] != "X"):
        move = 2

#GOES TO CHECK for win
    #check horizontal
    i = 0
    while i < 9:
        if board[i] == board[i + 1] == "O" and (board[i + 2] != "O" and board[i + 2] != "X"):
            move = i + 2
        elif board[i] == board[i + 2] == "O" and (board[i + 1] != "O" and board[i + 1] != "X"):
            move = i + 1
        elif board[i+1] == board[i + 2] == "O" and (board[i] != "O" and board[i] != "X"):
            move = i
        i = i + 3
    i = 0
    #check vertical
    while i < 3:
        if board[i] == board[i + 3] == "O" and (board[i + 6] != "O" and board[i + 6] != "X"):
            move = i + 6
        elif board[i] == board[i + 6] == "O" and (board[i + 3] != "O" and board[i + 3] != "X"):
            move = i + 3
        elif board[i+6] == board[i + 3] == "O" and (board[i] != "O" and board[i] != "X"):
            move = i
        i = i + 1
    #check diagnal
    if (board[0] == "O" and board[4] == "O" ) and (board[8] != "O" and board[8] != "X"):
        move = 8
    elif (board[0] == "O" and board[8] == "O") and (board[4] != "O" and board[4] != "X"):
        move = 4
    elif (board[4] == "O" and board[8] == "O") and (board[0] != "O" and board[0] != "X"):
        move = 0
    elif (board[2] == "O" and board[4] == "O") and (board[6] != "O" and board[6] != "X"):
        move = 6
    elif (board[2] == "O" and board[6] == "O") and (board[4] != "O" and board[4] != "X"):
        move = 4
    elif (board[4] == "O" and board[6] == "O") and (board[2] != "O" and board[2] != "X"):
        move = 2

    #IF NO OTHER VALID MOVES FOUND, RANDOM
    if move == -1:
        move = m

    if board[move] != "O" and board[move] != "X":
        return move
    else:
        return comp_move(board, move_number)

def comp_play(board, c):
    board[comp_move(board, c)] = "O"

def ttt():
    b = ["1", "2", "3", "4","5", "6","7", "8", "9"]
    w = False
    count = 0
    print_board(b)
    while w == False and count < 5:
        player_move(b)
        w = win(b)
        if w == "X":
            print_board(b)
            print("You win!")
            return 0, 1
        if count == 4:
            print("It's a tie!")
            return 0, 0
        comp_play(b, count)
        print_board(b)
        w = win(b)
        count = count + 1
    if w == "O":
        print("Computer wins!")
        return 1, 0
    else:
        print("It's a tie!")
        return 0, 0

def game ():
    print("How many rounds would you like to play?")
    num_rounds = int(input())
    player_score = 0
    comp_score = 0
    while num_rounds > 0:
        print("Number of rounds left: " + str(num_rounds))
        print("Current Score " + str(player_score) + " - " + str(comp_score))
        comp_add, p_add = ttt()
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

def tic_tac_toe():
    print("***********************************************")
    print("******************TIC TAC TOE******************")
    print("Would you like to play tic tac toe? Y/N")
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