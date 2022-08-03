for _ in range(1, int(input()) + 1):
    n = int(input())
    arr = [50000, 10000, 5000, 1000, 500, 100, 50, 10]
    answer = []
    for i in arr:
        x, n = divmod(n, i)
        answer.append(x)
    print('#'+str(_))
    print(*answer)