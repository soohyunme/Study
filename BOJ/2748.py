import sys
def fibonacci(x):
    if dp[x] != 0:
        return dp[x]
    if x == 0:
        return 0
    elif x == 1:
        return 1
    dp[x] = fibonacci(x-1) + fibonacci(x-2)
    return dp[x]

n = int(sys.stdin.readline())
dp = [0] * (n + 1)
print(fibonacci(n))
