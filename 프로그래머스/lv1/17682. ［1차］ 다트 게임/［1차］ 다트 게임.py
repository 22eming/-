import re
def solution(dartResult):
    Bouns = {'S': 1,'D' : 2,'T' : 3}
    option = {'' : 1, '*': 2, '#': -1}

    p = re.compile('(\d+)([SDT])([*#]?)')
    dart = p.findall(dartResult)
    
    for n in range(len(dart)):
        if dart[n][2] == "*" and n > 0:
            dart[n-1] *= 2
        dart[n] = int(dart[n][0]) ** Bouns[dart[n][1]] * option[dart[n][2]]
    return sum(dart)