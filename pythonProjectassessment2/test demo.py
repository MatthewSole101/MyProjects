import time, random


def PopOutPlayer1(y, x):
    if board[y][x] == 'X':
        board[y][x] = ''
    elif board[y][x] == 'O':
        print("Error: Wrong piece inputed")
        return None
    else:
        print("Input is invalid")


def PopOutPlayer2(y, x):
    if board[y][x] == 'O':
        board[y][x] = ''
    elif board[y][x] == 'X':
        print("Error: Wrong piece inputed")
        return None
    else:
        print("Input is invalid")


def special_move(y, x):
    for i in board[x]:
        if board[y][i] != '':
            board[y][i] = ''
    return board[y]


def random_obstruct_cells():
    rand = random.randint(1, 6)
    count = 0
    no = 'N'
    count2 = 1
    while count != 3:
        # y axis
        board[0 + count][rand].append(no)
        board[0 + count][rand + 1].append(no)
        count = count + 1


def remove_random_obstruct_cells():
    count = 0
    while count != 5:
        if board[0][count] == 'N':
            board[0][count] = ''

        if board[1][count] == 'N':
            board[0][count] = ''

        if board[2][count] == 'N':
            board[0][count] = ''

        if board[3][count] == 'N':
            board[0][count] = ''

        if board[4][count] == 'N':
            board[0][count] = ''

        if board[5][count] == 'N':
            board[0][count] = ''

        count = count + 1


def check_winner():
    # rows

    # colums

    return


def player1():
    x = 5
    starttimer = time.time()
    # inpy = int(input("Player 1:Write the column: "))
    # if inpy == 1:
    #     inpy = 0
    # elif inpy > 1:
    #     inpy = inpy - 1
    inpx = int(input("Player 1 :Write the row"))
    endtimer = time.time()
    movetime = int(endtimer - starttimer)
    print(movetime, "seconds")
    inpchoice = input("Do you wnat to use your special move or PopOut?(S/P) or No(N):  ")

    # inpspecial = input("Do you wnat to use your special move or PopOut?(Y/N): ")

    # if board[inpy][inpx] == 'O':
    #     return print("Cant make that move: next players go")

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

            #
            # if board[inpy][inpx] != 'N':
            #
            #     if inpy == 0:
            #         board[inpy][inpx] = 'X'
            #         display()
            #     if inpy == 1:
            #         board[inpy][inpx] = 'X'
            #         display()
            #     if inpy == 2:
            #         board[inpy][inpx] = 'X'
            #         display()
            #     if inpy == 3:
            #         board[inpy][inpx] = 'X'
            #         display()
            #
            #     if inpy == 4:
            #         board[inpy][inpx] = 'X'
            #         display()
            #
            #     if inpy == 5:
            #         num = inpy + 1
            #         board[inpy][inpx] = 'X'
            #         display()
            #
            #     if inpy == 6:
            #         num = inpy + 1
            #         board[inpy][inpx] = 'X'
            #         display()
            # else:
            #     print("Invalid Input")

        elif movetime > 5:
            print("You took too long! - player 2's turn")
            display()
            return 0

    elif inpchoice == 'Y' or inpchoice == 'y':
        # special_move(inpy, inpx)
        display()
    elif inpchoice == 'P' or inpchoice == 'p':
        print("Player 1 has removed an item from the board")
        PopOutPlayer1(0, inpx)
        display()


def player2():
    x = 5
    starttimer = time.time()
    # inpy = int(input("Player 2:Write the column: "))
    # if inpy == 1:
    #     inpy = 0
    # elif inpy > 1:
    #     inpy = inpy - 1
    inpx = int(input("Player 2 :Write the row"))
    endtimer = time.time()
    movetime = int(endtimer - starttimer)
    print(movetime, "seconds")
    # inpspecial = input("Do you wnat to use your special move?(Y/N): ")
    inpchoice = input("Do you wnat to use your special move or PopOut?(S/P) or No(N):  ")

    # if board[inpy][inpx] == 'O':
    #     return print("Cant make that move: next players go")

    if inpchoice == 'N' or inpchoice == 'n':

        if movetime <= 5:
            for i in board:
                while board[x][inpx] != '':
                    x = x - 1
                else:
                    board[x][inpx] = 'O'
                    display()
                    break

            else:
                print("Cant make that move: next players go")

            # if board[inpy][inpx] != 'N':
            #
            #     if inpy == 0:
            #         board[inpy][inpx] = 'O'
            #         display()
            #     if inpy == 1:
            #         board[inpy][inpx] = 'O'
            #         display()
            #     if inpy == 2:
            #         board[inpy][inpx] = 'O'
            #         display()
            #     if inpy == 3:
            #         board[inpy][inpx] = 'O'
            #         display()
            #
            #     if inpy == 4:
            #         board[inpy][inpx] = 'O'
            #         display()
            #
            #     if inpy == 5:
            #         num = inpy + 1
            #         board[inpy][inpx] = 'O'
            #         display()
            #
            #     if inpy == 6:
            #         num = inpy + 1
            #         board[inpy][inpx] = 'O'
            #         display()
        elif movetime > 5:
            print("You took too long! - player 1's turn")
            display()
            return 0
    elif inpchoice == 'Y' or inpchoice == 'y':
        # special_move(inpy, inpx)
        display()
    elif inpchoice == 'P' or inpchoice == 'p':
        print("Player 2 has removed an item from the board")
        PopOutPlayer2(0, inpx)
        display()


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
display()
print(len(board))
while count != 42:
    # while count3 != 1:
    #     random_obstruct_cells()
    #     count3 = count3 + 1
    player1()
    player2()
    count = count + 1
    print("You have", 42 - count, "goes left")
    remove_random_obstruct_cells()

else:
    print("Game is a draw")

