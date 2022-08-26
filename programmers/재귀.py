def solution(arr):
    answer = [0,0]
    N = len(arr)
    def res(x,y,n):
        init = arr[x][y]
        for i in range(x, x+n):
            for j in range(y, y+n):
                if arr[i][j] != init:
                    nn = n//2
                    res(x,y,nn)
                    res(x+nn,y,nn)
                    res(x,y+nn,nn)
                    res(x+nn,y+nn,nn)
                    return
        answer[init] += 1
    res(0,0,N)
    return answer

# import numpy as np

# def solution(arr):
#     def fn(a):
#         if np.all(a == 0): return np.array([1, 0])
#         if np.all(a == 1): return np.array([0, 1])
#         n = a.shape[0]//2
#         return fn(a[:n, :n]) + fn(a[n:, :n]) + fn(a[:n, n:]) + fn(a[n:, n:])
#     return fn(np.array(arr)).tolist()

print(solution([[1,1,0,0],[1,0,0,0],[1,0,0,1],[1,1,1,1]]))
