x, y, c = map(float, input().split())

h = min(x, y)
l = 1
pow_x, pow_y = x**2, y**2
answer = 0
while l+0.001 <= h:
    mid = (h+l) / 2
    
    h1 = (pow_x - mid**2) ** 0.5
    h2 = (pow_y - mid**2) ** 0.5
    c_hat = (h1*h2) / (h1+h2)
    
    if c_hat >= c:
        l = mid
        answer = mid
    else:
        h = mid

print('{:.3f}'.format(answer))