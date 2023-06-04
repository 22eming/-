from math import gcd


def solution(arrayA, arrayB):
    answer = 0
    gca, gcb = 0, 0
    for i in range(len(arrayA)):
        gca = gcd(gca, arrayA[i])

    for i in range(len(arrayB)):
        gcb = gcd(gcb, arrayB[i])
    
    for j in range(len(arrayA)):
        if arrayA[j] % gcb == 0:
            gcb = 1
        if arrayB[j] % gca == 0:
            gca = 1
    if gca == 1 and gcb == 1:
        return 0
    return max(gca, gcb)