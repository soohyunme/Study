from itertools import permutations
n, m = map(int, input().split())
answer = permutations(range(1, n+1), m)

for i in answer:
    print(*i)
