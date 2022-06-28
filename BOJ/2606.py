n = int(input())
edge = int(input())
virus = [False] * (n+1)
graph = [[0] * (n+1) for _ in range(n+1)]

for i in range(edge):
    n1, n2 = map(int, input().split())
    graph[n1][n2] = graph[n2][n1] = 1


def dfs(node):
    if virus[node]:
        return
    virus[node] = True
    for k in range(n+1):
        if graph[node][k] and not virus[k]:
            dfs(k)
    return 0


dfs(1)
print(sum(virus)-1)
