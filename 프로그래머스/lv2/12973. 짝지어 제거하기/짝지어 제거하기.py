def solution(s):
    a = []
    for n in s:
        a.append(n)
        if len(a) >= 2 and a[-1] == a[-2]:
            del a[-2:]
            
    if a == []: return 1
    else: return 0