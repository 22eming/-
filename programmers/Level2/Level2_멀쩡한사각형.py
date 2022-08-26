from math import gcd
def solution(W, H):
    total = W * H
    minus = W + H - gcd(H, W%H) # 전부 곂치지 않을 때 - 곂칠때
    
    return total - minus

print(solution(8,12))
