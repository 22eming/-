from bisect import insort_left, bisect_left
def solution(info, query):
    a = {}; answer = []
    for i in info:
        s = i.split()
        t = ''.join(s[:-1])
        if a.get(t) == None:
            a[t] = [int(s[-1])]
        else:
            a[t] += [int(s[-1])]
    for key, val in a.items():
        a[key] = sorted(val)

    for i in query:
        q = i.replace("and", "").replace("-","").split()
        p = int(q.pop())
        cnt = 0
        for j in a.keys():
            if all( [k in j for k in q] ):
                cnt += len(a[j]) - bisect_left(a[j], p)
        answer.append(cnt)
    return answer