import sys
import heapq
arr = [tuple(map(int, sys.stdin.readline().split())) for _ in range(int(sys.stdin.readline()))]
heapq.heapify(arr)
answer = 0
hq = []
while arr:
    s, e = heapq.heappop(arr)
    if hq and hq[0] <= s:
        heapq.heappop(hq)
    heapq.heappush(hq, e)
    answer = max(len(hq), answer)
print(answer)
