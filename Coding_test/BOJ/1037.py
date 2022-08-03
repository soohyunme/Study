import sys
In = sys.stdin.readline
n = int(In())
array = list(map(int, In().split()))
print(min(array) * max(array))