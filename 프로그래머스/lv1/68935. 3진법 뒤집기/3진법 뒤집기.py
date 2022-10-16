def convert(n, base):
    T = "0123456789ABCDEF"
    q, r = divmod(n, base)
    if q == 0:
        return T[r]
    else:
        return convert(q, base) + T[r]

def solution(n):
    a = convert(n, 3)
    answer = 0
    for idx, i in enumerate(a):
        answer += int(i)*(3**idx)
    return answer