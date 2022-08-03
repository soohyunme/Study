import sys
import heapq

max_heap, min_heap = [], []
visited = [False] * 100001
for N in range(int(sys.stdin.readline())):
    p, l = map(int, sys.stdin.readline().split())
    heapq.heappush(min_heap, (l, p))
    heapq.heappush(max_heap, (-l, -p))
    visited[p] = True

for M in range(int(sys.stdin.readline())):
    s = sys.stdin.readline().split()
    if s[0] == 'add':
        while min_heap and not visited[min_heap[0][1]]:
            heapq.heappop(min_heap)
        while max_heap and not visited[-max_heap[0][1]]:
            heapq.heappop(max_heap)
        p, l = map(int, s[1:])
        heapq.heappush(min_heap, (l, p))
        heapq.heappush(max_heap, (-l, -p))
        visited[p] = True
        continue
    c, p = s[0], int(s[1])
    if c == 'solved':
        visited[p] = False
    elif p == 1:
        while max_heap and not visited[-max_heap[0][1]]:
            heapq.heappop(max_heap)
        print(-max_heap[0][1])
    elif p == -1:
        while min_heap and not visited[min_heap[0][1]]:
            heapq.heappop(min_heap)
        print(min_heap[0][1])
