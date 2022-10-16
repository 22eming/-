def solution(number):
    answer = 0
    n = len(number)
    for a in range(n-2):
        for b in range(a+1, n-1):
            for c in range(b+1, n):
                if number[a] + number[b] + number[c] == 0:
                    answer += 1
    return answer