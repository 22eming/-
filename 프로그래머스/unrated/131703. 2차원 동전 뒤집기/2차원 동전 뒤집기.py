def solution(beginning, target):
    n_y, n_x = len(beginning), len(beginning[0])
    board = [[beginning[y][x] ^ target[y][x]
              for x in range(len(beginning[y]))] for y in range(len(beginning))]

    cnt = 0
    for y in range(1, n_y):
        if board[y] != board[0]:
            cnt += 1
            if list(map(lambda x: x ^ 1, board[y])) != board[0]:
                return -1

    result = min(cnt+sum(board[0]), (n_y-cnt) + (n_x-sum(board[0])))
    return result