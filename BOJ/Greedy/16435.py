import sys
In = sys.stdin.readline

n, k = map(int, In().split())
array = list(map(int, In().split()))

array.sort()

for i in array:
    if k < i:
        break
    k += 1
print(k)

