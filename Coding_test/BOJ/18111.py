# pypy3 정답 코드 - python3의 경우 시간초과
import sys
n, m, b = map(int, sys.stdin.readline().split())
arr = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
answer = (sys.maxsize, 0)
for h in range(min(min(arr)), max(max(arr)) + 1):
    dig, stack = 0, 0
    for x in range(n):
        for y in range(m):
            if arr[x][y] >= h:
                dig += arr[x][y] - h
            else:
                stack += h - arr[x][y]
    if b + dig >= stack:
        if answer[0] >= dig * 2 + stack:
            answer = (min(answer[0], dig * 2 + stack), h)
print(*answer)