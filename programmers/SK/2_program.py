import numpy


def solution(n, clockwise):
    answer = [[0]*n for _ in range(n)]
    direct_t = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    direct_f = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    loc_t = ((0, 0), (n-1, 0), (n-1, n-1), (0, n-1))
    loc_f = ((0, 0), (0, n-1), (n-1, n-1), (n-1, 0))

    if clockwise:
        direct = direct_t
        loc = loc_t
    else:
        direct = direct_f
        loc = loc_f

    for idx, l in enumerate(loc):
        x, y = l
        d = 0 + idx
        cnt = n-1
        i = 1
        while cnt > 0:
            for _ in range(cnt):
                answer[y][x] = i
                x, y = x + direct[d][0], y + direct[d][1]
                i += 1
            x, y = x - direct[d][0], y - direct[d][1]
            d = (d+1) % 4
            x, y = x + direct[d][0], y + direct[d][1]
            cnt -= 2

    if n % 2 and n > 1:
        mid = n//2
        answer[mid][mid] = answer[mid][mid+1]+1
    elif n == 1:
        return [[1]]
    return numpy.array(answer)


print(solution(1, True))
