# time 20m
from math import ceil
def solution(progresses, speeds):
    answer,res = [], []
    for i in range(len(progresses)):
        res.append(ceil((100-progresses[i])/speeds[i]))
    max_i, cnt = res[0], 1
    for i in range(1,len(res)):
        if max_i < res[i]:
            answer.append(cnt)
            cnt = 1
            max_i = res[i]
        else:
            cnt += 1
    return answer + [cnt]

# time 10m
import numpy as np
def solution(progresses, speeds):
    answer,pro = [], 0
    today = np.array(progresses)
    while pro != len(progresses):
        today = today + np.array(speeds)
        cnt = 0
        for i in today[pro:]:
            if i >= 100:
                cnt += 1
            else:
                break
        if cnt > 0:
            answer.append(cnt)
        pro += cnt
    
    return answer

# first
import math
def solution(progresses, speeds):
    answer,new ,n, j, h = [0], [], 0, 0, 0
    while n != len(speeds):
        a = math.ceil((100 - progresses[n])/speeds[n])
        new.append(a)
        n += 1

    for i in range(1, len(speeds)):
        if new[h] < new[i]:
            answer[j] += 1
            answer.append(0)
            j += 1
            h = i
        else:
            answer[j] += 1
    answer[-1] += 1
    return answer

print(solution([93, 30, 55], [1, 30, 5]))