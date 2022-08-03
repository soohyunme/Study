import sys
from collections import deque
arr = deque()
out = sys.stdout.write
for _ in range(int(sys.stdin.readline().rstrip())):
    command = sys.stdin.readline().rstrip()
    if 'push_front' in command:
        arr.appendleft(command.split()[1])
    elif 'push_back' in command:
        arr.append(command.split()[1])
    elif 'pop_front' == command:
        out(str(arr.popleft() if len(arr) else -1)+'\n')
    elif 'pop_back' == command:
        out(str(arr.pop() if len(arr) else -1)+'\n')
    elif 'size' == command:
        out(str(len(arr))+'\n')
    elif 'empty' == command:
        out(str(0 if len(arr) else 1)+'\n')
    elif 'front' == command:
        out(str(arr[0] if len(arr) else -1)+'\n')
    else:
        out(str(arr[-1] if len(arr) else -1)+'\n')
