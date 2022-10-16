def div(w):
    p = 0
    for i in range(len(w)):
        if w[i] == "(":
            p += 1
        else:
            p -= 1
        if p == 0:
            return w[:i+1], w[i+1:]

def is_bal(w):
    p = 0
    for i in w:
        if i == "(":
            p += 1
        else:
            p -= 1
        if p < 0:
            return False
    return True

def solution(w):
    if w == '': return ''

    u, v = div(w)
    if is_bal(u):
        return u + solution(v)
    else:
        answer = "(" + solution(v) + ")" 
        for i in u[1:-1]:
            if i == "(":
                answer += ")"
            else:
                answer += "("
    return answer