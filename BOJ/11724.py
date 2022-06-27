import sys
sys.setrecursionlimit(15000)
n, m = map(int, sys.stdin.readline().split())
graph = [[0] * (n+1) for _ in range(n+1)]
visit = [False] * (n+1)
answer = 0
for i in range(m):
    n1, n2 = map(int, sys.stdin.readline().split())
    graph[n1][n2] = graph[n2][n1] = 1


def dfs(start_node):
    for k in range(len(graph[start_node])):
        if graph[start_node][k] and not visit[k]:
            visit[k] = True
            dfs(k)
    return 1


for node in range(1, n+1):
    if not visit[node]:
        answer += dfs(node)
print(answer)