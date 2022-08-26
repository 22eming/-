# Floyd-Warshall 이용
INF = float("inf")


def solution(n, edges):
    answer = 0
    board = [[INF]*n for _ in range(n)]

    for i in range(n):
        board[i][i] = 0

    for x, y in edges:
        board[x][y] = 1
        board[y][x] = 1

    for k in range(n):
        board[k][k] = 0
        for i in range(n):
            for j in range(n):
                board[i][j] = min(board[i][j], board[i][k] + board[k][j])

    for i in range(n):
        for j in range(n):
            for k in range(n):
                if board[i][j] and board[j][k] and board[i][k]:
                    if board[i][j] + board[j][k] == board[i][k]:
                        answer += 1
    return answer


print(solution(4,	[[2, 3], [0, 1], [1, 2]]))
