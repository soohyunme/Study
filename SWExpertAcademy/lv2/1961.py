for _ in range(1, int(input()) + 1):
    n = int(input())
    table = [list(map(int, input().split())) for __ in range(n)]
    print('#'+str(_))
    # 90도
    for j in range(n):
        print(''.join(map(str, [table[i][j] for i in range(n)][::-1])), end=' ')
        print(''.join(map(str, table[n-j-1][::-1])), end=' ')
        print(''.join(map(str, [table[i][n-j-1] for i in range(n)])))


