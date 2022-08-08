def check(n):
    one_cnt = 0
    while n != 0:
        n, mod = divmod(n, 2)
        one_cnt += 1 if mod else 0
    return one_cnt


def solution(n):
    one_cnt = check(n)
    while True:
        n += 1
        if one_cnt == check(n):
            return n
