import sys
import heapq
hq = []
n = int(input())
for _ in range(n):
    x, c = map(int, input().split())
    heapq.heappush(hq, (c, x))
dot = heapq.heappop(hq)
tmp = sys.maxsize
answer = 0
while len(hq) > 1:
    if dot[0] == hq[0][0]:
        answer += min(hq[0][1] - dot[1], tmp)
        tmp = hq[0][1] - dot[1]
    else:
        answer += tmp
        tmp = sys.maxsize
    dot = heapq.heappop(hq)
else:
    answer += (hq[0][1] - dot[1]) + min(hq[0][1] - dot[1], tmp) if tmp != sys.maxsize else (hq[0][1] - dot[1]) * 2
print(answer)