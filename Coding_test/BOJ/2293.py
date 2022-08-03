n, k = map(int, input().split())
arr = [int(input()) for _ in range(n)]
dp = [1] + [0] * k
for x in arr:
    for i in range(x, k+1):
        dp[i] += dp[i-x]
print(dp[k])
