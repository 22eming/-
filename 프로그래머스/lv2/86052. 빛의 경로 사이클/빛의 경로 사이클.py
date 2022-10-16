def solution(grid):
    answer = []
    row = len(grid)
    col = len(grid[0])
    visited = [[[0, 0, 0, 0] for _ in range(col)] for _ in range(row)]
    way = [0, 1, 2, 3]  # down, right, up, left
    my = [1, 0, -1, 0]
    mx = [0, -1, 0, 1]
    for j in range(row):
        for i in range(col):
            for s in way:
                i_way, j_way, cnt = i, j, 0
                while visited[j_way][i_way][s] == 0:
                    cnt += 1
                    visited[j_way][i_way][s] = 1
                    # 방향 변경
                    if grid[j_way][i_way] == "L":
                        s = (s + 1) % 4
                    elif grid[j_way][i_way] == "R":
                        s = way[s - 1]
                    # 위치 변경
                    i_way += mx[s]
                    j_way += my[s]
                    # 위치 조정
                    i_way = col-1 if i_way < 0 else i_way % col
                    j_way = row-1 if j_way < 0 else j_way % row

                if cnt > 0 and [i_way, j_way] == [i, j]:
                    answer.append(cnt)
    return sorted(answer)