import sys
input = sys.stdin.readline
n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
mat = []
for i, row in enumeratae(arr):
    num = 0
    tmp = []
    for j, x in enumerate(row):
        num += x
        tmp.append(num)
    mat.append(tmp)
for _ in range(m):
    num = 0
    x1, y1, x2, y2 = map(lambda x: int(x)-1, input().split())
    for x in range(x1, x2+1):
        num += mat[x][y2] - mat[x][y1] + arr[x][y1]
    print(num)
