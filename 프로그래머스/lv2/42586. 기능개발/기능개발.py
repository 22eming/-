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
    answer.append(cnt)

    return answer