n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
dp = [arr[0] + [0, 0, 0] for _ in range(n)]
for i in range(1, n):
    dp[i] = [arr[i][0] + min(dp[i-1][1], dp[i-1][2]),
             arr[i][1] + min(dp[i-1][0], dp[i-1][2]),
             arr[i][2] + min(dp[i-1][0], dp[i-1][1])]
print(min(dp[n-1]))
