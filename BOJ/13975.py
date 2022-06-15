import sys
import heapq
input = sys.stdin.readline
T = int(input())
for _ in range(T):
    __ = input()
    hq = list(map(int, input().split()))
    heapq.heapify(hq)
    answer = 0
    while len(hq) > 1:
        tmp = heapq.heappop(hq) + heapq.heappop(hq)
        answer += tmp
        heapq.heappush(hq, tmp)
    print(answer)

