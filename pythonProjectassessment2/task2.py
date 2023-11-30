def check_winner():
    return

def player1():
    inpy = int(input("Player 1:Write the column: "))
    inpx = int(input("Player 1 :Write the row"))

    if inpy == 1:
        board[inpy][inpx] = 'X'
        display()
    if inpy == 2:
        board[inpy][inpx] = 'X'
        display()
    if inpy == 3:
        board[inpy][inpx] = 'X'
        display()

    if inpy == 4:
        board[inpy][inpx] = 'X'
        display()

    if inpy == 5:
        num = inpy + 1
        board[inpy][inpx] = 'X'
        display()

    if inpy == 6:
        num = inpy + 1
        board[inpy][inpx] = 'X'
        display()

def player2():
    inpy = int(input("Player 2:Write the column: "))
    inpx = int(input("Player 2 :Write the row"))

    if inpy == 1:
        board[inpy][inpx] = 'O'
        display()
    if inpy == 2:
        board[inpy][inpx] = 'O'
        display()
    if inpy == 3:
        board[inpy][inpx] = 'O'
        display()

    if inpy == 4:
        board[inpy][inpx] = 'O'
        display()

    if inpy == 5:
        num = inpy + 1
        board[inpy][inpx] = 'O'
        display()

    if inpy == 6:
        num = inpy + 1
        board[inpy][inpx] = 'O'
        display()

def display():

    print(board[0])
    print(board[1])
    print(board[2])
    print(board[3])
    print(board[4])
    print(board[5])


def print_board(board, cell, row):
    # This function should print the board at the terminal
    # Inputs: board, a nested list which contains the current status of the board
    for row in board:
        print("|", end="")
        for cell in row:
            print(cell, end="|")
        print()
    print("---------------")
    print(" 1 2 3 4 5 6 7 ")




inpy = 0
inpx = 0

board = [["|", "", "", "", "", "", "", "", "|"],
            ["|", "", "", "", "", "", "", "", "|"],
            ["|", "", "", "", "", "", "", "", "|"],
            ["|", "", "", "", "", "", "", "", "|"],
            ["|", "", "", "", "", "", "", "", "|"],
            ["|", "", "", "", "", "", "", "", "|"]]
count = 0

display()



while count != 42:
    player1()
    player2()
    count = count + 1
else:
    print("Game is a draw")



