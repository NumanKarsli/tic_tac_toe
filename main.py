board = [
    [" ", " ", " "],
    [" ", " ", " "],
    [" ", " ", " "],
]

who = 0     # 0 means Player 1 (O letter),   1 means player 2 (X letter)


def displayBoard():
    print()
    print(f"1: {board[0][0]} | {board[0][1]} | {board[0][2]} \n -----------\n2: {board[1][0]} | {board[1][1]} | {board[1][2]} \n -----------\n3: {board[2][0]} | {board[2][1]} | {board[2][2]} \n   A   B   C")
    print()

def get_row_col(a):
    my_list = [1, 1]
    if a[0] == "A":
        my_list[1] = 0
    elif a[0] == "B":
        my_list[1] = 1
    elif a[0] == "C":
        my_list[1] = 2
    if a[1] == "1":
        my_list[0] = 0
    elif a[1] == "2":
        my_list[0] = 1
    elif a[1] == "3":
        my_list[0] = 2
    return my_list


def move(who):
    if who == 0:
        game = input(
            "Player 1, play your game (O) (for example A1) : ").upper()
        moveList = get_row_col(game)
        board[moveList[0]][moveList[1]] = "O"
        displayBoard()
        changePlayer()
    else:
        game = input(
            "Player 2, play your game (X) (for example A1) : ").upper()
        moveList = get_row_col(game)
        board[moveList[0]][moveList[1]] = "X"
        displayBoard()
        changePlayer()


def changePlayer():
    global who
    if who == 0:
        who = 1
    else:
        who = 0

print()
print("Welcome to Numan Personal Tic Tac Toe game")
print()

displayBoard()


while True:
    if board[0][0] == board[0][1] == board[0][2] == "X":
        print("Player 2 wins (X)")
        break
    elif board[1][0] == board[1][1] == board[1][2] == "X":
        print("Player 2 wins (X)")
        break
    elif board[2][0] == board[2][1] == board[2][2] == "X":
        print("Player 2 wins (X)")
        break
    elif board[0][0] == board[1][0] == board[2][0] == "X":
        print("Player 2 wins (X)")
        break
    elif board[0][1] == board[1][1] == board[2][1] == "X":
        print("Player 2 wins (X)")
        break
    elif board[0][2] == board[1][2] == board[2][2] == "X":
        print("Player 2 wins (X)")
        break
    elif board[0][0] == board[1][1] == board[2][2] == "X":
        print("Player 2 wins (X)")
        break
    elif board[0][2] == board[1][1] == board[2][0] == "X":
        print("Player 2 wins (X)")
        break
    if board[0][0] == board[0][1] == board[0][2] == "O":
        print("Player 1 wins (O)")
        break
    elif board[1][0] == board[1][1] == board[1][2] == "O":
        print("Player 1 wins (O)")
        break
    elif board[2][0] == board[2][1] == board[2][2] == "O":
        print("Player 1 wins (O)")
        break
    elif board[0][0] == board[1][0] == board[2][0] == "O":
        print("Player 1 wins (O)")
        break
    elif board[0][1] == board[1][1] == board[2][1] == "O":
        print("Player 1 wins (O)")
        break
    elif board[0][2] == board[1][2] == board[2][2] == "O":
        print("Player 1 wins (O)")
        break
    elif board[0][0] == board[1][1] == board[2][2] == "O":
        print("Player 1 wins (O)")
        break
    elif board[0][2] == board[1][1] == board[2][0] == "O":
        print("Player 1 wins (O)")
        break
    elif " " not in board[0] and " " not in board[1] and " " not in board[2]:
        print("It is a tie")
        break
    else:
        move(who)