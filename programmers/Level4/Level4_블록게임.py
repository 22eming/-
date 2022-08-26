import numpy as np


def block(pos, board, n, umb_x, answer):
    y, x = pos
    if n == 0 or n in answer:
        return True
    if board[y+1, x] == n:
        if board[y+2, x] == n:  # y 3칸
            for i in [-1, 1]:
                if board[y+2, x+i] == n:
                    if x+i not in umb_x:
                        for j in (0, 1):
                            if not block([y+j, x+i], board, board[y+j, x+i], umb_x, answer):
                                return False
                        return True
        else:  # y 2칸
            for i in ((1, 2), (-1, -2)):
                if board[y+1, x+i[1]] == n:  # ㄴ
                    if x+i[0] not in umb_x and x+i[1] not in umb_x:
                        for j in i:
                            if not block([y, x+j], board, board[y, x+j], umb_x, answer):
                                return False
                        return True
            if board[y+1, x-1] == n and board[y+1, x+1] == n:  # ㅗ
                if x-1 not in umb_x and x+1 not in umb_x:
                    for j in (1, -1):
                        if not block([y, x+j], board, board[y, x+j], umb_x, answer):
                            return False
                    return True
    return False


def solution(board):
    answer = []  # 정답 block
    b_set = {0}  # 확인한 block
    umb_x = set()  # 막힌 x
    umb_b = set()  # 막은 블락
    board = np.pad(board, ((2, 2), (2, 2)), constant_values=0)
    for y in range(len(board)):
        for x in range(len(board[0])):
            n = board[y, x]
            if n not in b_set:
                b_set.add(n)
                if block([y, x], board, n, umb_x, answer):
                    answer.append(n)
                else:
                    if board[y, x+2] == n:  # ㄱ
                        umb_x.update({x, x+1, x+2})
                        umb_b.add(n)
                    elif board[y+1, x-1] == n:  # ㅓ
                        umb_x.update({x, x-1})
                        umb_b.add(n)
                    else:
                        umb_x.update({x, x+1})
                        umb_b.add(n)
    return answer

# y 0부터 내려오면서 불가능한 도형이면 x값 저장


print(solution([[0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 4, 0, 0, 0], [
      0, 0, 0, 0, 0, 4, 4, 0, 0, 0], [0, 0, 0, 0, 3, 0, 4, 0, 0, 0], [0, 0, 0, 2, 3, 0, 0, 0, 5, 5], [1, 2, 2, 2, 3, 3, 0, 0, 0, 5], [1, 1, 1, 0, 0, 0, 0, 0, 0, 5]]))

# 가능 1-3, 1-4, 2-2, 2-3, 3-1
