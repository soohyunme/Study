import sys
In = sys.stdin.readline
n = int(In())
for i in range(n):
    a, b = map(int, In().split())
    mul = 0
    for j in range(1, max(a, b) + 1):
        if a % j == 0 and b % j == 0:
            mul = j
    div = int(a * b / mul)
    print(div)

