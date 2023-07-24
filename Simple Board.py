def best_move(board):
    # TODO: Add a working code to play best move
    # return a string of 2 characters each from 0 to 2
    """
    bestMove=NULL
    for each legal move on the board:
        if *currentMove is better than bestMove*:
            bestMove=currentMove
    return bestMove
    """
    # Bad algorithm:
    for i in range(3):
        for j in range(3):
            if board[i][j] == "_":
                return str(i) + str(j)


""" 
if board[int(n[0])][0] == board[int(n[0])] and if board[int(n[0])][1] == board[int(n[0])][2]:
    win

if board[0][int(n[1])] == board[1][int(n[1])] and if board[1][int(n[1])] == board[2][int(n[1])]:
    win
    
if n[0] == n[1]:
    if board[0][0] == board[1][1] and board[1][1] == board[2][2]:
        win
    if board[0][2] == board[1][1] and board[1][1] == board[2][0]:
        win 
"""


def check(board, turn):
    for row in range(3):
        if board[row][0] == board[row][1] and board[row][1] == board[row][2]:
            if board[row][0] != "_":
                if turn == 1:
                    return "player"
                else:
                    return "computer"

    for col in range(3):
        if board[0][col] == board[1][col] and board[1][col] == board[2][col]:
            if board[0][col] != "_":
                if turn == 1:
                    return "player"
                else:
                    return "computer"

    if board[0][0] == board[1][1] and board[1][1] == board[2][2]:
        if board[0][0] != "_":
            if turn == 1:
                return "player"
            else:
                return "computer"

    if board[0][2] == board[1][1] and board[1][1] == board[2][0]:
        if board[1][1] != "_":
            if turn == 1:
                return "player"
            else:
                return "computer"
    for i in range(3):
        for j in range(3):
            if board[i][j] == "_":
                return None
    return "draw"


def minimax(board, depth, turn):
    # minimax(board, depth, turn==1) ??
    # TODO: Add minimax algorithm
    """
    if check(board,turn) returns win, loss or draw:
        return value of board
    if turn==1:
        if depth = diffficulty_depth: #Check TODO: after hardest
                    return -Infty
        bestVal = -Infty
        for each move on Board:
            value = minimax(board, depth+1, 1-turn)
            #value = minimax(board, depth+1, 0) also possible??
            bestVal = max(bestVal, value)

        return bestVal
    else:
        if depth = diffficulty_depth: #Check TODO: after hardest
                return +Infty
        bestVal = +Infty
        for each move on Board:
            value = minimax(board, depth+1, 1-turn)
            #value = minimax(board, depth+1, 1) also possible??

            bestVal = min(bestVal, value)
        return bestVal
    """
    pass


def evaluate(board):
    # checking for computer as winner
    # checking diagonals
    if board[1][1] == "X" and board[0][0] == "X" and board[2][2] == "X":
        return 11
    if board[1][1] == "X" and board[0][2] == "X" and board[2][0] == "X":
        return 11

    # checking horizontals
    if board[0][0] == "X" and board[0][1] == "X" and board[0][2] == "X":
        return 11
    if board[1][0] == "X" and board[1][1] == "X" and board[1][2] == "X":
        return 11
    if board[2][0] == "X" and board[2][1] == "X" and board[2][2] == "X":
        return 11

    # checking verticals
    if board[0][0] == "X" and board[1][0] == "X" and board[2][0] == "X":
        return 11
    if board[0][1] == "X" and board[1][1] == "X" and board[2][1] == "X":
        return 11
    if board[0][2] == "X" and board[1][2] == "X" and board[2][2] == "X":
        return 11
    """
    
    
    
    
    
    
    
    
    
    
    
    
    
    """

    # checking for player as winner
    # checking diagonals
    if board[1][1] == "O" and board[0][0] == "O" and board[2][2] == "O":
        return -11
    if board[1][1] == "O" and board[0][2] == "O" and board[2][0] == "O":
        return -11

    # checking horizontals
    if board[0][0] == "O" and board[0][1] == "O" and board[0][2] == "O":
        return -11
    if board[1][0] == "O" and board[1][1] == "O" and board[1][2] == "O":
        return -11
    if board[2][0] == "O" and board[2][1] == "O" and board[2][2] == "O":
        return -11

    # checking verticals
    if board[0][0] == "O" and board[1][0] == "O" and board[2][0] == "O":
        return -11
    if board[0][1] == "O" and board[1][1] == "O" and board[2][1] == "O":
        return -11
    if board[0][2] == "O" and board[1][2] == "O" and board[2][2] == "O":
        return -11

    # if none of them win
    return 0


print("Welcome to Tic Tac Toe!")
print(
    "This is a 3x3 board. Enter the coordinates of the square you want to place your X or O in."
)
print("The first player to get three in a row wins!")
print("The board is numbered like this:")
print("00 01 02")
print("10 11 12")
print("20 21 22")
print("Have fun!")
print(" ")
print(" ")
print(" ")
board = [["_", "_", "_"], ["_", "_", "_"], ["_", "_", "_"]]
turn = 0
broke = False
while True:
    if turn == 0:
        n = input("Your move:")
        while True:
            if n != "quit":
                if board[int(n[0])][int(n[1])] != "_":
                    print("That space is already taken!")
                    n = input("Your move:")
                else:
                    board[int(n[0])][int(n[1])] = "o"
                    break
            else:
                broke = True
                break
    elif turn == 1:
        move = best_move(board)
        board[int(move[0])][int(move[1])] = "x"
    if broke:
        break
    turn = 1 - turn
    print(" _ _ _")
    for i in range(3):
        print("|", end="")
        for j in range(3):
            print(board[i][j], end="|")
        print(" ")
    resp = check(board, turn)
    if resp == None:
        continue
    elif resp == "computer":
        print("You lose!")
        break
    elif resp == "player":
        print("You win!")
        break
    else:
        print("Draw")
        break
