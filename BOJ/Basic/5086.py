import sys
In = sys.stdin.readline

while True:
    n, m = map(int, In().split())
    if n + m == 0:
        break
    if m % n == 0:
        print('factor')
    elif n % m == 0:
        print('multiple')
    else:
        print('neither')
