N, M = map(int, input().split())
board = [ input() for _ in range(N) ]

chess_wb = ['WBWBWBWB','BWBWBWBW']*4
chess_bw = ['BWBWBWBW','WBWBWBWB']*4
answer_wb = 64
answer_bw = 64
for y in range(N-7):
    for x in range(M-7):
        temp_wb, temp_bw = 0, 0
        for i in range(8):
            for j in range(8):
                if board[y+i][x+j] != chess_wb[i][j]: temp_wb += 1
                if board[y+i][x+j] != chess_bw[i][j]: temp_bw += 1
        answer_wb = min(answer_wb, temp_wb)
        answer_bw = min(answer_bw, temp_bw)

print(min(answer_bw, answer_wb))