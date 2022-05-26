for _ in range(1, int(input()) + 1):
    n = int(input())
    print('#' + str(_))
    arr = []
    for i in range(1, n+1):
        if i < 3:
            arr = ([1] * i)
        else:
            arr = [1] + [x+arr[j+1] if j < len(arr)-1 else 1 for j, x in enumerate(arr)]
        print(*arr)

