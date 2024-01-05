import time, random

def PopOutPlayer1(x):
    if board[5][x] == 'X':
        print("Hello")
        board[5][x] = board[4][x]
        board[4][x] = board[3][x]
        board[3][x] = board[2][x]
        board[2][x] = board[1][x]
        board[1][x] = board[0][x]
        board[0][x] = ""
    elif board[0][x] == 'O':
        print("Error: Wrong piece inputed")
        return None
    else:
        print("Input is invalid")

def PopOutPlayer2(x):
    if board[5][x] == 'O':
        print("Hello")
        board[5][x] = board[4][x]
        board[4][x] = board[3][x]
        board[3][x] = board[2][x]
        board[2][x] = board[1][x]
        board[1][x] = board[0][x]
        board[0][x] = ""
    elif board[0][x] == 'X':
        print("Error: Wrong piece inputed")
        return None
    else:
        print("Input is invalid")


def special_move(x):
    count2 = 5
    count = 1

    while count != 0:
        if board[count2][x] != '':
            count2 = count2 - 1
        elif board[count2][x] == '':
            while count != 8:
                board[count2][count] = ''
                count += 1
            break

def random_obstruct_cells():
    rand = random.randint(1,6)
    count = 5
    no = 'N'
    count2 = 1
    while count != 2:
        #y axis
        board[0+count][rand] = no
        board[0+count][rand+1] = no
        count = count - 1

def remove_random_obstruct_cells():
    count = 1
    while count != 8:
        if board [0][count] == 'N':
            board[0][count] = ''

        if board[1][count] == 'N':
            board[1][count] = ''

        if board[2][count] == 'N':
            board[2][count] = ''

        if board[3][count] == 'N':
            board[3][count] = ''

        if board[4][count] == 'N':
            board[4][count] = ''

        if board[5][count] == 'N':
            board[5][count] = ''

        count = count + 1

def player2_winner():
    count = 0
    playercount = 0
    lastcount = 0
    while count != 6:
        for i in range(1, 3):
            if board[count][i] == 'O' and board[count][i + 1] == 'O' and board[count][i + 2] == 'O' and board[count][i + 3] == 'O':
                playercount += 1
            if board[i][count] == 'O' and board[i+1][count] == 'O' and board[i+2][count] == 'O' and board[i+3][count] == 'O':
                playercount += 1


        count = count + 1
    else:

        return playercount

def player1_winner():
    count = 0
    playercount = 0
    lastcount = 0
    while count != 6:
        for i in range(1, 3):
            if board[count][i] == 'X' and board[count][i + 1] == 'X' and board[count][i + 2] == 'X' and board[count][i + 3] == 'X':
                playercount += 1
            if board[i][count] == 'X' and board[i + 1][count] == 'X' and board[i + 2][count] == 'X' and board[i + 3][count] == 'X':
                playercount += 1

        count = count + 1
    else:
        return playercount


def player1():
    try:
        x = 5
        starttimer = time.time()

        inpx = int(input("Player 1: Write the row(1-7): "))
        endtimer = time.time()
        movetime = int(endtimer - starttimer)
        print(movetime, "seconds")
        inpchoice = input("Do you wnat to use your special move or PopOut?(S/P) or No(N) or Check Score(C):  ")


        if board [5][inpx] != 'N':
            if inpchoice == 'N' or inpchoice == 'n':

                if movetime <= 5:
                    for i in board:
                        while board[x][inpx] != '':
                            x = x - 1
                        else:
                            board[x][inpx] = 'X'
                            display()
                            break

                    else:
                        print("Cant make that move: next players go")
                elif movetime > 5:
                    print("You took too long! - player 2's turn")
                    display()
                    return 0

            elif inpchoice == 'S' or inpchoice == 's':
                special_move(inpx)
                display()
            elif inpchoice == 'P' or inpchoice == 'p':
                print("Player 1 has removed an item from the board")
                PopOutPlayer1(inpx)
                display()
            elif inpchoice == 'C' or inpchoice == 'c':
                print("Player 1 has", player1_winner(), "points")
                print("Player 2 has", player2_winner(), "points")
                display()

        else:
            print("Not playable area!: Player 2's turn")
            display()
    except KeyboardInterrupt:
        print("User interrupted")

def player2():
    try:
        x = 5
        starttimer = time.time()
        inpx = int(input("Player 2: Write the row(1-7): "))
        endtimer = time.time()
        movetime = int(endtimer - starttimer)
        print(movetime, "seconds")
        # inpspecial = input("Do you wnat to use your special move?(Y/N): ")
        inpchoice = input("Do you wnat to use your special move or PopOut?(S/P) or No(N) or Check Score(C):  ")


        if board [5][inpx] != 'N':

            if inpchoice == 'N' or inpchoice == 'n':

                if movetime <= 5:
                    for i in board:
                        while board[x][inpx] != '':
                            x = x - 1
                        else:
                            board[x][inpx] = 'O'
                            # display()
                            break

                    else:
                        print("Cant make that move: next players go")
                elif movetime > 5:
                    print("You took too long! - player 1's turn")
                    # display()
                    return 0
            elif inpchoice == 'S' or inpchoice == 's':
                special_move(inpx)
            elif inpchoice == 'P' or inpchoice == 'p':
                print("Player 2 has removed an item from the board")
                PopOutPlayer2(inpx)
                # display()
            elif inpchoice == 'C' or inpchoice == 'c':
                print("Player 1 has", player1_winner(), "points")
                print("Player 2 has", player2_winner(), "points")
                display()
        else:
            print("Not playable area!: Player 1's turn")
            display()
    except KeyboardInterrupt:
        print("User interrupted")

def display():

    print(board[0])
    print(board[1])
    print(board[2])
    print(board[3])
    print(board[4])
    print(board[5])



board = [["|", "", "", "", "", "", "", "", "|"],
            ["|", "", "", "", "", "", "", "", "|"],
            ["|", "", "", "", "", "", "", "", "|"],
            ["|", "", "", "", "", "", "", "", "|"],
            ["|", "", "", "", "", "", "", "", "|"],
            ["|", "", "", "", "", "", "", "", "|"]]
count = 0
count3 = 0
Player1Count = 0
Player1Count2 = 0
Player2Count = 0
Player2Count2 = 0

random_obstruct_cells()
display()



while count != 42:


    player1()
    # player1_winner()
    player2()
    player2_winner()

    if count3 != 1:
        remove_random_obstruct_cells()
        count3 = count3 + 1
    display()
    count = count + 1
    print("You have", 42-count, "goes left")
    print("Player 2:", Player2Count2, "points")

else:
    player1_winner()
    player2_winner()
    print("You have", 42 - count, "goes left")
    print("Player 2:", Player2Count2, "points")
    print("Game is a draw")

