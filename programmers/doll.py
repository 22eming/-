board = [[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]]	
moves = [1,5,3,5,1,2,1,4]

def solution(board, moves):
    answer = 0
    res = []
    for n in moves:
        for x in range(len(board)):
            if board[x][n-1] == 0:
                continue
            else:
                res.append(board[x][n-1])
                board[x][n-1] = 0
                break
        if len(res) > 1:
            if res[-1:] == res[-2:-1]:
                del res[-2:]
                answer +=2
    return answer

print(moves[-1:])