from itertools import product
n, m = map(int, input().split())
answer = product(range(1, n+1), repeat=m)

for i in answer:
    print(*i)
