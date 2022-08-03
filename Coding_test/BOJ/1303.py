m, n = map(int, input().split())
MAP = [list(input()) for _ in range(n)]

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]
visit = []


def dfs(x, y):
    answer = 1
    for k in range(4):
        nx = x + dx[k]
        ny = y + dy[k]
        if 0 <= nx < m and 0 <= ny < n and MAP[y][x] == MAP[ny][nx] and not (nx, ny) in visit:
            visit.append((nx, ny))
            answer += dfs(nx, ny)
    return answer


answer_w = 0
answer_b = 0
for i in range(m):
    for j in range(n):
        if not (i, j) in visit:
            visit.append((i, j))
            if MAP[j][i] == 'W':
                answer_w += dfs(i, j)**2
            else:
                answer_b += dfs(i, j)**2
print(answer_w, answer_b)