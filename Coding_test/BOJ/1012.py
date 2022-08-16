import sys
sys.setrecursionlimit(15000)
input = sys.stdin.readline

def dfs(x, y):
    maps[y][x] = 0
    for i in range(4):
        nx = dx[i] + x
        ny = dy[i] + y
        if 0 <= nx < m and 0 <= ny < n and maps[ny][nx]:
            dfs(nx, ny)

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

T = int(input())
for _ in range(T):
    m, n, k = map(int, input().split())
    maps = [[0 for _ in range(m)] for _ in range(n)]
    for _ in range(k):
        n1, n2 = map(int, input().split())
        maps[n2][n1] = 1
    answer = 0
    for i in range(m):
        for j in range(n):
            if maps[j][i]:
                dfs(i, j)
                answer += 1
    print(answer)
