from collections import deque
n, k = map(int, input().split())
num = input()
answer = deque()
cnt = 0
for i in range(len(num)):
    while answer:
        if num[i] <= answer[-1] or cnt >= k:
            break
        answer.pop()
        cnt += 1
    answer.append(num[i])
for _ in range(cnt, k):
    answer.pop()
print(''.join(answer))

