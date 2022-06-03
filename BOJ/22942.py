import sys
arr = []
stack = []
for i in range(int(sys.stdin.readline().rstrip())):
    x, r = map(int, sys.stdin.readline().rstrip().split())
    arr.append((x - r, '(', i))
    arr.append((x + r, ')', i))
arr.sort(key=lambda x: x[0])

for x, s, i in arr:
    if stack and s == ')':
        if stack[-1][1] != i:
            print('NO')
            break
        else:
            stack.pop()
    else:
        stack.append((s, i))
else:
    print('YES')

'''
# 시간 초과
from itertools import combinations
import sys
arr = [(tuple(map(int, sys.stdin.readline().rstrip().split()))) for _ in range(int(sys.stdin.readline().rstrip()))]
for (x1, r1), (x2, r2) in combinations(arr, 2):
    d = ((x1-x2)**2)**0.5
    if abs(r1-r2) < d < r1+r2:
        sys.stdout.write('NO')
        break
else:
    sys.stdout.write('YES')
'''