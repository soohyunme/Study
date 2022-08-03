h, w = map(int, input().split())
arr = list(map(int, input().split()))
top = answer = 0
stack = []
for x in arr:
    if x >= top:
        _min = min(top, x)
        while stack:
            answer += _min - stack.pop()
        top = x
    else:
        stack.append(x)
else:
    _top = area = cnt = 0
    while stack:
        x = stack.pop()
        if _top <= x:
            answer += area
            _top = x
            area = cnt = 0
        else:
            area += _top - x
            cnt += 1
    else:
        answer += area
print(answer)