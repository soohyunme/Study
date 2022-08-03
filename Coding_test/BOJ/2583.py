import sys
sys.setrecursionlimit(10000)
m, n, k = map(int, input().split())
MAP = [[0] * n for _ in range(m)]

for _ in range(k):
    x1, y1, x2, y2 = map(int, input().split())
    y1, y2 = m - y1 - 1, m - y2 - 1
    for i in range(y2+1, y1+1):
        for j in range(x1, x2):
            MAP[i][j] = 1

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]


def dfs(x, y, visit=[]):
    tmp = 0
    MAP[y][x] = 1
    visit.append([x, y])
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < n and 0 <= ny < m and not MAP[ny][nx] and not [nx, ny] in visit:
            MAP[ny][nx] = 1
            tmp += dfs(nx, ny, visit)
    return tmp + 1
answer = []
for y in range(m):
    for x in range(n):
        if not MAP[y][x]:
            answer.append(dfs(x, y))
print(len(answer))
print(' '.join(map(str, sorted(answer))))
