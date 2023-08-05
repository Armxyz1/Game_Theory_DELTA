#Import Modules
from tkinter import *
from tkinter.font import *
from tkinter import messagebox

#Game Initialization
def Play(board):
    game=Tk()
    game.title("Tic Tac Toe")
    '''#Heading (Disabled)
    head=Button(game, text="Welcome to Tic Tac Toe", 
        activebackground="yellow", activeforeground="light salmon",
        disabledforeground="yellow", 
        bg="light salmon", fg="yellow", width=300, bd=5, 
        font=("Helvetica",16))
    head.config(state=DISABLED)
    head.grid(row=0,column=0)'''
    #Creating Game Board
    for i in range(3):
        for j in range(3):
            board[i][j]=Button(game, text=var0,
                activebackground="red", fg="red", 
                activeforeground='yellow', bg="yellow", 
                disabledforeground="light salmon",
                font=("Helvetica",30), width=5, height=2,
                command=lambda r=i,c=j: Player(r,c))
            board[i][j].grid(row=i,column=j)
    '''#Leave the Game
    foot=Button(game, text="Exit the Game", command=exit, 
        activebackground="yellow", activeforeground="light salmon",
        disabledforeground="yellow", 
        bg="light salmon", fg="yellow", width=300, bd=5, 
        font=("Helvetica",16))
    foot.grid(row=4,column=0)'''
    game.mainloop()
    Computer(board)

#Player's Move
def Player(row,col):
    global turn
    if board[row][col]["text"]==var0 and not turn:
        board[row][col]['text']=var1
        board[row][col].config(state=DISABLED)
        if Evaluate(board)!=0 or not MoveLeft(board):
            End(board)
        turn=1-turn
        Computer(board)

#Computer's Move
def Computer(board):
    global turn
    if turn:
        move=BestMove(board)
        board[move[0]][move[1]]['text']=var2
        board[move[0]][move[1]].config(state=DISABLED)
        if Evaluate(board)!=0 or not MoveLeft(board):
            End(board)
        turn=1-turn

#Result Declaration        
def End(board):
    res=Evaluate(board)
    #Player Wins
    if res==-10:
        box=messagebox.showinfo("Win","You Win! Computer Lose!")
    #Computer Wins
    elif res==10:
        box=messagebox.showinfo("Lose","You Lose! Computer Win!")
    #Game Draw
    else:
        box=messagebox.showinfo("Draw","It is a Draw!")
    exit()

#Function to Find the Best Move
def BestMove(board):
    #Pseudo Code for the Best Move
    '''best move = None
    for each possible move on the board:
        if current move is better than best move:
            best move = current move
    return best move'''
    #Temporary Bad Algorithm
    '''for i in range(3):
        for j in range(3):
            if board[i][j]=="_":
                move=i,j'''
    #Added a Working Code to Solve
    best=-1000
    move=None
    for i in range(3):
        for j in range(3):
            if board[i][j]["text"]==var0:
                board[i][j]["text"]=var2
                val=MiniMax(board)
                board[i][j]["text"]=var0
                if val>best:                
                    move=i,j
                    best=val
    #Return 2 Digits each from 0 to 2
    return move

#Check if any Move is Left
def MoveLeft(board):
    for i in range(3):
        for j in range(3):
            if board[i][j]["text"]==var0:
                #Return TRUE if Game is Ongoing
                return True
    #Otherwise Return FALSE
    return False

#Added a Working Code for the MiniMax Algorithm
def MiniMax(board,depth=0,turn=0):
    '''if board evaluates win, loss or draw:
        return evaluated value of board removing depth'''
    res=Evaluate(board)
    if res==10:
        return res-depth
    elif res==-10:
        return res+depth
    if not MoveLeft(board):
        return 0
    #Pseudo Code for the MiniMax Algorithm
    #Break Further Check once Depth = Difficulty
    '''if minimizer's turn (turn==1):
        best = -Infty
        for each possible move on the board:
            value = minimax(board,depth+1,0)
            best = max(best,value)
    else maximizer's turn (turn==0):
        best = +Infty
        for each possible move on the board:
            value = minimax(board,depth+1,1)
            best = min(best,value)
        return bestVal'''
    #Computer's Turn : Maximizer
    if turn:
        best=-1000
        if depth==difficulty:
            return best
        for i in range(3):
            for j in range(3):
                if board[i][j]["text"]==var0:
                    board[i][j]["text"]=var2
                    val=MiniMax(board,depth+1)
                    best=max(best,val)
                    board[i][j]["text"]=var0
    #Player's Turn : Minimizer
    else:
        best=1000
        if depth==difficulty:
            return best
        for i in range(3):
            for j in range(3):
                if board[i][j]["text"]==var0:
                    board[i][j]["text"]=var1
                    val=MiniMax(board,depth+1,1)
                    best=min(best,val)
                    board[i][j]["text"]=var0
    return best

