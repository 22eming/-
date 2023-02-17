from sys import stdin
N = int(stdin.readline())
house = [ list(map(int, stdin.readline().split())) for i in range(N) ]
ans = 1e9
for k in range(3):
    dp = [[ans,ans,ans] for _ in range(N)]
    dp[0][k] = house[0][k]
    for i in range(1, N):
        dp[i][0] = house[i][0] + min(dp[i-1][1], dp[i-1][2])
        dp[i][1] = house[i][1] + min(dp[i-1][0], dp[i-1][2])
        dp[i][2] = house[i][2] + min(dp[i-1][0], dp[i-1][1])
    for j in range(3):
        if j != k:
            ans = min(ans, dp[-1][j])

print(ans)