def solution(board, moves):
    len_bo, answer, res = len(board), [], 0

    for i in moves:
        n = 0
        while n != len_bo:
            if board[n][i-1] != 0:
                answer.append(board[n][i-1])
                board[n][i-1] = 0
                break
            else: n += 1
        
        while len(answer) > 1 and answer[-1] == answer[-2]:
            del answer[-2:] ; res += 2
    
    return res