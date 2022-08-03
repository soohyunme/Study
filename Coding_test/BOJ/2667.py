dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]


def dfs(x, y):
    if x <= -1 or y <= -1 or x >= n or y >= n:
        return 0
    if arr[x][y] == 1:
        tmp = 0
        arr[x][y] = 0
        for k in range(4):
            tmp += dfs(x+dx[k], y+dy[k])
        return tmp + 1
    return 0


n = int(input())
arr = [list(map(int, input())) for _ in range(n)]
answer = []
for i in range(n):
    for j in range(n):
        tmp = dfs(i, j)
        if tmp:
            answer.append(tmp)
print(len(answer))
answer.sort()
[print(x) for x in answer]