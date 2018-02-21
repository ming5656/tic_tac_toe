#Define ai move
#Using Minmax alogrithm
#X always max its value, O always minimum its value

#If X win ,return 10
#If O win, return -10
#end neither in victory nor defeat , return 0
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

#Decide the current squre is legal
def isLegalMove(row,col,board):
    if board[row][col] is ' ':
        return True
    else:
        return False

#Check the all squres is filled
def isFinalState(board):
    for row in board:
        for squre in row:
            if squre is ' ':
                return False
    return True

#Implement minmax algorithm
def minmax(board,depth,player,score):
    finalScore = evaluate(board)

    #finalscore is not 0 means that game decide the winner
    if finalScore is not 0:
        return finalScore
    """
    depth is a factor. The more shallow depth the better.
    So if the scores  are same,we choose the shallowest depth.
    Player is X , the score will be reduced by depth.
    Player is O, the score will be added by depth.
    """

    #If no one win
    if isFinalState(board):
        if player == 'X':
            return depth * -1
        else:
            return depth

    #Maximum the score
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
    # Minumum the score
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

#test = [[' ',' ',' '],[' ',' ',' '],[' ',' ',' ']]
#print(minmax(test,5,'O',0))

# Decide AI the best next move
def bestMove(board,aiFirst):
    next_move = [-1,-1]
    if isFinalState(board) is True:
        return next_move
    p = 1
    v = 'X'
    y = 'O'
    if aiFirst is False:
        p = -1 # To use decide the smallest value
        v = 'O'
        y = 'X'
    k = -999

    # Choose every possible squre to decide whice move the score is best
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

