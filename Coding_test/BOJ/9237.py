import sys
In = sys.stdin.readline

n = In()
tree = list(map(int, In().split()))
tree.sort(reverse=True)

day = 1
answer = 0
for i in tree:
    day -= 1
    day = max(day, i)
    answer += 1
answer += day + 1
print(answer)
