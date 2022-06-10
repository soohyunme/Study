import sys

def func(a, b, c):
    if a <= 0 or b <= 0 or c <= 0:
        return 1
    elif a > 20 or b > 20 or c > 20:
        return func(20, 20, 20)
    if dp[a][b][c]:
        return dp[a][b][c]
    elif a < b < c:
        dp[a][b][c] = func(a, b, c-1) + func(a, b-1, c-1) - func(a, b-1, c)
        return dp[a][b][c]
    else:
        dp[a][b][c] = func(a-1, b, c) + func(a-1, b-1, c) + func(a-1, b, c-1) - func(a-1, b-1, c-1)
        return dp[a][b][c]


MAX = 21
a = b = c = 0
dp = [[[0]*MAX for _ in range(MAX)] for __ in range(MAX)]

while True:
    a, b, c = map(int, sys.stdin.readline().split())
    if a == b == c == -1:
        break
    print(f'w({a}, {b}, {c}) = {func(a, b, c)}')

