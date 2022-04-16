import sys
In = sys.stdin.readline

n, l, k = map(int, In().split())

count_1 = 0
count_2 = 0
for i in range(n):
    sub1, sub2 = map(int, In().split())
    if sub2 <= l:
        count_1 += 1
        count_2 += 1
    elif sub1 <= l:
        count_1 += 1

answer = [k if count_1 > k else count_1][0] * 100 + [k if count_2 > k else count_2][0] * 40
print(answer)

