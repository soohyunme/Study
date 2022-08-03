from collections import deque
import sys
stack = deque()
for _ in range(int(input())):
    s = sys.stdin.readline().rstrip().split()
    if 'push' in s:
        stack.append(s[1])
    elif s[0] == 'pop':
        sys.stdout.write(str(stack.popleft())+'\n' if len(stack) else '-1\n')
    elif s[0] == 'size':
        sys.stdout.write(str(len(stack))+'\n')
    elif s[0] == 'empty':
        sys.stdout.write('0\n' if len(stack) else '1\n')
    elif s[0] == 'front':
        sys.stdout.write(str(stack[0])+'\n' if len(stack) else '-1\n')
    else:
        sys.stdout.write(str(stack[-1])+'\n' if len(stack) else '-1\n')


