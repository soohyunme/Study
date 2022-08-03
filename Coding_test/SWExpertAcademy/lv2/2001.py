for _ in range(1, int(input()) + 1):
    n, m = map(int, input().split())
    table = []
    answer = 0
    for i in range(n):
        table.append(list(map(int, input().split())))
    if n == m:
        print('#' + str(_), answer)
        continue
    for i in range(n-m+1):
        for j in range(len(table[0])-m+1):
            tmp = 0
            for k in range(i, i+m):
                tmp += sum(table[k][j:j+m])
            answer = max(answer, tmp)
    print('#' + str(_), answer)

'''
1
7 5
17 24 11 29 18 21 11
8 5 14 0 19 15 17
18 25 29 1 29 16 16
3 26 27 20 6 2 27
20 13 19 8 13 29 15
8 22 8 23 21 7 6
14 9 9 27 16 23 29
'''