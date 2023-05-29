from collections import deque

def flip(value):
    return not value

def check_board(board):
    sum_b = sum([sum(row) for row in board])
    if sum_b == 9 or sum_b == 0:
        return True
    return False

def solve():
    T = int(input())
    for _ in range(T):
        board = [list(input().split()) for _ in range(3)]
        board = [[board[y][x] == "H" for x in range(3)] for y in range(3)]
        que = deque([[board, 0, [False] * 8]])

        while que:
            b, cnt, visited = que.popleft()

            if check_board(b):
                print(cnt)
                break

            for y in range(3):
                if visited[y]:
                    continue

                new_b = [row[:] for row in b]
                new_visited = visited[:]
                new_visited[y] = True
                new_b[y] = [flip(value) for value in new_b[y]]
                que.append([new_b, cnt + 1, new_visited])

            for y in range(3):
                if visited[y + 3]:
                    continue

                new_b = [row[:] for row in b]
                new_visited = visited[:]
                new_visited[3 + y] = True
                for x in range(3):
                    new_b[x][y] = flip(new_b[x][y])
                que.append([new_b, cnt + 1, new_visited])

            if not visited[6]:
                new_b = [row[:] for row in b]
                new_visited = visited[:]
                new_visited[6] = True
                for y in range(3):
                    new_b[y][y] = flip(new_b[y][y])
                que.append([new_b, cnt + 1, new_visited])

            if not visited[7]:
                new_b = [row[:] for row in b]
                new_visited = visited[:]
                new_visited[7] = True
                for y in range(3):
                    new_b[y][2 - y] = flip(new_b[y][2 - y])
                que.append([new_b, cnt + 1, new_visited])

        else:
            print(-1)

solve()
