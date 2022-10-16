from collections import defaultdict


def solution(id_list, report, k):
    answer = [0]*len(id_list)
    same_report = set()
    ban_dic = defaultdict(list)
    for i in report:
        user, ban = i.split(" ")
        if i not in same_report:
            same_report.add(i)
            if ban in ban_dic:
                ban_dic[ban][0] += 1
            else:
                ban_dic[ban].append(1)
            ban_dic[ban].append(user)

    for i in ban_dic.values():
        if i[0] >= k:
            for j in i[1:]:
                answer[id_list.index(j)] += 1
    return answer