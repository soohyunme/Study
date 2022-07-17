n = int(input())
arr = sorted(list(map(int, input().split())))
x = int(input())
i = answer = 0
j = len(arr) - 1
while i < j:
    if arr[i] + arr[j] == x:
        answer += 1
        i += 1
        j -= 1
    elif arr[i] + arr[j] < x:
        i += 1
    else:
        j -= 1
print(answer)