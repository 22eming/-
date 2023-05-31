from math import sqrt


def solution(k, d):
    answer = 0
    d_double = d**2
    for y in range(0, d + 1, k):
        x = sqrt(d_double - y**2)
        answer += x // k + 1
    return int(answer)