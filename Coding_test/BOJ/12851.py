from collections import deque
import sys
n, k = map(int, input().split())
if n == k:
    print('0'+'\n'+'1')
    sys.exit()
q = deque()
q.append((n, 0))
answer = []
visit = [0 for _ in range(100001)]
while q:
    x, cnt = q.popleft()
    if x == k:
        answer.append(cnt)
        continue
    for nx in [x - 1, x + 1, 2 * x]:
        if 0 <= nx <= 100000 and (not visit[nx] or visit[nx] >= visit[x] + 1):
            visit[nx] = cnt + 1
            q.append((nx, cnt + 1))
print(answer[0])
print(len(answer))