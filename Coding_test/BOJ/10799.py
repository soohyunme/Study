s = input().replace('()', 's')
sticks = []
answer = 0
for x in s:
    if x == 's':
        answer += len(sticks)
    elif x == '(':
        sticks.append(0)
    else:
        answer += 1
        sticks.pop()
print(answer)