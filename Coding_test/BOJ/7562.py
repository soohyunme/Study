# pypy
from collections import deque
import sys
input = sys.stdin.readline
dx = [-1, 1, -2, 2, -2, 2, -1, 1]
dy = [-2, -2, -1, -1, 1, 1, 2, 2]
for _ in range(int(input())):
    q = deque()
    l = int(input())
    maps = [[0 for _ in range(l)] for _ in range(l)]
    q.append((map(int, (input().split()))))
    target_x, target_y = map(int, input().split())
    while q:
        x, y = q.popleft()
        if x == target_x and y == target_y:
            print(maps[x][y])
            break
        for i in range(8):
            nx = dx[i] + x
            ny = dy[i] + y
            if 0 <= nx < l and 0 <= ny < l and (not maps[nx][ny] or maps[nx][ny] < maps[x][y] + 1):
                maps[nx][ny] = maps[x][y] + 1
                q.append((nx, ny))