def solution(n):
    dp = [0] + [1] * n
    for i in range(1, len(dp)):
        dp[i] = dp[i-1] + dp[i]
        if i % 2:
            dp[i] += 1
    return dp[n-1]