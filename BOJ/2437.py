n = int(input())
arr = sorted(list(map(int, input().split())))
answer = 0
for x in arr:
    if answer + 1 < x:
        break
    answer += x
print(answer + 1)