import numpy as np


def solution(board, skill):
    damage = np.zeros((len(board)+1, len(board[0])+1))
    for t, y1, x1, y2, x2, d in skill:
        d = d if t == 2 else -d
        damage[y1, x1] += d
        damage[y1, x2+1] -= d
        damage[y2+1, x1] -= d
        damage[y2+1, x2+1] += d

    damage = damage.cumsum(axis=1)
    damage = damage.cumsum(axis=0)
    answer = np.array(board) + damage[:len(board), :len(board[0])]

    return len(np.where(answer > 0)[0])


print(solution([[5, 5, 5, 5, 5], [5, 5, 5, 5, 5], [5, 5, 5, 5, 5], [5, 5, 5, 5, 5]],
               [[1, 0, 0, 3, 4, 4], [1, 2, 0, 2, 3, 2], [2, 1, 0, 3, 1, 2], [1, 0, 1, 3, 3, 1]]))


def non_np_solution(board, skill):
    def cumsum():
        for y in range(len(board)+1):
            for x in range(1, len(board[0])+1):
                damage[y][x] += damage[y][x-1]

        for x in range(len(board[0])+1):
            for y in range(1, len(board)+1):
                damage[y][x] += damage[y-1][x]

    damage = [[0]*(len(board[0])+1) for _ in range(len(board)+1)]
    for t, y1, x1, y2, x2, d in skill:
        d = d if t == 2 else -d
        damage[y1][x1] += d
        damage[y1][x2+1] -= d
        damage[y2+1][x1] -= d
        damage[y2+1][x2+1] += d

    cumsum()
    answer = [x+y for i in range(len(board))
              for x, y in zip(board[i], damage[i])]

    answer = sum([1 for i in answer if i > 0])
    return answer


print(non_np_solution([[5, 5, 5, 5, 5], [5, 5, 5, 5, 5], [5, 5, 5, 5, 5], [5, 5, 5, 5, 5]],
                      [[1, 0, 0, 3, 4, 4], [1, 2, 0, 2, 3, 2], [2, 1, 0, 3, 1, 2], [1, 0, 1, 3, 3, 1]]))
