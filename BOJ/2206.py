from collections import deque
n, m = map(int, input().split())
MAP = [list(map(int, list(input()))) for _ in range(n)]
visit = [[[0, 0] for _ in range(m)] for _ in range(n)]
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]
def bfs():
    q = deque()
    q.append([0, 0, 0])
    while q:
        x, y, w = q.popleft()
        if x == m - 1 and y == n - 1:
            return visit[y][x][w] + 1
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < m and 0 <= ny < n:
                if not MAP[ny][nx] and not visit[ny][nx][w]:
                    visit[ny][nx][w] = visit[y][x][w] + 1
                    q.append((nx, ny, w))
                elif MAP[ny][nx] and w == 0:
                    visit[ny][nx][w+1] = visit[y][x][w] + 1
                    q.append((nx, ny, w+1))
    return -1
print(bfs())

