import math
s = "abcde"
b = "qwer"
# n = math.floor(len(s)/2)
# print(n)
def solution(s):
    n = math.floor(len(s)/2)
    if len(s)%2 == 1:
        answer = s[n]
    else:
        answer = s[n-1:n+1] 
    return answer

print(solution(b))