import sys
from collections import deque
In = sys.stdin.readline
for _ in range(int(input())):
    p = In().rstrip()
    c = int(In().rstrip())
    q = deque(map(int, In().rstrip().lstrip('[').rstrip(']').split(','))) \
        if c else deque(In().rstrip().lstrip('[').rstrip(']'))
    reverse = 0
    for command in p:
        if command == 'R':
            reverse = 0 if reverse else 1
        elif len(q):
            if reverse == 1:
                q.pop()
            else:
                q.popleft()
        else:
            print('error')
            break
    else:
        answer = list(q)[::-1] if reverse else list(q)
        print('[', end='')
        print(*answer, sep=',', end='')
        print(']')
