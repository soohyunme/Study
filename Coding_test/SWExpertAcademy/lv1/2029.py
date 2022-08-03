for i in range(int(input())):
    a, b = map(int, input().split())
    print('#'+str(i+1), *divmod(a, b))
