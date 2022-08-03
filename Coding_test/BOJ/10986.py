import sys
input = sys.stdin.readline
n, m = map(int, input().split())
arr = list(map(int, input().split()))
dt = [0] * m
s = 0
ans = 0
for i in range(n):
    s += arr[i]
    res = s % m
    if not res:
        ans += 1
    dt[res] += 1

for i in range(m):
    ans += dt[i] * (dt[i] - 1) // 2
print(ans)