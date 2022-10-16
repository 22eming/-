from typing import DefaultDict


def solution(tickets):
    dic = DefaultDict(list)
    for s, a in tickets:
        dic[s].append(a)
    for s in dic.keys():
        dic[s].sort()

    stack = ['ICN']
    visit = []
    while stack:
        cur_p = stack[-1]
        if dic[cur_p] != []:
            stack.append(dic[cur_p].pop(0))
        else:
            visit.append(stack.pop())
    visit.reverse()
    return visit