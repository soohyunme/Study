for _ in range(1, int(input()) + 1):
    n, k = map(int, input().split())
    table = [list(map(int, input().split())) for _ in range(n)]
    answer = 0

    # row 찾기
    for i in range(n):
        arr = ''.join(str(x) for x in table[i]).split('0')
        if '1' * k in arr:
            answer += arr.count('1'*k)

    # column 찾기
    for j in range(n):
        arr = []
        for i in range(n):
            arr += str(table[i][j])
        arr = ''.join(str(x) for x in arr).split('0')
        if '1' * k in arr:
            answer += arr.count('1'*k)

    print('#'+str(_), answer)