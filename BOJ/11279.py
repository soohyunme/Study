import sys
import heapq
heap = []
for _ in range(int(sys.stdin.readline().rstrip())):
    x = int(sys.stdin.readline().rstrip())
    if x:
        heapq.heappush(heap, (-x, x))
    else:
        if len(heap) >= 1:
            print(heapq.heappop(heap)[1])
        else:
            print(0)
