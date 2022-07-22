import sys
input = sys.stdin.readline
n, m = map(int, input().split())
arr = list(map(int, input().split()))
s = [0]
num = 0
for x in arr:
    num += x
    s.append(num)

for _ in range(m):
    i, j = map(int, input().split())
    print(s[j] - s[i-1])