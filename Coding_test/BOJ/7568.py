n = int(input())

array = []
answer = []
for i in range(n):
    weight, height = map(int, input().split())
    array.append((weight, height))
for w, h in array:
    count = 1
    for w_, h_ in array:
        if w_ > w and h_ > h:
            count += 1
    answer.append(count)

print(*answer)

