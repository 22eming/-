def solution(triangle):
    answer = 0
    db = triangle[0]
    for i in range(1,len(triangle)):
        res = []
        for n, j in enumerate(triangle[i]):
            if n == 0:
                res.append(j+db[0])
            elif n == i:
                res.append(j+db[-1])
            else:
                res.append(max(db[n], db[n-1])+j)
        db = res
    return max(db)

print(solution([[7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]]))
