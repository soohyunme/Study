n = int(input())
answer = 2001
for _ in range(n):
    a, b = map(int, input().split())
    if a < b:
        answer = min(answer, b)
    elif a == b:
        answer = min(answer, a)
    elif a < b:
        answer = min(answer, b)
print(answer if answer != 2001 else -1)
