for _ in range(1, int(input()) + 1):
    n = int(input())
    print('#'+str(_), end=' ')
    nums = [2, 3, 5, 7, 11]
    for num in nums:
        cnt = 0
        while n % num == 0:
            n //= num
            cnt += 1
        print(cnt, end=' ')
    print()
