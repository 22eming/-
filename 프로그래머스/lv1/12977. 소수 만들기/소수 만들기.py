from itertools import combinations
def check(num):
    for i in range(2,num):
        if not num % i:
            return False
    return True

def solution(a):
    answer = 0
    for i in range(0, len(a)-2):
        for j in range(i+1, len(a)-1):
            for k in range(j+1, len(a)):
                if check(a[i] + a[j] + a[k]):
                        answer += 1
    return answer