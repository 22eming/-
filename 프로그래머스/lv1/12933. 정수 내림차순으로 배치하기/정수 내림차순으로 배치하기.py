def solution(n):
    answer = sorted(str(n))[::-1]
    return int(''.join(answer))