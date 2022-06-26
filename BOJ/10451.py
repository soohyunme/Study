from collections import defaultdict
T = int(input())
for t in range(T):
    graph = defaultdict(int)
    n = int(input())
    visit = [False] * 1001
    answer = 0
    arr = list(map(int, input().split()))
    for i in range(n):
        graph[i+1] = arr[i]
    for i in range(1, n+1):
        next_node = graph[i]
        if not visit[i]:
            answer += 1
        visit[i] = True
        while not visit[next_node]:
            visit[next_node] = True
            next_node = graph[next_node]
    print(answer)
