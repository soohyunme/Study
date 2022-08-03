def GCD(num1, num2):
    if num2 == 0:
        return num1
    return GCD(num2, num1 % num2)

def solution(n, m):
    gcd = GCD(n, m)
    return [gcd, n * m / gcd]