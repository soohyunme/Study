def solution(price, money, count):
    total = sum([price * (i+1) for i in range(count)])
    return total - money if not total - money < 0 else 0