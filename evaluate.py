def evaluate(board):
    for i in range(3):
        if board[i][0]==board[i][1] and board[i][1]==board[i][2]:
            if board[i][0]=='x':
                return 10;
            elif board[i][0]=='o':
                return -10;
        if board[0][i]==board[1][i] and board[1][i]==board[2][i]:
            if board[0][i] == 'x':
                return 10;
            elif board[0][i] == 'o':
                return -10;
    if board[0][0]==board[1][1] and board[1][1]==board[2][2]:
        if board[0][0] == 'x':
            return 10;
        elif board[0][0] == 'o':
            return -10;
    else:
        return 0;

board = [
    ['o','o','x'],
    ['o','x','x'],
    ['_','_','_']
]

print(evaluate(board))