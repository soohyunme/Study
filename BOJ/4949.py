while True:
    s = input()
    if s == '.':
        break
    stack = []
    for x in s:
        if x in ['(', '[']:
            stack.append(x)
        elif x == ')':
            if not stack or not stack.pop() == '(':
                print('no')
                break
        elif x == ']':
            if not stack or not stack.pop() == '[':
                print('no')
                break
    else:
        if not stack:
            print('yes')
        else:
            print('no')