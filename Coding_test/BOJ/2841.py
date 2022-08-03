import sys
n, p = map(int, input().split())
guitar = [[] for _ in range(6)]
answer = 0
last = 0
In = sys.stdin.readline
for _ in range(n):
    h, i = map(int, In().rstrip().split())
    now = 0
    if guitar[h-1] and i < guitar[h-1][-1]:
        while guitar[h-1] and guitar[h-1][-1] > i:
            now = guitar[h-1].pop()
            answer += 1
    if guitar[h-1] and guitar[h-1][-1] == i:
        continue
    guitar[h - 1].append(i)
    answer += 1
print(answer)
