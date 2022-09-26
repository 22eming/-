def max_board(y, x):
    answer = 1

    for yy in [y, y+1]:
        if yy >= N:
            continue
        temp = 1
        for xx in range(N-1):

            if board[yy][xx] == board[yy][xx+1]:
                temp += 1
            else:
                temp = 1
            answer = max(temp, answer)

    for xx in [x, x+1]:
        if xx >= N:
            continue
        temp = 1
        for yy in range(N-1):
            if board[yy][xx] == board[yy+1][xx]:
                temp += 1
            else:
                temp = 1
            answer = max(temp, answer)

    return answer


N = int(input())
board = [list(input()) for _ in range(N)]
result = 0
for y in range(N):
    for x in range(N):
        if x+1 < N:
            board[y][x], board[y][x+1] = board[y][x+1], board[y][x]
            result = max(result, max_board(y, x))
            board[y][x], board[y][x+1] = board[y][x+1], board[y][x]

        if y+1 < N:
            board[y][x], board[y+1][x] = board[y+1][x], board[y][x]
            result = max(result, max_board(y, x))
            board[y][x], board[y+1][x] = board[y+1][x], board[y][x]

print(result)
