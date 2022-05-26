for _ in range(1, int(input()) + 1):
    s = input().rstrip()
    print('#' + str(_), int(s == s[::-1]))