from collections import deque
import sys
input = sys.stdin.readline
n = int(input())
n1, n2 = map(int, input().split())
m = int(input())
graph = [[0 for x in range(n+1)] for _ in range(n+1)]
for _ in range(m):
    tmp1, tmp2 = map(int, input().split())
    graph[tmp1][tmp2] = graph[tmp2][tmp1] = 1
q = deque()
q.append(n1)
visit = [n1]
dist = [0 for _ in range(n+1)]
answer = 0
while q:
    v = q.popleft()
    for idx, x in enumerate(graph[v]):
        tmp = dist[v]
        if x and idx not in visit:
            tmp += 1
            dist[idx] = tmp
            visit.append(idx)
            q.append(idx)
            if idx == n2:
                print(dist[n2])
                sys.exit()
    answer += 1
print(-1)
