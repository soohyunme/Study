for _ in range(1, int(input()) + 1):
    arr = list(map(int, input().split()))
    arr.pop(arr.index(max(arr)))
    arr.pop(arr.index(min(arr)))
    print('#' + str(_), int(round(sum(arr)/len(arr))))
