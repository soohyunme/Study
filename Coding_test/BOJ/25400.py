n = int(input())
arr = list(map(int, input().split()))
idx = 1
answer = 0
for x in arr:
    if x == idx:
        idx += 1
    else:
        answer += 1
print(answer)