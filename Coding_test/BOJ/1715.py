import sys
import heapq
hq = []
answer = 0
for _ in range(int(sys.stdin.readline())):
    heapq.heappush(hq, int(sys.stdin.readline()))
while len(hq) > 1:
    tmp = heapq.heappop(hq) + heapq.heappop(hq)
    answer += tmp
    heapq.heappush(hq, tmp)
print(answer)