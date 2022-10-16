from math import factorial
def solution(n):
    answer = 0
    a,b = divmod(n,2)
    while a != -1:
        n = a+b
        answer += factorial(n)// (factorial(b) * factorial(n-b))
        a -= 1
        b += 2
    return answer%1234567