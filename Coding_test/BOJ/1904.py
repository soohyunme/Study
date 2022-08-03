import sys
n = int(sys.stdin.readline())
dp = [0] * (n + 2)
dp[0] = 0
dp[1] = 1
dp[2] = 2
for i in range(3, n+1):
    dp[i] = dp[i-1] + dp[i-2]
    if dp[i] >= 15746:
        dp[i] %= 15746
print(dp[n])
