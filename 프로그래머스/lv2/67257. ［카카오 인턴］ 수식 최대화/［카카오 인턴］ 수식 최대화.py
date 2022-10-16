from re import compile
def solution(s):
    answer = 0
    op = [["*","+","-"],["*","-","+"],["+","*","-"],["+","-","*"],["-","+","*"],["-","*","+"]]
    for i in op:
        oper = compile('[+*-]').findall(s)
        num = list(map(int, compile('\d+').findall(s)))
        for j in i:
            while oper != []:
                if j in oper:
                    p = oper.index(j)
                    oper.pop(p)
                    if j == "*":
                        num[p] = num[p] * num.pop(p+1)
                    elif j == "+":
                        num[p] = num[p] + num.pop(p+1)
                    else:
                        num[p] = num[p] - num.pop(p+1)
                else:
                    break
        answer = max(answer, abs(num[0]))

    return answer