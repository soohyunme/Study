for i in range(int(input())):
    arr = list(map(int, input().split()))
    print('#'+str(i+1), sum([x for x in arr if x % 2 == 1]))