#Added a Working Code for the Evaluation Function
def Evaluate(board):
    #Computer : Maximizer : Var2 : Return +10
    #Player : Minimizer : Var1 : Return -10
    #Checking the Rows
    for row in range(3):
        if board[row][0]["text"]!=var0 and board[row][0]["text"]==board[row][1]["text"] and board[row][1]["text"]==board[row][2]["text"]:        
            if board[row][0]["text"]==var2:
                return 10
            return -10
    #Checking the Columns
    for col in range(3):
        if board[0][col]["text"]!=var0 and board[0][col]["text"]==board[1][col]["text"] and board[1][col]["text"]==board[2][col]["text"]:
            if board[0][col]["text"]==var2:
                return 10
            return -10
    #Checking the Diagonal 1
    if board[1][1]["text"]!=var0 and board[0][0]["text"]==board[1][1]["text"] and board[1][1]["text"]==board[2][2]["text"]:
        if board[1][1]["text"]==var2:
            return 10
        return -10
    #Checking the Diagonal 2
    if board[1][1]["text"]!=var0 and board[0][2]["text"]==board[1][1]["text"] and board[1][1]["text"]==board[2][0]["text"]:
        if board[1][1]["text"]==var2:
            return 10
        return -10
    #Incase of Draw or Ongoing Game
    return 0

#Play using X or O
#Using 'X' Token
def xo():
    global var1,var2
    var1,var2="X","O"
    menu.destroy()
    Play(board)
#Using 'O' Token
def ox():
    global var1,var2
    var1,var2="O","X"
    menu.destroy()
    Play(board)

#Play as First or Second Chance
#Play the First Move
def first():
    global turn
    turn=0
    B0["text"]="Will You Play using the Token"
    B1["text"]="' X '"
    B1["command"]=xo
    B2["text"]="' O '"
    B2["command"]=ox
#Play the Second Move
def second():
    global turn
    turn=1
    B0["text"]="Will You Play using the Token"
    B1["text"]="' X '"
    B1["command"]=xo
    B2["text"]="' O '"
    B2["command"]=ox

#Difficulty Level
#Easy Level set upto Depth 4
def easy():
    global difficulty
    difficulty=4
    B0["text"]="Will You Play the Move"
    B1["text"]="First"
    B1["command"]=first
    B2["text"]="Second"
    B2["command"]=second
#Hard Level set upto Depth 7
def hard():
    global difficulty
    difficulty=7
    B0["text"]="Will You Play the Move"
    B1["text"]="First"
    B1["command"]=first
    B2["text"]="Second"
    B2["command"]=second

#Starting Menu
menu=Tk()
menu.geometry("300x290")
menu.title("Tic Tac Toe")

#Heading (Disabled)
head=Button(menu, text="Welcome to Tic Tac Toe", 
    activebackground="yellow", activeforeground="light salmon",
    disabledforeground="yellow", 
    bg="light salmon", fg="yellow", width=300, bd=5, 
    font=("Helvetica",16))
head.config(state=DISABLED)

#Menu Question (Disabled)
B0=Button(menu, text="Choose the Difficulty Level", 
    activebackground="yellow", activeforeground="red",
    disabledforeground="yellow", 
    bg="red", fg="yellow", width=300, bd=5, 
    font=("Helvetica",16,"bold"))
B0.config(state=DISABLED)

#Option 1 (Enabled)
B1=Button(menu, text="Easy", command=easy, 
    activebackground="yellow", activeforeground="red",
    disabledforeground="yellow", 
    bg="red", fg="yellow", width=300, bd=5, 
    font=("Helvetica",25,"bold"))
#Option 2 (Enabled)
B2=Button(menu, text="Hard", command=hard, 
    activebackground="yellow", activeforeground="red",
    disabledforeground="yellow", 
    bg="red", fg="yellow", width=300, bd=5, 
    font=("Helvetica",25,"bold"))

#Leave the Game
foot=Button(menu, text="Exit the Game", command=exit, 
    activebackground="yellow", activeforeground="light salmon",
    disabledforeground="yellow", 
    bg="light salmon", fg="yellow", width=300, bd=5, 
    font=("Helvetica",16))

#GUI Initialization
head.pack()
B0.pack()
B1.pack()
B2.pack()
foot.pack()
var0=" "
board=[[var0,var0,var0] for _ in range(3)]
menu.mainloop()
