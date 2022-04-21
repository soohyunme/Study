n = int(input())

answer = []
i = 0
while True:
    if len(answer) == n:
        break
    if '666' in str(i):
        answer.append(i)
    i += 1
print(answer[-1])

