for _ in range(1, int(input()) + 1):
    n = int(input())
    arr = list(map(int, input().split()))
    arr.reverse()
    tmp = arr[0]
    answer = 0
    for i, x in enumerate(arr):
        if x < tmp:
            answer += tmp - x
        else:
            tmp = x
    print('#'+str(_), answer)