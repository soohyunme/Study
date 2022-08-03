s = input()
stack = []
answer = ''
for x in s:
    if x.isalpha():
        answer += x
    elif x == '(':
        stack.append(x)
    elif x == ')':
        while stack:
            tmp = stack.pop()
            if tmp == '(':
                break
            answer += tmp
    elif x in ['*', '/']:
        while stack:
            if stack[-1] in ['*', '/']:
                answer += stack.pop()
                continue
            break
        stack.append(x)
    elif x in ['+', '-']:
        while stack:
            if stack[-1] == '(':
                break
            answer += stack.pop()
        stack.append(x)
while stack:
    answer += stack.pop()
print(answer + ''.join(stack[::-1]))


