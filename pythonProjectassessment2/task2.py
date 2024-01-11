import time, random

disccount =0
from filecmp import cmp

def check_full():
    Player1Count = board[0].count('X')
    Player2Count = board[0].count('O')

    sumcheck = Player1Count + Player2Count

    if sumcheck == 7:
        return True
    else:
        return False


#Popout function for player 1
def PopOutPlayer1(x):

    if board[5][x] == 'X':

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
        board[5][x] = board[4][x]
        board[4][x] = board[3][x]
        board[3][x] = board[2][x]
        board[2][x] = board[1][x]
        board[1][x] = board[0][x]
        board[0][x] = ""
        disccount =- 1

    elif board[0][x] == 'X':
        print("Error: Wrong piece inputed")
        return None
    else:
        print("Input is invalid")


def special_move(x):
    count2 = 5
    count = 1
    count3 = 0

    #Loops through the whole row to remove any inputs and make them blank("")
    while count != 0:
        if board[count2][x] != '':
            count2 = count2 - 1
        elif board[count2][x] == '':
            while count != 8:
                count3 = 1
                board[count2][count] = ''
                board[count2][count] = board[count2 - 1][count]

                count += 1
            else:
                count4 = 1
                count = 0
                count3 = count2 - 5
                while count4  != count3:
                    while count != 8:
                        board[count2 + count4][count] = board[(count2 + count4)-1][count]
                        count += 1
                    count4 = count4 + 1
    return 0


#Randomly creates obstructed cells which doesnt allow users to go on there first rounds
def random_obstruct_cells():
    rand = random.randint(1,6)
    count = 5
    count2 = 1
    while count != 2:
        #y axis
        board[0+count][rand] = 'N'
        board[0+count][rand+1] = 'N'
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
    count5 = 0
    playercount = 0
    lastcount = 0
    count2 = 4
    count3 = 5
    count = 1
    while count5 != 6:
        for i in range(1, 3):
            if board[count5][i] == 'O' and board[count5][i + 1] == 'O' and board[count5][i + 2] == 'O' and board[count5][i + 3] == 'O':
                playercount += 1
            if board[i][count5] == 'O' and board[i+1][count5] == 'O' and board[i+2][count5] == 'O' and board[i+3][count5] == 'O':
                playercount += 1


        count5 = count5 + 1
    else:
        if board[3][1] == 'O' and board[2][2] == 'O' and board[1][3] == 'O' and board[0][4] == 'O':
            playercount += 1

        if board[count2][count] == 'O' and board[count2 - 1][count + 1] == 'O' and board[count2 - 2][count + 2] == 'O' and board[count2 - 3][count + 3] == 'O':
            playercount += 1

        if board[count2 - 1][count + 1] == 'O' and board[count2 - 2][count + 2] == 'O' and board[count2 - 3][count + 3] == 'O' and board[count2 - 4][count + 4] == 'O':
            playercount += 1

        if board[count3][count] == 'O' and board[count3 - 1][count + 1] == 'O' and board[count3 - 2][count + 2] == 'O' and board[count3 - 3][count + 3] == 'O':
            playercount += 1
        if board[count3 - 1][count + 1] == 'O' and board[count3 - 2][count + 2] == 'O' and board[count3 - 3][count + 3] == 'O' and board[count3 - 4][count + 4] == 'O':
            playercount += 1
        if board[count3 - 2][count + 2] == 'O' and board[count3 - 3][count + 3] == 'O' and board[count3 - 4][count + 4] == 'O' and board[count3 - 5][count + 5] == 'O':
            playercount += 1

        if board[count3][count + 1] == 'O' and board[count3 - 1][count + 2] == 'O' and board[count3 - 2][count + 3] == 'O' and board[count3 - 3][count + 4] == 'O':
            playercount += 1
        if board[count3 - 1][count + 2] == 'O' and board[count3 - 2][count + 3] == 'O' and board[count3 - 3][count + 4] == 'O' and board[count3 - 4][count + 5] == 'O':
            playercount += 1
        if board[count3 - 2][count + 3] == 'X' and board[count3 - 3][count + 4] == 'X' and board[count3 - 4][count + 5] == 'X' and board[count3 - 5][count + 6] == 'O':
            playercount += 1

        if board[5][3] == 'O' and board[4][4] == 'O' and board[3][5] == 'O' and board[2][6] == 'O':
            playercount += 1
        if board[4][4] == 'O' and board[3][5] == 'O' and board[2][6] == 'O' and board[1][7] == 'O':
            playercount += 1

        if board[5][4] == 'O' and board[4][5] == 'O' and board[3][6] == 'O' and board[2][7] == 'O':
            playercount += 1

        if board[5][4] == 'O' and board[4][3] == 'O' and board[3][2] == 'O' and board[2][1] == 'O':
            playercount += 1
        if board[5][5] == 'O' and board[4][4] == 'O' and board[3][3] == 'O' and board[2][2] == 'O':
            playercount += 1
        if board[4][4] == 'O' and board[3][3] == 'O' and board[2][2] == 'O' and board[1][1] == 'O':
            playercount += 1

        if board[5][6] == 'O' and board[4][5] == 'O' and board[3][4] == 'O' and board[2][3] == 'O':
            playercount += 1
        if board[4][5] == 'O' and board[3][4] == 'O' and board[2][3] == 'O' and board[1][2] == 'O':
            playercount += 1
        if board[3][4] == 'O' and board[2][3] == 'O' and board[1][2] == 'O' and board[0][1] == 'O':
            playercount += 1

        if board[5][7] == 'O' and board[4][6] == 'O' and board[3][5] == 'O' and board[2][4] == 'O':
            playercount += 1
        if board[4][6] == 'O' and board[3][5] == 'O' and board[2][4] == 'O' and board[1][3] == 'O':
            playercount += 1
        if board[3][5] == 'O' and board[2][4] == 'O' and board[1][3] == 'O' and board[0][2] == 'O':
            playercount += 1

        if board[4][7] == 'O' and board[3][6] == 'O' and board[2][5] == 'O' and board[1][4] == 'O':
            playercount += 1
        if board[3][6] == 'O' and board[2][5] == 'O' and board[1][4] == 'O' and board[0][3] == 'O':
            playercount += 1

        if board[3][7] == 'O' and board[2][6] == 'O' and board[1][5] == 'O' and board[0][4] == 'O':
            playercount += 1

        return playercount

