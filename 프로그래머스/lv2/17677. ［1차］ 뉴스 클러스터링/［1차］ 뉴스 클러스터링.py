from re import sub
def su(s):
    a = []
    for n in range(len(s)-1):
        i = sub('[-=+,#/\?:^$.@*\"※~&%ㆍ!』_\\‘|\(\)\[\]\<\>`\'… 0-9]', '', s[n]+s[n+1]).lower()
        if len(i) == 2:
            a.append(i)
    return a

def solution(str1, str2):
    answer = 0
    st1 = su(str1) ;  st2 = su(str2)
    p = set(st1) & set(st2)
    q = set(st1) | set(st2)
    
    if len(q) == 0: return 65536
    
    p_sum = sum([min(st1.count(pp), st2.count(pp)) for pp in p])
    q_sum = sum([max(st1.count(qq), st2.count(qq)) for qq in q])
    
    return int((p_sum/q_sum)*65536)