import sys
t = int(sys.stdin.readline())

for i in range(t):
    stack = []
    s = sys.stdin.readline().strip()
    try:
        [stack.append(_) if _ == '(' else stack.pop() for _ in s]
        if len(stack) == 0:
            print('YES')
        else:
            print('NO')
    except:
        print('NO')