# 대각선 전 사각형 경로 + 대각선 이후 사각형 경로
from math import factorial


def fac(x, y):
    return factorial(x+y) / (factorial(x)*factorial(y))


def solution(width, height, diagonals):
    answer = 0
    for x, y in diagonals:
        answer += fac(x-1, y) * fac(width-x, height-y+1)
        answer += fac(x, y-1) * fac(width-x+1, height-y)
    return answer % 10000019


print(solution(51,	37,	[[17, 19]]))
print(fac(16, 18) * fac(35, 18)*2)
