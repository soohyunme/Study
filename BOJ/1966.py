from collections import deque
for _ in range(int(input())):
    n, m = map(int, input().split())
    q = deque(zip(list(map(int, input().split())), range(n)))
    answer = 1
    while q:
        if max(map(lambda x: x[0], q)) > q[0][0]:
            q.rotate(-1)
        elif q[0][1] == m:
            print(answer)
            break
        else:
            q.popleft()
            answer += 1

