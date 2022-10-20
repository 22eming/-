N, M = map(int, input().split())

friend = [set() for _ in range(N+1)]
for _ in range(M):
    a, b = map(int, input().split())
    friend[a].add(b)
    friend[b].add(a)


answer = float('inf')
for i in range(1, N+1):
    for j in friend[i]:
        if i == j:
            continue
        for k in friend[j]:
            if i == k or j == k:
                continue
            if j in friend[i] and k in friend[i] and k in friend[j]:
                answer = min(answer, len(
                    friend[i]) + len(friend[j]) + len(friend[k]) - 6)

if answer == float('inf'):
    print(-1)
else:
    print(answer)
