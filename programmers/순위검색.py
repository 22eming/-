from bisect import bisect_left, insort_left
def solution(info, query):
    a = {}
    answer = []
    for n in info:
        q = n.split(); d = int(q.pop()); s = ' '.join(q)
        if a.get(s) == None:
            a[s] = [d]
        else:
            insort_left(a[s], d)

    for n in query:
        p = n.replace("-","").replace("and","").split()
        b_num = int(p.pop())
        cnt = 0
        for i in a.keys():
            if all([j in i for j in p]):
                cnt += len(a[i]) - bisect_left(a[i], b_num)
        answer.append(cnt)
    return answer


print(solution(	["java backend junior pizza 150", "python frontend senior chicken 210", "python frontend senior chicken 150", "cpp backend senior pizza 260", "java backend junior chicken 80", "python backend senior chicken 50"], ["java and backend and junior and pizza 100", "python and frontend and senior and chicken 200", "cpp and - and senior and pizza 250", "- and backend and senior and - 150", "- and - and - and chicken 100", "- and - and - and - 150"]))
