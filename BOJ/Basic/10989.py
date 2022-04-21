import sys
In = sys.stdin.readline

n = int(In())
d = [0] * 10001

for i in range(n):
    d[int(In().strip())] += 1

for i in range(len(d)):
    if d[i] != 0:
        for j in range(d[i]):
            print(i)