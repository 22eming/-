from math import sqrt
def solution(board):
    a, answer = [0]*len(board[0]), 0
    for b in board:
        a = list((x+y)*y for x,y in zip(a,b))
        if max(a) >= sqrt(answer):
            re = list(set(a))
            for i in re:
                cnt = 0
                for n in a:
                    if n >= i:
                        cnt += 1
                        if cnt >= i:
                            answer = max(answer, i**2)
                    else: cnt = 0

    return answer