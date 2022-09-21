from collections import deque
N, M = map(int, input().split())

computer = [[] for _ in range(N+1)]
for _ in range(M):
    a, b = map(int, input().split())
    computer[b].append(a)

answer, cnt = [], 0
for i in range(1, N+1):
    que = deque([i])
    com = [False]*(N+1)
    count = 1
    while que:
        q = que.popleft()
        for j in computer[q]:
            if not com[j]:
                com[j] = True
                que.append(j)
                count += 1

    if count > cnt:
        answer = [i]
        cnt = count
    elif count == cnt:
        answer.append(i)

print(*answer)
