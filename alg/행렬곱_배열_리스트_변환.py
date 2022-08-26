import numpy as np
def solution(arr1, arr2):
    return (np.array(arr1)@np.array(arr2)).tolist()


print(solution([[1, 4], [3, 2], [4, 1]],[[3, 3], [3, 3]]))