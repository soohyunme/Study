s = list(map(ord, input().upper()))
d = {}
for i in s:
    if i not in d:
        d[i] = 1
    else:
        d[i] += 1

max_val = 0
for idx, value in d.items():
    if max_val == value:
        answer = '?'
    if max_val < value:
        max_val = value
        answer = chr(idx)
print(answer)
