import sys
n, m = map(int, sys.stdin.readline().rstrip().split())
s = set()
answer = 0
for _ in range(n):
    s.update({sys.stdin.readline().rstrip()})
for _ in range(m):
    answer += 1 if sys.stdin.readline().rstrip() in s else 0
print(answer)