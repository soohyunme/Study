for _ in range(1, int(input())+1):
    __ = int(input())
    arr = list(map(lambda x: -int(x) if x[0] == '-' else int(x), input().split()))
    print('#'+str(_), min(arr), arr.count(min(arr)))