def check(s):
    res = []
    dic = { "(" : [0,0], ")" : [0,1], "{" : [1,0], "}" : [1,1], "[" : [2,0], "]" : [2,1]}
    for i in s:
        res.append(i)
        while ( len(res) > 1 ):
            if ( dic[res[-2]][0] == dic[res[-1]][0] ):
                if ( dic[res[-2]][1] == 0 and dic[res[-1]][1] == 1):
                    del res[-2:]
            break
    return len(res) > 0

def solution(s):
    answer = 0
    s = list(s)
    for _ in range(len(s)):
        if check(s) == False:
            answer += 1
        s.insert(0, s.pop())
    return answer

print(solution("}]()[{"))