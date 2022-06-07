import sys
n = int(input())
answer = sys.maxsize
for i in range(n//5 + 1):
    v, mod = divmod((n - i * 5), 2)
    if not mod:
        answer = min(i + v, answer)
print(answer if not answer == sys.maxsize else -1)