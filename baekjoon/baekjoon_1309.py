N = int(input())

a, b, c = 1, 1, 1
for i in range(1, N):
    a, b, c = a+b+c, a+c, a+b

print((a+b+c) % 9901)
