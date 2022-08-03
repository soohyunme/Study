import sys
n = int(input())
arr = list(map(int, input().split()))[::-1]
stack = []
answer = []
for x in arr:
    while stack:
        if stack[-1] > x:
            answer.append(stack[-1])
            break
        else:
            stack.pop()
    else:
        answer.append(-1)
    stack.append(x)
print(*answer[::-1])