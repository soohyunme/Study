stack = []
for _ in range(int(input())):
    n = int(input())
    if not n:
        stack.pop()
    else:
        stack.append(n)
print(sum(stack))