def player1_winner():
    count5 = 0
    playercount = 0
    lastcount = 0
    count2 = 4
    count3 = 5
    count = 1
    while count5 != 6:
        for i in range(1, 3):
            if board[count5][i] == 'X' and board[count5][i + 1] == 'X' and board[count5][i + 2] == 'X' and board[count5][i + 3] == 'X':
                playercount += 1
            if board[i][count5] == 'X' and board[i + 1][count5] == 'X' and board[i + 2][count5] == 'X' and board[i + 3][count5] == 'X':
                playercount += 1

        count5 = count5 + 1
    else:
        if board[3][1] == 'X' and board[2][2] == 'X' and board[1][3] == 'X' and board[0][4] == 'XO':
            playercount += 1

        if board[count2][count] == 'X' and board[count2 - 1][count + 1] == 'X' and board[count2 - 2][count + 2] == 'X' and board[count2 - 3][count + 3] == 'X':
            playercount += 1

        if board[count2 - 1][count + 1] == 'X' and board[count2 - 2][count + 2] == 'X' and board[count2 - 3][count + 3] == 'X' and board[count2 - 4][count + 4] == 'X':
            playercount += 1

        if board[count3][count] == 'X' and board[count3 - 1][count + 1] == 'X' and board[count3 - 2][count + 2] == 'X' and board[count3 - 3][count + 3] == 'X':
            playercount += 1
        if board[count3 - 1][count + 1] == 'X' and board[count3 - 2][count + 2] == 'X' and board[count3 - 3][count + 3] == 'X' and board[count3 - 4][count + 4] == 'X':
            playercount += 1
        if board[count3 - 2][count + 2] == 'X' and board[count3 - 3][count + 3] == 'X' and board[count3 - 4][count + 4] == 'X' and board[count3 - 5][count + 5] == 'X':
            playercount += 1

        if board[count3][count + 1] == 'X' and board[count3 - 1][count + 2] == 'X' and board[count3 - 2][count + 3] == 'X' and board[count3 - 3][count + 4] == 'X':
            playercount += 1
        if board[count3 - 1][count + 2] == 'X' and board[count3 - 2][count + 3] == 'X' and board[count3 - 3][count + 4] == 'X' and board[count3 - 4][count + 5] == 'X':
            playercount += 1
        if board[count3 - 2][count + 3] == 'X' and board[count3 - 3][count + 4] == 'X' and board[count3 - 4][count + 5] == 'X' and board[count3 - 5][count + 6] == 'X':
            playercount += 1

        if board[5][3] == 'X' and board[4][4] == 'X' and board[3][5] == 'X' and board[2][6] == 'X':
            playercount += 1
        if board[4][4] == 'X' and board[3][5] == 'X' and board[2][6] == 'X' and board[1][7] == 'X':
            playercount += 1

        if board[5][4] == 'X' and board[4][5] == 'X' and board[3][6] == 'X' and board[2][7] == 'X':
            playercount += 1

        if board[5][4] == 'X' and board[4][3] == 'X' and board[3][2] == 'X' and board[2][1] == 'X':
            playercount += 1
        if board[5][5] == 'X' and board[4][4] == 'X' and board[3][3] == 'X' and board[2][2] == 'X':
            playercount += 1
        if board[4][4] == 'X' and board[3][3] == 'X' and board[2][2] == 'X' and board[1][1] == 'X':
            playercount += 1

        if board[5][6] == 'X' and board[4][5] == 'X' and board[3][4] == 'X' and board[2][3] == 'X':
            playercount += 1
        if board[4][5] == 'X' and board[3][4] == 'X' and board[2][3] == 'X' and board[1][2] == 'X':
            playercount += 1
        if board[3][4] == 'X' and board[2][3] == 'X' and board[1][2] == 'X' and board[0][1] == 'X':
            playercount += 1

        if board[5][7] == 'X' and board[4][6] == 'X' and board[3][5] == 'X' and board[2][4] == 'X':
            playercount += 1
        if board[4][6] == 'X' and board[3][5] == 'X' and board[2][4] == 'X' and board[1][3] == 'X':
            playercount += 1
        if board[3][5] == 'X' and board[2][4] == 'X' and board[1][3] == 'X' and board[0][2] == 'X':
            playercount += 1

        if board[4][7] == 'X' and board[3][6] == 'X' and board[2][5] == 'X' and board[1][4] == 'X':
            playercount += 1
        if board[3][6] == 'X' and board[2][5] == 'X' and board[1][4] == 'X' and board[0][3] == 'X':
            playercount += 1

        if board[3][7] == 'X' and board[2][6] == 'X' and board[1][5] == 'X' and board[0][4] == 'X':
            playercount += 1

        return playercount


