def solution(genres, plays):
    a = {} ; num = {} ; sm = []
    x = 1 ; answer = []
    for i,j in zip(genres,plays):
        x -= 1
        if a.get(i) == None:
            a[i] = [j]
            num[i] = [[j,x]]
        else:
            a[i].append(j)
            num[i].append([j,x])

    for i in a:
        sm += [[i,sum(a[i])]]
    sm.sort(key= lambda x: x[1] ,reverse= True)

    for i in sm:
        c = sorted(num[i[0]])
        answer.append(-c.pop()[1])
        if len(c) > 0:
            answer.append(-c.pop()[1])

    return answer