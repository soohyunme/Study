for _ in range(1, int(input()) + 1):
    n = int(input())
    nums = set()
    cnt = 0
    while len(nums) != 10:
        cnt += 1
        s = str(n * cnt)
        nums.update(s)
    print('#'+str(_), n*cnt)
