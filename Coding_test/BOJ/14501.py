n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
dp = [0] * (n + 1)
for i in range(n-1, -1, -1):
    if i + arr[i][0] > n:
        dp[i] = dp[i+1]
    else:
        dp[i] = max(dp[i+1], dp[i+arr[i][0]] + arr[i][1])
print(dp[0])