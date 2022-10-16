def solution(d, budget):
    a, answer = sorted(d), 0
    for idx, n in enumerate(a):
        answer += n
        if answer > budget: return idx
        elif answer == budget: return idx +1
    else:
        return len(d)