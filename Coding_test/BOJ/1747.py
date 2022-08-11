n = max(int(input()), 2)
while True:
    if str(n)[::-1] == str(n):
        for k in range(2, n):
            if not n % k:
                break
        else:
            print(n)
            break
    n += 1


