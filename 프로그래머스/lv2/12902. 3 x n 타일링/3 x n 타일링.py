def solution(n):
    dp = [0, 3, 11]
    for i in range(3, n//2 + 1):
        dp.append(dp[i-1]*3 + sum(dp[:i-1])*2 + 2)
    return dp[-1] % 1000000007