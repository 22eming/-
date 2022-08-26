from bisect import bisect_left

def solution(info, query):
    info_dic = {}; answer = []
    for i in info:
        p = i.split(); p_num = int(p.pop()); p = ''.join(p)
        if info_dic.get(p) == None:
            info_dic[p] = [p_num]
        else:
            info_dic[p] += [p_num]

    for key, val in info_dic.items():
        info_dic[key] = sorted(val)
    
    for i in query:
        qruery_res = i.replace("and", "").replace("-", "").split()
        query_num = int(qruery_res.pop())
        cnt = 0
        for j in info_dic:
            if all( [k in j for k in qruery_res] ):
                cnt += len(info_dic[j]) - bisect_left(info_dic[j], query_num)
        answer.append(cnt)

    return answer


print(solution(["java backend junior pizza 150","python frontend senior chicken 210","python frontend senior chicken 150","cpp backend senior pizza 260","java backend junior chicken 80","python backend senior chicken 50"],	["java and backend and junior and pizza 100","python and frontend and senior and chicken 200","cpp and - and senior and pizza 250","- and backend and senior and - 150","- and - and - and chicken 100","- and - and - and - 150"]))
