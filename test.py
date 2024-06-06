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
    score=evaluate(board,turn)
    if score==10:
        return score
    if score==-10:
        return score
    if check(board,turn)=="draw":
        return 0
    if turn==1:
        bestVal=-1000
        for i in range(3):
            for j in range(3):
                if board[i][j]=="_":
                    board[i][j]="x"
                    value=minimax(board,depth+1,1-turn)
                    bestVal=max(bestVal,value)
                    board[i][j]="_"
        return bestVal
    else:
        bestVal=1000
        for i in range(3):
            for j in range(3):
                if board[i][j]=="_":
                    board[i][j]="o"
                    value=minimax(board,depth+1,1-turn)
                    bestVal=min(bestVal,value)
                    board[i][j]="_"
        return bestVal
def evaluate(board,turn):
    for row in range(3) :     
        if (board[row][0] == board[row][1] and board[row][1] == board[row][2]) :
            if board[row][0]!="_":        
                if turn==0:
                    return 10
                else:
                    return -10
        
    for col in range(3) :
       
        if (board[0][col] == board[1][col] and board[1][col] == board[2][col]) :
            if board[0][col]!="_":
                if turn==0:
                    return 10
                else:
                    return -10
        
    if (board[0][0] == board[1][1] and board[1][1] == board[2][2]) :
        if board[0][0]!="_":
            if turn==0:
                    return 10
            else:
                    return -10
    
    if (board[0][2] == board[1][1] and board[1][1] == board[2][0]) :
        if board[1][1]!="_":
            if turn==0:
                    return 10
            else:
                    return -10
    return 0
def best_move(board):
    bestMove=None
    bestVal=-1000
    for i in range(3):
        for j in range(3):
            if board[i][j]=="_":
                board[i][j]="x"
                value=minimax(board,0,0)
                print(value)
                board[i][j]="_"
                if value>bestVal:
                    bestMove=str(i)+str(j)
                    bestVal=value
    return bestMove
board=[
    ['_','x','x'],
    ['o','_','o'],
    ['_','o','_']
]
print(best_move(board))