for _ in range(1, int(input()) + 1):
    n, m = map(int, input().split())
    arr1 = list(map(int, input().split()))
    arr2 = list(map(int, input().split()))

    # 긴 배열을 arr2로 고정
    if n > m:
        n, m = m, n
        arr1, arr2 = arr2, arr1
    answer = 0
    for i in range(m-n+1):
        tmp = 0
        for j in range(n):
            tmp += arr1[j] * arr2[i+j]
        answer = max(answer, tmp)
    print('#'+str(_), answer)