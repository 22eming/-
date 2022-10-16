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