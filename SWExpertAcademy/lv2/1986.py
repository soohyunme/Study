for _ in range(1, int(input()) + 1):
    n = int(input())
    answer = sum(x if x % 2 == 1 else -x for x in range(1, n+1))
    print('#' + str(_), answer)