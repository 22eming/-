from collections import defaultdict
def solution(weights):
    siso = defaultdict(int)
    answer = 0
    for w in weights:
        answer += siso[w*0.5] + siso[w] + siso[w*1.5] + siso[w*2/3]\
                + siso[w*2] + siso[w*3/4] + siso[w*4/3]
        siso[w] += 1
    return answer    