def is_prime(num):
    for i in range(2, int(num**0.5)+1):
        if num % i == 0:
            return 0
    return 1

def solution(n):
    return sum(is_prime(i) for i in range(2, n+1))