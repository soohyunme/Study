from collections import deque
n, m = map(int, input().split())
MAP = [list(map(int, input())) for _ in range(n)]

dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]
q = deque([(0, 0)])
while q:
    x, y = q.popleft()
    for i in range(4):
        nx, ny = x+dx[i], y+dy[i]
        if nx < 0 or ny < 0 or nx >= m or ny >= n:
            continue
        if MAP[ny][nx] == 1:
            q.append((nx, ny))
            MAP[ny][nx] = MAP[y][x] + 1
print(MAP[n-1][m-1])