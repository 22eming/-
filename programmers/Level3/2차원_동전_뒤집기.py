from itertools import combinations
# 행 뒤집는 함수
def filp_coin(new_board, y_loc):
    for y in y_loc:
        if y == 0:
            print(' 행 idx :{}\n 행 값:{}'.format(y, new_board[y]))
            new_board[y] = [-i for i in new_board[y]]
            print(' 바뀐 행 값 :{}'.format(new_board[y]))
            print('-'*40)
        else:
            new_board[y] = [-i for i in new_board[y]]
            
    return check_board(new_board)

# 열 1자로 같은지 확인
def check_board(new_board):
    for x in range(len(new_board)):
        if abs(sum([new_board[y][x] for y in range(len(new_board))])) != len(new_board):
            return False
    return True

def solution(beginning, target):
    answer = 0
    n = len(beginning)
    board = []
    # beginnig 과 target 요소 비교 / 같으면 1 다르면 -1
    for y in range(n):
        temp = []
        for x in range(n):
            if beginning[y][x] == target[y][x]:
                temp.append(1)
            else:
                temp.append(-1)
        board.append(temp)
    
    # 행 바꿔보고 열이 1자로 같으면 true
    for i in range(n):
        for com in combinations(range(n), i):
            if filp_coin(board, com):
                return i


beginning = [[0, 1, 0, 0, 0], [1, 0, 1, 0, 1], [0, 1, 1, 1, 0], [1, 0, 1, 1, 0], [0, 1, 0, 1, 0]]
target = [[0, 0, 0, 1, 1], [0, 0, 0, 0, 1], [0, 0, 1, 0, 1], [0, 0, 0, 1, 0], [0, 0, 0, 0, 1]]
print(solution(beginning, target))