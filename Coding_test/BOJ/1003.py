t = int(input())
d = [[0]*2 for _ in range(41)]
d[0] = [1, 0]
d[1] = [0, 1]

for i in range(t):
    n = int(input())
    for j in range(2, n+1):
        d[j][0] = d[j - 1][0] + d[j - 2][0]
        d[j][1] = d[j - 1][1] + d[j - 2][1]
    print(d[n][0], d[n][1])
