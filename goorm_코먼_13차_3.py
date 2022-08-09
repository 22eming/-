import numpy as np
N, M = map(int, input().split())
max_size = int(input())
MAP = np.array([list(map(int, input().split())) for _ in range(N)])

for y in range(N-2):
    for x in range(M-2):
        temp = sum(MAP[y:y+3, x:x+3])
        if temp > 0:
            max_sum = max(max_sum, temp)
