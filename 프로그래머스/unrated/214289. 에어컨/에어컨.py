def solution(temperature, t1, t2, a, b, onboard):
    temperature, t1, t2 = temperature + 11, t1 + 11, t2 + 11
    dp = [[float("inf")] * 53 for _ in range(len(onboard))]
    dp[0][temperature] = 0
    min_t, max_t = min(temperature, t1), max(temperature, t2)
    for i in range(1, len(onboard)):
        start, end = [t1, t2] if onboard[i] else [min_t, max_t]

        for j in range(start, end + 1):
            l = dp[i - 1][j - 1] if j-1 < temperature else dp[i - 1][j - 1] + a
            m = dp[i - 1][j] if j == temperature else dp[i - 1][j] + b
            h = dp[i - 1][j + 1] if j+1 > temperature else dp[i - 1][j + 1] + a

            dp[i][j] = min(l, m, h)
    return min(dp[-1])