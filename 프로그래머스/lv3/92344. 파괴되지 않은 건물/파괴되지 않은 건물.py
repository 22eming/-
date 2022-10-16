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