from collections import deque

N, M = map(int, input().split())

friends = [set() for _ in range(N+1)]
for _ in range(M):
    a, b = map(int, input().split())
    friends[a].add(b)
    friends[b].add(a)

answer = [float('inf'), 0]
for n in range(1, N+1):
    que = deque([n])
    friend = [0] * (N+1)

    while que:
        q = que.popleft()
        for i in friends[q]:
            if friend[i] == 0:
                friend[i] = friend[q] + 1
                que.append(i)

    if answer[0] > sum(friend):
        answer = [sum(friend), n]

print(answer[1])
