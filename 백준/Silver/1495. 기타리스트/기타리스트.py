N, S, M = map(int, input().split())
V = list(map(int, input().split()))

vol = [ set() for _ in range(N+1) ]
vol[0] = {S}
for i in range(1, N+1):
    for j in vol[i-1]:
        if j+V[i-1] <= M:
            vol[i].add(j+V[i-1])
        if 0 <= j-V[i-1]:
            vol[i].add(j-V[i-1])

if vol[-1] == set():
    print(-1)
else:
    print(max(vol[-1]))