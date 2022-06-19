from collections import defaultdict
import sys
n, k = map(int, sys.stdin.readline().split())
arr = list(map(int, sys.stdin.readline().split()))
cnt = defaultdict(int)
l = r = 0
answer = 0
while r < n:
    if cnt[arr[r]] < k:
        cnt[arr[r]] += 1
        r += 1
    else:
        cnt[arr[l]] -= 1
        l += 1
    answer = max(answer, r-l)
print(answer)