def solution(n):
    answer = ''; S = n
    while S != 0:
        S,R = divmod(S,3)
        if R == 0:
            S -= 1; R = 4
        answer = str(R) + answer
    return answer