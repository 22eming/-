from math import gcd

def gcd(w, h):
    return h if w % h == 0 else gcd(h, w % h) 
         

def solution(w,h):
    total = w * h
    minus = w + h - gcd(w, h)
    return total - minus


print(gcd(8,12))
print(solution(8,12))

