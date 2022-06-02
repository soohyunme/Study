from collections import deque
n = int(input())
q = deque(zip(map(int, input().split()), range(1, n + 1)))
answer = []
rot = 0
while q:
    rot, idx = q.popleft()
    q.rotate(-(rot-1) if rot > 0 else -rot)
    answer.append(idx)

print(*answer)