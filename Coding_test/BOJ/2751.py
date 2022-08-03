import sys
In = sys.stdin.readline

n = int(input())
array = []
for i in range(n):
    array.append(int(In().strip()))
array.sort()
for i in array:
    print(i)