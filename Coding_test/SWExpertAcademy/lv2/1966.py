for _ in range(1, int(input()) + 1):
    __ = input()
    arr = map(int, input().split())
    print('#'+str(_), *sorted(arr))