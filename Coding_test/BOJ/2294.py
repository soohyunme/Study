import sys
n, k = map(int, input().split())
arr = sorted([int(input()) for _ in range(n)])
dp = [0] + [sys.maxsize] * k
for num in arr:
    for i in range(num, k+1):
        dp[i] = min(dp[i], dp[i-num] + 1)
print(dp[k] if not dp[k] == sys.maxsize else -1)