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

print(solution("103"))


def prime(x):
    if x == 0 or x == 1:
        return False
    for i in range(2, int(math.sqrt(x))+1):
        if x % i == 0:
            return False
    return True
    
def solution(numbers):
    answer = 0
    ex = []
    for i in range(1, len(numbers)+1):
        res = list(permutations(numbers, i))
        # print(res)
        for n in range(len(res)):
            ex.append("".join(res[n]))
    num = list(set(map(int, ex)))
    for n in range(len(num)):
        if prime(num[n]) == True:
            answer += 1
        else:
            pass
    
    return answer
