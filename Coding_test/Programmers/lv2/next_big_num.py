def one_cnt(n):
    cnt = 0
    while n != 0:
        n, div = divmod(n ,2)
        cnt += 1 if div else 0
    return cnt


def solution(n):
    answer = 0
    cnt = one_cnt(n)
    while True:
        n += 1
        if cnt == one_cnt(n):
            return n
