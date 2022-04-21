import sys
In = sys.stdin.readline

n = int(In())
array = []
for i in range(n):
    x, y = In().split()
    array.append((int(y), int(x)))
array.sort()
for i in range(n):
    print(array[i][1], array[i][0])

