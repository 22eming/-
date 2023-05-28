from collections import deque


def move_robot(y, x, d, board):
    dy, dx = (-1, 0, 1, 0), (0, 1, 0, -1)
    while True:
        y, x = y + dy[d], x + dx[d]
        if not (0 <= y < len(board) and 0 <= x < len(board[0])) or board[y][x] == "D":
            break
    return (y - dy[d], x - dx[d])


def solution(board):
    len_y, len_x = len(board), len(board[0])
    max_cnt = len_y * len_x
    visited = [[float("inf")] * len_x for _ in range(len_y)]
    for y in range(len_y):
        for x in range(len_x):
            if board[y][x] == "R":
                sy, sx = y, x
            elif board[y][x] == "G":
                ey, ex = y, x

    que = deque([[sy, sx, 0]])

    while que:
        ny, nx, cnt = que.popleft()
        if board[ny][nx] == "G":
            return cnt
        if visited[ny][nx] < cnt:
            continue
        else:
            visited[ny][nx] = cnt

        for i in range(4):
            yy, xx = move_robot(ny, nx, i, board)
            if not (yy, xx) == (ny, nx):
                que.append([yy, xx, cnt + 1])
    return -1
