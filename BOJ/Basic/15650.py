from itertools import combinations
n, m = map(int, input().split())
answer = combinations(range(1, n+1), m)

for i in answer:
    print(*i)

