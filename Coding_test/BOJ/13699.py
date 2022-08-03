import sys
n = int(input())
if not n:
    print(1)
    sys.exit()
dp = [0] * (n + 1)
dp[0] = 1
dp[1] = 1
for i in range(2, n+1):
    if i % 2:
        dp[i] = sum(dp[j] * 2 * dp[i-j-1] for j in range(i//2)) + dp[i//2]**2
    else:
        dp[i] = sum(dp[j] * 2 * dp[i-j-1] for j in range(i//2))
print(dp[n])
