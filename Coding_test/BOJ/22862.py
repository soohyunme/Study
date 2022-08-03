import sys
n, k = map(int, sys.stdin.readline().split())
s = list(map(int, sys.stdin.readline().split()))
l = r = 0
cnt = 0
answer = 0
while r < n:
    if cnt <= k:
        cnt += 1 if s[r] % 2 else 0
        r += 1
    else:
        cnt -= 1 if s[l] % 2 else 0
        l += 1
    answer = max(answer, r - l - cnt)
print(answer)
