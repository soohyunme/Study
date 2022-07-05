import sys
sys.setrecursionlimit(15000)
n, m, k = map(int, input().split())
MAP = [[0] * m for _ in range(n)]
visit = []
for _ in range(k):
    r, c = map(int, input().split())
    MAP[r-1][c-1] = 1
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]


def dfs(x, y):
    tmp = 1
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < m and 0 <= ny < n and MAP[ny][nx] and not (nx, ny) in visit:
            visit.append((nx, ny))
            tmp += dfs(nx, ny)
    return tmp

answer = 0
for x in range(m):
    for y in range(n):
        if MAP[y][x] and not (x, y) in visit:
            visit.append((x, y))
            answer = max(answer, dfs(x, y))
print(answer)