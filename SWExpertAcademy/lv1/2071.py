for i in range(int(input())):
    arr = list(map(int, input().split()))
    print('#'+str(i+1), int(round(sum([x for x in arr]) / len(arr), 0)))
