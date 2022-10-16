from math import gcd
def solution(arr):
    c = arr[0]
    for n in arr[1:]:
        c =  c*n//gcd(c,n)
    return c