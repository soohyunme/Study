import numpy as np

table = np.zeros((19, 19), int)

for i in range(19):
    input_list = list(map(int, input().split()))
    for j in range(19):
        table[i, j] = input_list[j]
n = int(input())

for i in range(n):
    x, y = input().split()
    for j in range(19):
        if table[j-1][int(y)-1] == 0:
            table[j-1][int(y)-1] = 1
        else:
            table[j-1][int(y)-1] = 0
        if table[int(x)-1][j-1] == 0:
            table[int(x)-1][j-1] = 1
        else:
            table[int(x)-1][j-1] = 0

for i in range(19):
    for j in range(19):
        print(table[i, j], end=' ')
    print()
