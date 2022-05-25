for i in range(int(input())):
    a, b = map(int, input().split())
    print('#'+str(i+1), '>' if a > b else '=' if a == b else '<')
