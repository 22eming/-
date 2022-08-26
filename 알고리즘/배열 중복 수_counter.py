import numpy as np
def solution(arr1, arr2):
    arr3, a = [[] for n in range(len(arr2))], []
    for n in arr2:
        for idx, i in enumerate(n):
            arr3[idx].append(i)
    # for n in range(len(arr1)):
    a = list(zip(arr1,arr3))
    print(a)
    # for n in a:
    #     print(sum(np.array(n[0])*np.array(n[1])))

print(solution([[2, 3, 2], [4, 2, 4], [3, 1, 4]], [[5, 4, 3], [2, 4, 1], [3, 1, 1]]))