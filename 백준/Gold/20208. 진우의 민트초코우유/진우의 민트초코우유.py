from itertools import permutations

N, M, H = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
mints = []
answer = 0

for y in range(N):
    for x in range(N):
        if board[y][x] == 2:
            mints.append((y, x))
        elif board[y][x] == 1:
            home = (y, x)


def dfs(ny, nx, h, cnt):
    global answer
    for y, x in mints:
        if board[y][x] == 2:
            dist = abs(ny - y) + abs(nx - x)
            if dist <= h:
                board[y][x] = 0
                dfs(y, x, h - dist + H, cnt + 1)
                board[y][x] = 2

    if abs(ny - home[0]) + abs(nx - home[1]) <= h:
        answer = max(answer, cnt)


dfs(home[0], home[1], M, 0)
print(answer)