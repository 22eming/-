# time : 7m
def solution(n):
    answer = ''; S = n
    while S != 0:
        S,R = divmod(S,3)
        if R == 0:
            S -= 1; R = 4
        answer = str(R) + answer
    return answer

def solution(n):
    num = ['1','2','4']
    answer = ""

    while n > 0:
        n -= 1
        answer = num[n % 3] + answer
        n //= 3

print(solution(7))