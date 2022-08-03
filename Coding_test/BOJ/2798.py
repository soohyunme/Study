n, target = map(int, input().split())

array = list(map(int, input().split()))
array.sort()
answer = 0
for i in range(len(array)):
    for j in range(i+1, len(array)):
        for k in range(j+1, len(array)):
            tmp = max(answer, array[i] + array[j] + array[k])
            if tmp <= target:
                answer = tmp

print(answer)

