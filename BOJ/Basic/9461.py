def func(n):
    if dp[n]:
        return dp[n]
    dp[n] = func(n-5) + func(n-1)
    return dp[n]


dp = [1, 1, 1, 2, 2, 3, 4, 5, 7, 9] + [0] * 90
t = int(input())

for i in range(t):
    n = int(input())
    print(func(n-1))
