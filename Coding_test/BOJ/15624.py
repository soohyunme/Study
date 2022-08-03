n = int(input())
dp = [0, 1]
for i in range(3, n+2):
    dp[(i-1) % 2] = (dp[(i-1) % 2] + dp[i % 2]) % 1000000007
print(dp[n % 2])