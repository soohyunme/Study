n, k = map(int, input().split())
arr = list(map(int, input().split()))
num = sum(arr[:k])
dp = [num] * (n + 1)
for i in range(k, n):
    dp[i] = dp[i-1] - arr[i-k] + arr[i]
print(max(dp))