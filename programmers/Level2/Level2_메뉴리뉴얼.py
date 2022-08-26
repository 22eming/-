from itertools import combinations
import collections

def solution(orders, course):

    manu = {}
    orders = [sorted(i) for i in orders]

    for i in course:
        manu[i] = []

    for i in course:
        for j in orders:
            manu[i].extend(list(combinations(j,i)))

    result = []        
    for i in course:
        a = collections.Counter(manu[i]).most_common()
        for j in range(len(a)):
            if a[0][1] == 1: break
            if a[j][1] == a[0][1]:
                result.append(''.join(a[j][0]))

    return sorted(result)

# import itertools
# import collections
# def solution(orders, course):
#     res, answer = [], []
#     for i in range(len(orders)):
#         orders[i] = sorted(orders[i])

#     for j in course:
#         ans = []
#         for n in range(len(orders)):
#             res = list(itertools.combinations((orders[n]),j))
#             for i in range(len(res)):
#                 ans.append(''.join(res[i]))
#         a = collections.Counter(ans).most_common()
#         i = 1

#         if len(a) == 0 or a[0][1] == 1:
#             pass
#         elif len(a) == 1: answer.append[0][0]
#         else:
#             while a[i-1][1] == a[i][1]:
#                 i += 1
#                 if len(a) == i: break
#             for c in range(i):
#                 answer.append(a[c][0])

#     return sorted(answer)

print(solution(["XYZ", "XWY", "WXA"],[2,3,4] ))




print(solution(["ABCDE", "AB", "CD", "ADE", "XYZ", "XYZ", "ACD"],	[2,3,5]))

