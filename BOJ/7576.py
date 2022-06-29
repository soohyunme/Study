from collections import deque
import sys
m, n = map(int, input().split())
MAP = [list(map(int, input().split())) for _ in range(n)]
q = deque()
answer = 0
dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]
cnt = 0
for y in range(n):
    for x in range(m):
        if MAP[y][x] == 1:
            q.append((x, y))
while q:
    x, y = q.popleft()
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx < 0 or nx >= m or ny < 0 or ny >= n:
            continue
        if MAP[ny][nx] == 0:
            q.append((nx, ny))
            MAP[ny][nx] = MAP[y][x] + 1
if sum([True if 0 in x else False for x in MAP]):
    print(-1)
    sys.exit()
print(max(max(x) for x in MAP)-1)