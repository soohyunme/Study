from collections import deque
n = int(input())
arr = deque(sorted(list(map(int, input().split()))))
while len(arr) >= 2:
    arr.append(arr.pop() + arr.popleft() / 2)
print(*arr)