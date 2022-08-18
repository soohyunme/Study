n, l = map(int, input().split())
arr = sorted(list(map(int, input().split())))
tmp = arr[0]
answer = 1
for x in arr[1:]:
    if x - tmp >= l:
        answer += 1
        tmp = x
print(answer)