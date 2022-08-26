import itertools
import collections
def solution(orders, course):
    res, answer = [], []
    for i in range(len(orders)):
        orders[i] = sorted(orders[i])

    for j in course:
        ans = []
        for n in range(len(orders)):
            res = list(itertools.combinations((orders[n]),j))
            for i in range(len(res)):
                ans.append(''.join(res[i]))
        a = collections.Counter(ans).most_common()
        i = 1

        if len(a) == 0 or a[0][1] == 1:
            pass
        elif len(a) == 1: answer.append[0][0]
        else:
            while a[i-1][1] == a[i][1]:
                i += 1
                if len(a) == i: break
            for c in range(i):
                answer.append(a[c][0])

    return sorted(answer)

print(solution(["XYZ", "XWY", "WXA"],[2,3,4] ))
