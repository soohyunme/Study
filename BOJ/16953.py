import sys
a, b = map(int, input().split())
answer = 0
while b != 1 and a != b:
    b1 = b2 = sys.maxsize
    if str(b)[-1] == '1':
        b1 = int(str(b)[:-1])
    if b % 2 == 0:
        b2 = b // 2
    if b1 == b2 == sys.maxsize:
        break
    b = min(b1, b2)
    answer += 1
print(answer + 1 if a == b else -1)

