for _ in range(1, int(input()) + 1):
    s = input()
    answer = ''
    for i, x in enumerate(s):
        answer += x
        if len(set(s[:30-(30 % len(answer))].split(answer))) == 1:
            break
    print('#' + str(_), len(answer))