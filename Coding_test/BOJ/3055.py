from collections import deque
import sys

r, c = map(int, input().split())
MAP = [list(input()) for _ in range(r)]
visit = [[False] * (c + 1) for _ in range(r)]
water = deque()
path = deque()
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]
for i in range(r):
    for j in range(c):
        if MAP[i][j] == '*':
            water.append([j, i])
        elif MAP[i][j] == 'S':
            path.append([j, i, 1])
        elif MAP[i][j] == 'X':
            visit[i][j] = True

while path:
    for _ in range(len(water)):
        x, y = water.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < c and 0 <= ny < r and MAP[ny][nx] == '.':
                water.append([nx, ny])
                MAP[ny][nx] = '*'
                visit[ny][nx] = True
    for _ in range(len(path)):
        x, y, cnt = path.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < c and 0 <= ny < r and MAP[ny][nx] == 'D':
                print(cnt)
                sys.exit()
            elif 0 <= nx < c and 0 <= ny < r and not visit[ny][nx]:
                path.append([nx, ny, cnt + 1])
                visit[ny][nx] = True
print('KAKTUS')
