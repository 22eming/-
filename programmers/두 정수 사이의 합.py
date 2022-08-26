def solution(a, b):
    answer = []
    for n in range(abs(a - b)+1):
        answer.append(min(a,b)+n)
    return sum(answer)