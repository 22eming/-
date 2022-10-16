import re
def solution(files):
    answer = []
    res = []; res_new = [[] for i in range(len(files))]
    for i in files:
        res.extend(re.compile('([\D]+)([0-9]+)(\D+.+)?').findall(i))
    for idx,i in enumerate(res):
        for j in range(len(i)-1):
            if j == 0:
                res_new[idx].append(i[j].lower())
            else:
                res_new[idx].append(int(i[j]))
                res_new[idx].append(idx)
    res_new.sort(key= lambda x: (x[0],x[1],x[2]))
    for i in res_new:
        answer.append(''.join(res[i[2]]))

    return answer