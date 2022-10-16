def sol(line_a, line_b):
    A, B, E = line_a
    C, D, F = line_b
    if A*D - B*C == 0:
        return 0.1, 0.1
    x = ((B*F) - (E*D)) / ((A*D) - (B*C))
    y = ((E*C) - (A*F)) / ((A*D) - (B*C))
    return x, y


def solution(line):
    answer = []
    for i in range(len(line)):
        for ii in range(i+1, len(line)):
            x, y = sol(line[i], line[ii])
            if (x.is_integer() and y.is_integer()):  # 값이 정수라면
                answer.append([int(x), int(y)])
    answer.sort()
    # x, y 좌표값
    x1, x2 = answer[0][0], answer[-1][0]
    x = x2-x1
    y1, y2 = min(a[1] for a in answer), max(a[1] for a in answer)
    y = y2-y1
    # 출력
    res = []
    for i in range(y, -1, -1):
        txt = ""
        for j in range(x+1):
            if([j+x1, i+y1] in answer):
                txt += "*"
            else:
                txt += "."
        res.append(txt)
    return res