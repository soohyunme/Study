import sys
In = sys.stdin.readline

n = int(In())
array = []
for i in range(n):
    x, y = In().split()
    array.append((int(x), int(y)))
array.sort()
for i in range(n):
    print(*array[i])

