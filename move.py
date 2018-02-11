def evaluate(board):
    for i in range(3):
        if( board[i][0] == 'X' and board[i][1] == 'X'and board[i][2] == 'X'):
            return 10
        
        if( board[i][0] == 'O' and board[i][1] == 'O' and board[i][2] == 'O'):
            return -10
        
        if( board[0][i] == 'X' and board[1][i] == 'X' and board[2][i] == 'X'):
            return 10
        
        if( board[0][i] == 'O' and board[1][i] == 'O' and board[2][i] == 'O'):
            return -10
        
    if( board[0][0] == 'X' and board[1][1] == 'X' and board[2][2] == 'X'):
        return 10
    
    if( board[0][2] == 'X' and board[1][1] == 'X' and board[2][0] == 'X'):
        return 10
    
    if( board[0][0] == 'O' and board[1][1] == 'O' and board[2][2] == 'O'):
        return -10
    
    if( board[0][2] == 'O' and board[1][1] == 'O' and board[2][0] == 'O'):
        return -10
    return 0

def isLegalMove(row,col,board):
    if board[row][col] is ' ':
        return True
    else:
        return False

def isFinalState(board):
    for row in board:
        for squre in row:
            if squre is ' ':
                return False
    return True
def minmax(board,depth,player,score):
    finalScore = evaluate(board)
    if finalScore is not 0:
        return finalScore
    if isFinalState(board):
        if player == 'X':
            return depth * -1
        else:
            return depth
    if player=='X':
        max_score = -999
        for i in range(3):
            for j in range(3):
                if( isLegalMove( i , j , board ) ):
                    new_board = board
                    new_board[i][j] = 'X'
                    max_score = max(max_score,minmax(new_board, depth+1 , 'O', score))
                    new_board[i][j] = ' '
        return max_score - depth
    elif player == 'O':
        min_score = 999
        for i in range(3):
            for j in range(3):
                if (isLegalMove(i, j, board)):
                    new_board = board
                    new_board[i][j] = 'O'
                    min_score = min(min_score, minmax(new_board, depth + 1, 'X', score))
                    new_board[i][j]= ' '
        return min_score + depth

test = [[' ',' ',' '],[' ',' ',' '],[' ',' ',' ']]
#print(minmax(test,5,'O',0))
def bestMove(board,aiFirst):
    next_move = [-1,-1]
    if isFinalState(board) is True:
        return next_move
    p = 1
    v = 'X'
    y = 'O'
    if aiFirst is False:
        p = -1
        v = 'O'
        y = 'X'
    k = -999
    for i in range(3):
        for j in range(3):
            #print(board)
            if isLegalMove(i,j,board) is True:
                board[i][j] = v
                q = minmax(board,0,y,0) * p
                if q > k:
                    next_move[0] = i
                    next_move[1] = j
                    k = q
                board[i][j] = ' '
    return next_move

