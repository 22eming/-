def solution(t, p):
    answer = 0
    cnt = len(p)
    for i in range(len(t)-cnt+1):
        if int(t[i:i+cnt]) <= int(p):
            answer += 1        
    return answer