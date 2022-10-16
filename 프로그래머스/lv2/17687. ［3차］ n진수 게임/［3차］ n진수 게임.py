def trans(n,base):
    T = "0123456789ABCDEF"
    q, r = divmod(n, base)
    if q == 0:
        return T[r]
    else:
        return trans(q, base) + T[r]

def solution(n, t, m, p):
    answer = ''
    res = []
    for i in range(m*t):
        res.append(trans(i, n))
    res = list(''.join(res))
    for i in range(p, m*t+1, m):
        answer += res[i-1]
    return answer