def solution(n):
    if n < 3:
        return sum([0,1,1][:n])
    dp = [0 for _ in range(n % 1234567 + 1)]
    dp[0] = 0
    dp[1] = 1
    for i in range(2, n % 1234567 + 1):
        dp[i] = (dp[i - 2] + dp[i - 1]) % 1234567
    return dp[n % 1234567]