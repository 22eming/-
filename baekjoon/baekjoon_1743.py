from collections import deque


def bfs(x, y):
    cnt = 0
    d1 = [-1, 0, 1, 0]
    d2 = [0, 1, 0, -1]
    que = deque([[x, y]])
    while que:
        x, y = que.popleft()
        if not visited[y][x]:
            visited[y][x] = True
            if board[y][x]:
                cnt += 1
                for dy, dx in zip(d1, d2):
                    xx, yy = x+dx, y+dy
                    if 0 <= xx < M and 0 <= yy < N:
                        que.append([xx, yy])

    return cnt


N, M, K = map(int, input().split())  # 세로 가로 개수

board = [[False]*M for _ in range(N)]
visited = [[False]*M for _ in range(N)]
answer = 0
for _ in range(K):
    r, c = map(int, input().split())
    board[r-1][c-1] = True

for y in range(N):
    for x in range(M):
        answer = max(answer, bfs(x, y))

print(answer)
