import math
from itertools import combinations
l = int(input())
s = sorted(list(map(int, input().split())))
n = int(input())
tmp = 0
answer = 0
for x in s:
    if x < n:
        tmp = x
    else:
        print(len(set(map(lambda z: z if z[0] <= n <= z[1] else 0, combinations(range(tmp+1, x), 2))) - set({0})))
        break

