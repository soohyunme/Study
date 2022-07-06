# pypy
from itertools import permutations
import sys
n = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))
a = list(map(int, sys.stdin.readline().split()))
operators = []
for i, x in enumerate(a):
    if i == 0:
        for _ in range(x):
            operators.append('+')
    if i == 1:
        for _ in range(x):
            operators.append('-')
    if i == 2:
        for _ in range(x):
            operators.append('*')
    if i == 3:
        for _ in range(x):
            operators.append('/')
ops = permutations(operators, len(operators))


def operation(n1, op, n2):
    if op == '+':
        return n1 + n2
    elif op == '-':
        return n1 - n2
    elif op == '*':
        return n1 * n2
    else:
        if n1 < 0:
            return -(-n1//n2)
        return n1//n2


answer_m = sys.maxsize
answer_M = -sys.maxsize
for op in ops:
    tmp = arr[0]
    for idx, x in enumerate(op):
        a = operation(tmp, x, arr[idx+1])
        tmp = a

    answer_M = max(answer_M, tmp)
    answer_m = min(answer_m, tmp)
print(answer_M)
print(answer_m)
