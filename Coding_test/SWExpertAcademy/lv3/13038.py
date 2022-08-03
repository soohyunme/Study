for _ in range(1, int(input()) + 1):
    n = int(input())
    arr = list(map(int, input().split()))
    start_day = [i for i, x in enumerate(arr) if x]
    day = 10e+5 * 7
    for start_idx in start_day:
        cnt = 0
        tmp_day = 0
        start = False
        while cnt != n:
            for i, x in enumerate(arr):
                if i == start_idx:
                    start = True
                if not start:
                    continue
                if cnt == n:
                    break
                cnt += x
                tmp_day += 1
        day = min(day, tmp_day)
    print('#'+str(_), day)