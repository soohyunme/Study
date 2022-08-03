from collections import deque
import sys
sys.setrecursionlimit(15000)
dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]


def dfs(x, y, h):
    for i in range(4):
        nx, ny = x+dx[i], y+dy[i]
        if 0 <= nx < n and 0 <= ny < n and not visit[nx][ny] and MAP[nx][ny] > h:
            visit[nx][ny] = True
            dfs(nx, ny, h)
    return 1


n = int(sys.stdin.readline())
MAP = [list(map(int, sys.stdin.readline().split())) for i in range(n)]
q = deque()
answer = 0
for h in range(max(max(MAP))):
    visit = [[False for _ in range(n)] for __ in range(n)]
    tmp = 0
    for i in range(n):
        for j in range(n):
            if not visit[i][j] and MAP[i][j] > h:
                visit[i][j] = True
                tmp += dfs(i, j, h)
    answer = max(tmp, answer)
print(answer)
