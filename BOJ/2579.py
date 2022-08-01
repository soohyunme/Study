import sys
input = sys.stdin.readline
n = int(input())
arr = [int(input()) for _ in range(n)]
dp = [0 for _ in range(n)]
if n < 3:
    print(sum(arr))
    sys.exit()
elif n == 3:
    print(max(arr[0] + arr[2], arr[1] + arr[2]))
dp[0] = arr[0]
dp[1] = sum(arr[:2])
dp[2] = max(arr[0] + arr[2], arr[1] + arr[2])
for i in range(3, n-1):
    dp[i] = max(dp[i-2] + arr[i], dp[i-3] + arr[i-1] + arr[i])
dp[n-1] = max(dp[n-4] + arr[n-1] + arr[n-2], dp[n-3] + arr[n-1])
print(dp[n-1])