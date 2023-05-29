from collections import deque
from copy import deepcopy

T = int(input())
for i in range(T):
    board = [list(input().split()) for _ in range(3)]
    board = [[board[y][x] == "H" for x in range(3)] for y in range(3)]
    que = deque([[board, 0, [False] * 8]])
    while que:
        b, cnt, visited = que.popleft()
        sum_b = sum([sum(b[y]) for y in range(3)])
        if sum_b == 9 or sum_b == 0:
            print(cnt)
            break

        # 가로
        for y in range(3):
            if visited[y]:
                continue
            new_b = b.copy()
            new_visited = deepcopy(visited)
            new_visited[y] = True
            new_b[y] = [not new_b[y][i] for i in range(3)]
            que.append([new_b, cnt + 1, new_visited])

        # 세로
        for y in range(3):
            if visited[y + 3]:
                continue
            new_b = deepcopy(b)
            new_visited = deepcopy(visited)
            new_visited[3 + y] = True
            for x in range(3):
                new_b[x][y] = not new_b[x][y]
            que.append([new_b, cnt + 1, new_visited])

        # 좌측 대각
        if visited[6] == False:
            new_b = deepcopy(b)
            new_visited = deepcopy(visited)
            new_visited[6] = True
            for y in range(3):
                new_b[y][y] = not new_b[y][y]
            que.append([new_b, cnt + 1, new_visited])

        # 우측 대각
        if visited[7] == False:
            new_b = deepcopy(b)
            new_visited = deepcopy(visited)
            new_visited[7] = True
            for y in range(3):
                new_b[y][2 - y] = not new_b[y][2 - y]
            que.append([new_b, cnt + 1, new_visited])
    if sum_b != 9 and sum_b != 0:
        print(-1)
