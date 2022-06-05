for _ in range(int(input())):
    n = int(input())
    cnt = 0
    arr = []
    s = []
    for __ in range(n//10+1):
        s.extend(map(int, input().split()))
    print(n//2 + 1 if n%2 else n//2)
    for x in s:
        cnt += 1
        arr.append(x)
        arr.sort()
        if cnt % 2 == 1:
            print(arr[int(cnt/2)], end=' ')
        elif cnt % 20 == 0:
            print()

