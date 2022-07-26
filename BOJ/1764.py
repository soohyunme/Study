import sys
input = sys.stdin.readline
print = sys.stdout.write
n, m = map(int, input().split())
d = set(input() for _ in range(n))
b = set(input() for _ in range(m))
answer = sorted(list(d.intersection(b)))
print(str(len(answer))+'\n')
for x in answer:
    print(x)

