from collections import deque
n, m = map(int, input().split())
graph = [[0 for _ in range(n+1)] for _ in range(n+1)]
for _ in range(m):
    n1, n2 = map(int, input().split())
    graph[n1][n2] = graph[n2][n1] = 1
q = deque()
answer = [0] * (n + 1)
for i in range(1, n+1):
    tmp = 1
    visit = [False] * (n + 1)
    dist = [0] * (n + 1)
    visit[i] = True
    for idx, x in enumerate(graph[i]):
        if x:
            visit[idx] = True
            dist[idx] = 1
            q.append(idx)
    while q:
        v = q.popleft()
        for idx, x in enumerate(graph[v]):
            if x and not visit[idx]:
                visit[idx] = True
                dist[idx] = dist[v] + 1
                q.append(idx)
    answer[i] = (sum(dist))
print(answer.index(min(answer[1:])))