import numpy as np


h, w = map(int, input().split())
table = np.zeros((h, w)).astype(int)

n = int(input())
for i in range(n):
    l, d, x, y = map(int, input().split())
    for j in range(l):
        if d == 0:
            table[x-1, y+j-1] = 1
        else:
            table[x+j-1, y-1] = 1

for i in range(h):
    for j in range(w):
        print(table[i, j], end=' ')
    print()
