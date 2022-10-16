D = ((-1, 0), (0, 1), (1, 0), (0, -1))


def turn(a_pos, b_pos, cnt, board):
    if cnt % 2:  # b턴
        y, x = b_pos
    else:  # a턴
        y, x = a_pos
    # 같은 자리 -> b움직임
    if board[y][x] == 0:
        return True, cnt

    new_board = [r[:] for r in board]
    new_board[y][x] = 0
    _win, _lose = [], []
    next_turn = False

    # 4방향 이동
    for dy, dx in D:
        cy, cx = y + dy, x + dx
        # 이동 가능 할 때
        if 0 <= cy < len(board) and 0 <= cx < len(board[0]) and board[cy][cx] == 1:
            next_turn = True
            if cnt % 2:
                iswin, result = turn(a_pos, [cy, cx], cnt+1, new_board)
            else:
                iswin, result = turn([cy, cx], b_pos, cnt+1, new_board)

            if iswin:
                _win.append(result)
            else:
                _lose.append(result)

    # 움직일 곳 유무
    if next_turn:
        # 한 번이라도 승리하면 승리 선택
        if _win:
            return (0, min(_win))
        else:
            return (1, max(_lose))
    # 없으면 패
    else:
        return(1, cnt)


def solution(board, aloc, bloc):
    result = turn(aloc, bloc, 0, board)
    return result[1]