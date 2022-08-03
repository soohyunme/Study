n = int(input())
answer = 0
for i in range(1, n+1):
    j = i
    total = i
    while j >= 10:
        total += j % 10
        j //= 10
    total += j
    if total == n:
        answer = i
        break


print(answer)
