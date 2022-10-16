def solution(s):
    answer, cnt = [], []
    for idx, n in enumerate(s):
        if n == " ": cnt.append(idx)
    a = s.split()
    for n in a:
        answer += n.capitalize()
    for n in cnt:
        answer.insert(n," ")
    return ''.join(answer)