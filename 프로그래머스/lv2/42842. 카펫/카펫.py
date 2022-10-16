import math
def solution(brown, yellow):
    total = brown + yellow
    res = []
    for i in range(3,int(math.sqrt(total)+1)):
        if (total / i) % 1 == 0:
            if (2 * i) + (2 * (total // i)) - 4 == brown:
                return [total // i, i]