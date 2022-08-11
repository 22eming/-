from collections import deque

N, M = map(int, input().split())

MAP = [ list(map(int, input().split())) for i in range(N)]

board = [ [0]*M for _ in range(N) ]
board[0][0] = MAP[0][0]
# 윗층에서 내려옴, 좌측에서 옴, 우측에서 옴
    
for y in range(N):
    for x in range(M):
        if y == 0:
            board[y][x] = board[y][x-1] + MAP[y][x]
            continue
        
        board[y][x] = board[y-1][x] + MAP[y][x]
     
        for i in range(0, x):
            temp = board[y-1][i]
            for j in range(i, x+1):
                temp += MAP[y][j]
            board[y][x] = max(board[y][x], temp)
        
        for i in range(M-1, x, -1):
            temp = board[y-1][i]
            for j in range(i, x-1, -1):
                temp += MAP[y][j]
            board[y][x] = max(board[y][x], temp)

print(board[N-1][M-1])
    

            
    
    
