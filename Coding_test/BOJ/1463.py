def make_one(i):
    if dp[i]:
        return dp[i]
    dp[i] = min(dp[int(i/2)] + i % 2, dp[int(i/3)] + i % 3, dp[i-1]) + 1
    return dp[i]

import sys
n = int(sys.stdin.readline())

answer = 0
dp = [0, 0, 1, 1, 2, 3, 2, 3, 3] + [0] * (n - 8)
for i in range(2, n+1):
    make_one(i)

print(dp[n])
