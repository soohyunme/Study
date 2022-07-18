from collections import deque
n, m = map(int, input().split())
arr = list(range(1, n+1))
pop_list = deque(list(map(int, input().split())))
q = deque(arr)
cnt = answer = 0
while pop_list and q:
    if q[0] == pop_list[0]:
        answer += min(cnt, len(q) - cnt)
        q.popleft()
        pop_list.popleft()
        cnt = 0
    else:
        q.rotate(-1)
        cnt += 1
print(answer)