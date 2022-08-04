import sys
import heapq
input = sys.stdin.readline
n = int(input())
hq = []
heapq.heapify(hq)
for _ in range(n):
    num = int(input())
    if not num:
        print(heapq.heappop(hq) if hq else 0)
    else:
        heapq.heappush(hq, num)
