# pypy
import sys
input = sys.stdin.readline
print = sys.stdout.write
s = input().rstrip()
q = int(input())
arr = [[0] * 26 for _ in range(len(s) + 1)]
for i, x in enumerate(s):
    alpha = ord(x) - 97
    arr[i][alpha] = 1
    for j in range(26):
        arr[i][j] += arr[i-1][j]
for _ in range(q):
    a, l, r = input().split()
    l, r = map(int, [l, r])
    print(str(arr[r][ord(a)-97] - arr[l-1][ord(a)-97]) + '\n')