def player1():
    try:
        x = 5

        starttimer = time.time()

        inpx = int(input("Player 1: Write the row(1-7) or check score(0): "))
        endtimer = time.time()
        movetime = int(endtimer - starttimer)
        print(movetime, "seconds")
        # inpchoice = input("Do you wnat to use your special move or PopOut?(S/P) or No(N) or Check Score(C):  ")

        if board[5][inpx] != 'N':
            if movetime <= 5:
                inpchoice = input("Do you want to PopOut?(P) or No(N) or Check Score(C):  ")

                if inpchoice == 'N' or inpchoice == 'n':
                    #checks what part of the column is empty so the player disc can go
                    for i in board:
                        while board[x][inpx] != '':
                            x = x - 1
                        else:
                            board[x][inpx] = 'X'
                            display()
                            break

                    else:
                        print("Cant make that move: next players go")

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

                    player1win = int(player1_winner())
                    player2win = int(player2_winner())



                    if player1win > player2win:
                        print("Player1 is leading")
                    elif player1win < player2win:
                        print("Player2 is leading")
                    else:
                        print("Currently a draw Draw!")
                    display()
                else:
                    print("Invalid input")
                    display()


            elif movetime > 5:
                print("You took too long! - player 2's turn")
                display()
                return 0
        else:
            print("Not playable area!: Player 2's turn")
            display()
    #Error handling
    except KeyboardInterrupt:
        print("User interrupted")
    except ValueError:
        print("Wrong allowed  input type: Player 2's turn")
        display()
    except IndexError:
        print("Input was out of range!: Players 2's turn")
        display()

def player2():
    try:
        x = 5
        starttimer = time.time()
        inpx = int(input("Player 2: Write the row(1-7) or check score(0): "))
        endtimer = time.time()
        movetime = int(endtimer - starttimer)
        print(movetime, "seconds")

        if board [5][inpx] != 'N':
            if movetime <= 5:
                inpchoice = input("Do you want to PopOut?(P) or No(N) or Check Score(C):  ")

                if inpchoice == 'N' or inpchoice == 'n':

                        for i in board:
                            while board[x][inpx] != '':
                                x = x - 1
                            else:
                                board[x][inpx] = 'O'
                                # display()
                                break

                        else:
                            print("Cant make that move: next players go")

                elif inpchoice == 'S' or inpchoice == 's':
                    special_move(inpx)
                elif inpchoice == 'P' or inpchoice == 'p':
                    print("Player 2 has removed an item from the board")
                    PopOutPlayer2(inpx)
                    # display()
                elif inpchoice == 'C' or inpchoice == 'c':
                    print("Player 1 has", player1_winner(), "points")
                    print("Player 2 has", player2_winner(), "points")

                    player1win = int(player1_winner())
                    player2win = int(player2_winner())

                    if player1win > player2win:
                        print("Player1 is leading")
                    elif player1win < player2win:
                        print("Player2 is leading")
                    else:
                        print("Currently a draw Draw!")
            elif movetime > 5:
                print("You took too long! - player 1's turn")
                # display()
                return 0
        else:
            print("Not playable area!: Player 1's turn")
    except KeyboardInterrupt:
        print("User interrupted")
    except ValueError:
        print("Wrong allowed  input type: Player 1's turn")
    except IndexError:
        print("Input was out of range!: Players 1's turn")


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



while not check_full():


    player1()

    player2()

    #After both player1 and player2 had their goes - obstructed cells then get removed
    if count3 != 1:
        remove_random_obstruct_cells()
        count3 = count3 + 1
    display()



else:


    player1win = int(player1_winner())
    player2win = int(player2_winner())

    if player1win > player2win:
        print("Player1 has won!")
    elif player1win < player2win:
        print("Player2 has won!")
    else:
        print("It's a Draw!")

