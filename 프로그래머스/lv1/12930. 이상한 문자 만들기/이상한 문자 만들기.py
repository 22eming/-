def solution(s):
    s = s.split(" ")
    answer = ''
    for n in s:
        for idx, i in enumerate(n):
            if idx % 2 == 0:
                answer += i.upper()
            else:
                answer += i.lower()
        answer += " "
    return answer[:-1]