n	= 5
arr1 =	[9, 20, 28, 18, 11]
arr2 =	[30, 1, 21, 17, 28]

# import numpy as np

# def solution(n, arr1, arr2):
#     answer = []
#     empty_arr = np.zeros((n,n))
#     for idx, a in enumerate(arr1):
#         empty_arr[idx] = list(format(a, 'b').zfill(n))
#     for idx, b in enumerate(arr2):
#         map_1 = list(map(int, format(b, 'b').zfill(n)))
#         map_2 = [x+y for x,y in zip(empty_arr[idx], map_1)]
#         for map_idx in range(n):
#             if map_2[map_idx] >= 1:
#                 answer.extend("#")
#             else:
#                 answer.extend(" ")
#     answer = [(''.join(answer[i:i + n])) for i in range(0, len(answer), n)]
#     return answer

# print(solution(n, arr1, arr2))

def solution(n, arr1, arr2):
    answer = []
    for i,j in zip(arr1,arr2):
        a12 = str(bin(i|j)[2:])
        a12=a12.rjust(n,'0')
        a12=a12.replace('1','#')
        a12=a12.replace('0',' ')
        answer.append(a12)
    return answer
