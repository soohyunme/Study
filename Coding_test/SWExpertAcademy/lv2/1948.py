for _ in range(1, int(input()) + 1):
    m1, d1, m2, d2 = map(int, input().split())
    month = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
    days = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    answer = 0
    while m1 != m2:
        answer += days[m1] - d1 + 1
        d1 = 1
        m1 += 1 if m1 != 12 else - 11
    answer += d2 - d1 + 1
    print('#'+str(_), answer)


