def solution(s):
    s = list(s)
    p = []
    res_1, res_2 = 0,0
    for n in range(len(s)):
        a = s[:n+1]
        b = s[n:][::-1]
        answer = 0
        while a != [] and b != []:
            if a.pop() == b.pop(): answer += 1
            else: a = []
        res_1 = max(res_1, answer)

    for n in range(len(s)):
        a = s[:n+1]
        b = s[n+1:][::-1]
        answer = 0
        while a != [] and b != []:
            if a.pop() == b.pop(): answer += 1
            else: a = []
        res_2 = max(res_2, answer)

    if res_1 > res_2: return res_1*2 -1
    else: return res_2*2