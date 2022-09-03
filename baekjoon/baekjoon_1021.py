from collections import deque

N, M = map(int, input().split())
loc = list(map(int, input().split()))
que = deque([i for i in range(1, N+1)])
cnt = 0

for l in loc:
    if que.index(l) <= len(que) / 2:
        while que[0] != l:
            que.append(que.popleft())
            cnt += 1
    else:
        while que[0] != l:
            que.appendleft(que.pop())
            cnt += 1
    que.popleft()

print(cnt)