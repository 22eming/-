a,b,c = map(int, input().split())

def late(x, y):
    if y == 1:
        return x%c
    temp = late(x, y//2)
    if y % 2: # 홀수
        return temp * temp * x % c
    else:
        return temp * temp % c

print(late(a, b))