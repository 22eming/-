import math
def solution(brown, yellow):
    res = []
    total = brown + yellow
    for i in range(3,int(math.sqrt(total)+1)):
        if (total / i) % 1 == 0:
            if (2 * i) + (2 * (total // i)) - 4 == brown:
                return [total // i, i]

print(solution(24	,24))

def solution(brown, yellow):
    answer = []
    n = math.sqrt(brown+yellow)
    for x in range(math.ceil(n), brown//2):
        y = ((brown - 2*x) // 2)+2
        if x*y == brown + yellow:
           return [x,y]