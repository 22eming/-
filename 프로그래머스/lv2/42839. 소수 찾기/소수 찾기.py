from math import sqrt
from itertools import permutations
def prime(x):
    if x == 2: return True
    if (x == 0) or (x == 1) or (x % 2) == 0:
        return False
    for i in range(3, int(sqrt(x))+1, 2):
        if x % i == 0:
            return False
    return True

def solution(number):
    answer = 0
    ex = []
    for i in range(1, len(number)+1):
        ans = list(permutations(number,i))
        for j in range(len(ans)):
            ex.append( int(''.join(ans[j])) )

    for i in set(ex):
        if prime(i):
            answer += 1

    return answer