n = int(input())
N = n - len(str(n))*9
if N < 0: N = 0 
for i in range(N, n):
    if i + sum(map(int, list(str(i)))) == n:
        print(i)
        break
else:print(0)