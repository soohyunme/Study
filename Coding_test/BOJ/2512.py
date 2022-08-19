import sys
n = int(input())
arr = sorted(list(map(int, input().split())))
m = int(input())
length = len(arr)
if sum(arr) < m:
    print(max(arr))
else:
    for x in arr:
        if m <= x * length:
            print(m // length)
            sys.exit()
        else:
            length -= 1
            m -= x
