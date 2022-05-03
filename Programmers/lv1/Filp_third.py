def solution(n):
    third = ''
    while n:
        third += str(n % 3)
        n //= 3
    return int(third, 3)
