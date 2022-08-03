from collections import deque

n, m, v = map(int, input().split())
graph = [[0] * (n+1) for _ in range(n+1)]

for _ in range(m):
    n1, n2 = map(int, input().split())
    graph[n1][n2] = graph[n2][n1] = 1


def dfs(start_node, visited=[]):
    visited.append(start_node)
    print(start_node, end=' ')
    for i in range(n+1):
        if graph[start_node][i] == 1 and i not in visited:
            dfs(i, visited)


def bfs(start_node):
    visited = [start_node]
    q = deque()
    q.append(start_node)
    while q:
        tmp = q.popleft()
        print(tmp, end=' ')
        for i in range(len(graph[tmp])):
            if graph[tmp][i] == 1 and i not in visited:
                visited.append(i)
                q.append(i)


dfs(v)
print()
bfs(v)
