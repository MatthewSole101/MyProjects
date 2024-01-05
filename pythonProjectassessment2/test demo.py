def checkwiner():
    count = 0
    while count != 6:
        for i in range(1,3):
            if board [count][i] == 'O' and board[count][i+1] == 'O' and board[count][i+2] == 'O' and board[count][i+3] == 'O':
                print("Winner")
        count = count + 1

def display():
        print(board[0])
        print(board[1])
        print(board[2])
        print(board[3])
        print(board[4])
        print(board[5])

board = [["|", "", "", "", "", "", "", "", "|"],
             ["|", "", "", "", "", "", "", "", "|"],
             ["|", "X", "", "", "", "", "", "", "|"],
             ["|", "X", "", "", "", "", "", "", "|"],
             ["|", "X", "", "", "", "", "", "", "|"],
             ["|", "X", "O", "O", "O", "O", "", "", "|"]]

checkwiner()