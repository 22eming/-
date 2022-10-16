def solution(survey, choices):
    char_cnt = {'R':0, 'T':0, 'C':0, 'F':0, 'J':0, 'M':0, 'A':0, 'N':0}
    for surv, cho in zip(survey, choices):
        p, n = surv
        if cho > 4:
            char_cnt[p] += 4 - cho
        elif cho < 4:
            char_cnt[n] += cho -4
    
    result = ""
    for a, b in [['R','T'],['C','F'],['J','M'],['A','N']]:
        if char_cnt[a] >= char_cnt[b]:
            result += a
        else:
            result += b

    return result