def solution(n, words):
    a = set()
    for idx, i in enumerate(words):
        b = len(a); a.add(i)
        if b == len(a):
            return [idx%n+1,idx//n+1]
        if idx > 0 and words[idx-1][-1] != words[idx][0]:
            return [idx%n+1,idx//n+1]
    else: return [0,0]