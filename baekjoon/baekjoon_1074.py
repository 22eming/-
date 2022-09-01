N, r, c = map(int, input().split())

def quadrant(n, y, x):
    half_n = 2**(n-1)
    answer = 0
    answer += 1 if x >= half_n else 0
    answer += 2 if y >= half_n else 0
    return answer

result = 0
while N != 0:
    quad = quadrant(N, r, c)
    result += quad * (2**(N-1))**2
    r = r - 2**(N-1) if quad >= 2 else r
    c = c - 2**(N-1) if quad % 2 else c
    N -= 1
    
print(result)
    