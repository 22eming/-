from collections import defaultdict
N, D = map(int, input().split())
dp = list(range(D+1))

short_cut = defaultdict(list)
for _ in range(N):
    s, e, d = map(int, input().split())
    short_cut[s].append([e, d])

for i in range(D+1):
    if i > 0 and dp[i] > dp[i-1]+1:
        dp[i] = dp[i-1]+1
    if short_cut.get(i) != []:
        for e, d in short_cut[i]:
            if e <= D:
                dp[e] = min(dp[e], dp[i]+d)

print(dp[-1])