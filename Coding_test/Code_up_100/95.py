import numpy as np

n = int(input())

mt = np.zeros((19, 19)).astype(int)
for i in range(n):
    i, j = map(int, input().split())
    mt[i-1, j-1] = 1


for i in mt:
    for j in i:
        print(j, end=' ')
    print()
