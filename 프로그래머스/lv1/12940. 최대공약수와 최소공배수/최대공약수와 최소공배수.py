from math import gcd
def gcd(n, m):     
    return m if n % m == 0 else gcd(m, n % m) 
def solution(n, m):
    g = gcd(n,m)
    return [g, n*(m//g)]