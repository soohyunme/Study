import sys
import heapq
input = sys.stdin.readline
hq = [list(map(int, input().split())) for _ in range(int(input()))]
heapq.heapify(hq)
room = []
answer = 0
while hq:
    now = heapq.heappop(hq)
    if room and room[0] <= now[0]:
        heapq.heappop(room)
    heapq.heappush(room, now[1])
    answer = max(answer, len(room))
print(answer)

