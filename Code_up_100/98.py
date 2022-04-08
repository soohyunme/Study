import numpy as np

table = np.zeros((10, 10), int)

for i in range(10):
    table[i] = list(map(int, input().split()))

x, y = 1, 1

while not ((x == 8 and y == 8) or (table[x+1, y] == 1 and table[x, y+1] == 1) or (table[x, y] == 2)):
    table[x, y] = 9
    if table[x, y+1] == 1:
        x += 1
    else:
        y += 1
table[x, y] = 9

for i in range(10):
    for j in range(10):
        print(table[i, j], end=' ')
    print()

