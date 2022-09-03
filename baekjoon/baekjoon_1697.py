from collections import deque
N, K = map(int, input().split())

MAX = 100000
que = deque([N])
dp = [0]*(MAX + 1)

while que:
    loc = que.popleft()
    if loc == K:
        print(dp[loc])
        break
    for dx in [loc-1, loc+1, loc*2]:
        if 0 <= dx <= MAX and not dp[dx]:
            dp[dx] = dp[loc] + 1
            que.append(dx)
