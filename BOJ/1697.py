from collections import deque
import sys
n, k = map(int, input().split())
answer = [0] * 100001
q = deque([n])

if n == k:
    print(0)
    sys.exit()

while q:
    v = q.popleft()
    dx = [-1, 1, v]
    for i in range(3):
        nx = v + dx[i]
        if nx < 0 or nx > 100000 or (answer[nx] != 0 and answer[nx] < answer[v]+1):
            continue
        answer[nx] = answer[v]+1
        q.append(nx)
        if nx == k:
            print(answer[k])
            sys.exit()
print(answer[k])
