def solution(a, b, n):
    answer = 0
    blank, spare = n, 0
    while blank+spare >= a:
        blank += spare
        blank, spare = divmod(blank, a)
        blank *= b
        answer += blank
        
    return answer