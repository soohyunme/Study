n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
dp = [[0] * (n + 1) for _ in range(n+1)]

for i in range(1, n+1):
    dp[i][0] = arr[i-1][0] + dp[i-1][0]
    for j in range(1, i):
        dp[i][j] = max(dp[i-1][j-1], dp[i-1][j]) + arr[i-1][j-1]
    dp[i][i] = arr[i-1][i-1] + dp[i-1][i-1]
print(max(dp[n]))
