from collections import deque
n = int(input())
arr = deque(sorted(list(map(int, input().split()))))
answer = arr[-1]
if len(arr) % 2 == 1:
    arr.pop()
while len(arr) >= 2:
    answer = max(arr.pop() + arr.popleft(), answer)
print(answer)