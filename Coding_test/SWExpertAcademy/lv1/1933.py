n = int(input())
print(*[x for x in range(1, n+1) if n % x == 0])
