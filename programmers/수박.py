from itertools import cycle
res = cycle(["수","박"])
def solution(n):
    answer = ""
    for idx in range(n):
        answer = answer + next(res)
    return answer
