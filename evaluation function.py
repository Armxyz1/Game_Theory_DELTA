def evaluate(board):
    #TODO: Add evaluation function
    """
    if maximiser has won:
        return +10
    if minimiser has won:
        return -10
    return 0
    """
    
board = [
	[ 'o', 'o', 'x' ],
	[ 'o', 'x', 'x' ],
	[ '_', '_', '_' ]
]
print(evaluate(board))