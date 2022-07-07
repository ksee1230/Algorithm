def solution(board):
    answer = 0
    
    if len(board) < 2 or len(board[0]) < 2:
        temp = 0
        for i in range(len(board)):
            for j in range(len(board[i])):
                temp += board[i][j]
        if temp == 0:
            return 0
        return 1
    
    for i in range(1, len(board)):
        for j in range(1, len(board[i])):
            if board[i][j] == 1:
                board[i][j] = min(board[i-1][j], board[i][j-1], board[i-1][j-1]) + 1
            answer = max(answer, board[i][j])
                        
    return answer * answer