import sys
n = int(sys.stdin.readline())

for i in range(n):
    words = sys.stdin.readline().split()
    [print(word[::-1], end=' ') for word in words]





