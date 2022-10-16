maxsize = 1000000
def solution(n, s, a, b, fares):
    answer = maxsize
    mat = [[maxsize]*(n+1) for _ in range(n+1)]

    for fare in fares:
        node1, node2, cnt = fare
        mat[node1][node2] = cnt
        mat[node2][node1] = cnt

    for k in range(1, n+1):
        mat[k][k] = 0
        for i in range(1, n+1):
            for j in range(1, n+1):
                x = mat[i][k] + mat[k][j]
                if mat[i][j] > x:
                    mat[i][j] = x

    return min([mat[mid][s] + mat[mid][a] + mat[mid][b] for mid in range(1, n+1)])