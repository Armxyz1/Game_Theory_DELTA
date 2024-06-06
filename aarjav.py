def best_move(board):
    best=-1000
    move=None
    for i in range(3):
        for j in range(3):
            if board[i][j]=="_":
                board[i][j]="x"
                val=minimax(board,0,0)
                print(val)
                board[i][j]="_"
                if val>best:                
                    move=(i,j)
                    best=val
    return move

    
def check(board,turn):
    for row in range(3) :     
        if (board[row][0] == board[row][1] and board[row][1] == board[row][2]) :
            if board[row][0]!="_":        
                if turn==1:
                    return "player"
                else:
                    return "computer"
    for col in range(3) :
        if (board[0][col] == board[1][col] and board[1][col] == board[2][col]) :
            if board[0][col]!="_":
                if turn==1:
                    return "player"
                else:
                    return "computer"
    if (board[0][0] == board[1][1] and board[1][1] == board[2][2]) :
        if board[0][0]!="_":
            if turn==1:
                    return "player"
            else:
                    return "computer"
    if (board[0][2] == board[1][1] and board[1][1] == board[2][0]) :
        if board[1][1]!="_":
            if turn==1:
                    return "player"
            else:
                    return "computer"
    for i in range(3):
        for j in range(3):
            if board[i][j]=="_":
                return None
    return "draw"
    
def minimax(board, depth, turn):
    #minimax(board, depth, turn==1) ??
    #TODO: Add minimax algorithm
    score=evaluate(board)
    if score==10 or score==-10:
        return score
    if check(board,turn)=="draw":
        return 0
    #Computer's Turn : Maximizer
    if turn:
        best=-1000
        for i in range(3):
            for j in range(3):
                if board[i][j]=="_":
                    board[i][j]="x"
                    val=minimax(board,depth+1,0)
                    best=max(best,val)
                    board[i][j]="_"
    #Player's Turn : Minimizer
    else:
        best=+1000
        for i in range(3):
            for j in range(3):
                if board[i][j]=="_":
                    board[i][j]="o"
                    val=minimax(board,depth+1,1)
                    best=min(best,val)
                    board[i][j]="_"
    return best
def evaluate(board):
    #TODO: Add Evaluation Function
    #Computer : Maximizer & Player : Minimizer
    #Checking the Rows
    for row in range(3):
        if board[row][0]==board[row][1] and board[row][1]==board[row][2]:
            if board[row][0]=="o":
                return -10
            elif board[row][0]=="x":
                return 10
    #Checking the Columns
    for col in range(3):
        if board[0][col]==board[1][col] and board[1][col]==board[2][col]:
            if board[0][col]=="o":
                return -10
            elif board[0][col]=="x":
                return 10
    #Checking the Diagonals
    if ( board[0][0]==board[1][1] and board[1][1]==board[2][2] ) or ( board[0][2]==board[1][1] and board[1][1]==board[2][0] ):
        if board[1][1]=="o":
            return -10
        elif board[1][1]=="x":
            return 10
    #Incase of Draw
    return 0
    
print("Welcome to Tic Tac Toe!")
print("This is a 3x3 board. Enter the coordinates of the square you want to place your X or O in.")
print("The first player to get three in a row wins!")
print("The board is numbered like this:")
print("00 01 02")
print("10 11 12")
print("20 21 22")
print("Have fun!")
print(" ")
print(" ")
print(" ")
board=[
    ["_","_","_"],
    ["_","_","_"],
    ["_","_","_"]
    ]
turn=0
broke=False
while True:
    if turn==0:
        n=input("Your move:")
        while True:
            if n!="quit":
                if board[int(n[0])][int(n[1])]!="_":
                    print("That space is already taken!")
                    n=input("Your move:")
                else:    
                    board[int(n[0])][int(n[1])]="o"
                    break
            else:
                broke=True
                break
    elif turn==1:
        move=best_move(board)
        board[int(move[0])][int(move[1])]="x"
    if broke:
        break
    turn=1-turn
    print(" _ _ _")
    for i in range(3):
        print("|",end="")
        for j in range(3):
            print(board[i][j],end="|")
        print(" ")
    resp=check(board,turn)
    if resp==None:
        continue
    elif resp=="computer":
        print("You lose!")
        break
    elif resp=="player":
        print("You win!")
        break
    else:
        print("Draw")
        break
