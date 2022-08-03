# def dfs(matrix, x, y):
#     matrix[x][y] = 1  # 방문 처리
#     for k in range(4):  # 인접 노드 탐색
#         nx = x + dx[k]
#         ny = y + dy[k]
#         if nx < 0 or ny < 0 or nx >= w or ny >= h:
#             continue
#         if matrix[nx][ny] == 0:
#             a = nx  # 좌표 이동
#             b = ny  # 좌표 이동
#             dfs(matrix, a, b)
#
#
# count = 0
# matrix = []
# w, h = map(int, input().split())
#
# for i in range(w):
#     matrix.append(list(map(int, input())))
# dx = [-1, 0, 1, 0]
# dy = [0, -1, 0, 1]
#
# for i in range(w):
#     for j in range(h):
#         if matrix[i][j] == 0:
#             dfs(matrix, i, j)
#             count += 1
# print(count)


#####################

def dfs(x, y):
    if x <= -1 or x >= n or y <= -1 or y >= m:
        return False
    if graph[x][y] == 0:
        graph[x][y] = 1
        dfs(x - 1, y)
        dfs(x, y - 1)
        dfs(x + 1, y)
        dfs(x, y + 1)
        return True
    return False


n, m = map(int, input().split())
graph = []
for i in range(n):
    graph.append(list(map(int, input())))

result = 0
for i in range(n):
    for j in range(m):
        if dfs(i, j) == True:
            result += 1
print(result)
