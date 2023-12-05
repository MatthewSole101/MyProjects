import time
def check_winner():
    return

def player1():
    starttimer = time.time()
    inpy = int(input("Player 1:Write the column: "))
    inpx = int(input("Player 1 :Write the row"))
    endtimer = time.time()
    movetime = int(endtimer-starttimer)
    print(movetime, "seconds")

    if movetime <= 5:

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

    elif movetime > 5:
        print("You took too long! - player 2's turn")
        display()
        return 0

def player2():
    starttimer = time.time()
    inpy = int(input("Player 2:Write the column: "))
    inpy = inpy - 1
    inpx = int(input("Player 2 :Write the row"))
    endtimer = time.time()
    movetime = int(endtimer-starttimer)
    print(movetime, "seconds")
    # if inpy
    if movetime <= 5:

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
    elif movetime > 5:
        print("You took too long! - player 1's turn")
        display()
        return 0

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

display()



while count != 42:
    player1()
    player2()
    count = count + 1
    print("You have", 42-count, "goes left")
else:
    print("Game is a draw")


