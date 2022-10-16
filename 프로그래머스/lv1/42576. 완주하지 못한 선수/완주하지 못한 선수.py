def solution(participant, completion):
    par, com = sorted(participant), sorted(completion)
    n = 0
    while n != len(com):
        if par[n] != com[n]:
            break
        n += 1
    answer = par[n]
    return answer