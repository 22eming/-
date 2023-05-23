R, C = map(int, input().split())
board = [list(input()) for _ in range(R)]
visited = set(board[0][0])
move = ((-1, 0), (0, 1), (1, 0), (0, -1))
answer = 0


def dfs(y, x, cnt):
    global answer
    is_visit = False
    for dy, dx in move:
        ny, nx = dy + y, dx + x
        if 0 <= ny < R and 0 <= nx < C and board[ny][nx] not in visited:
            is_visit = True
            visited.add(board[ny][nx])
            dfs(ny, nx, cnt + 1)
            visited.remove(board[ny][nx])
    if not is_visit:
        answer = max(answer, cnt)


dfs(0, 0, 1)
print(answer)
