import sys
import heapq
hq = []
for _ in range(int(sys.stdin.readline())):
    nums = list(map(int, sys.stdin.readline().split()))
    if not hq:
        for num in nums:
            heapq.heappush(hq, num)
    else:
        for num in nums:
            if num > hq[0]:  # heapq는 최소힙 따라서 0번 인덱스가 최소값
                heapq.heappop(hq)
                heapq.heappush(hq, num)
print(hq[0])

