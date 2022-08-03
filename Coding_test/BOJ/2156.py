import sys
input = sys.stdin.readline
n = int(input())
arr = [int(input()) for _ in range(n)]
if n < 3:
    print(sum(arr))
    sys.exit()
dp = [arr[0]] + [0 for _ in range(n)]
dp[1] = sum(arr[:2])
dp[2] = max(sum(arr[:2]), sum(arr[1:3]), arr[0] + arr[2])
for i in range(3, n):
    dp[i] = max(dp[i-3] + arr[i-1] + arr[i], dp[i-2] + arr[i], dp[i-1])
print(dp[n-1])
