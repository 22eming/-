dartResult = "1D#2S*3S"
import re
def solution(dartResult):
    Bouns = {'S': 1,'D' : 2,'T' : 3}
    option = {'' : 1, '*': 2, '#': -1}

    p = re.compile('(\d+)([SDT])([*#]?)')
    dart = p.findall(dartResult)
    print(dart)
    for n in range(len(dart)):
        if dart[n][2] == "*" and n > 0:
            dart[n-1] *= 2
        dart[n] = int(dart[n][0]) ** Bouns[dart[n][1]] * option[dart[n][2]]
    return sum(dart)

print(solution(dartResult))


# 같은 2개 문자 지우기
# t = re.sub(r'(.)\1',"", s)