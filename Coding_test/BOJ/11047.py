n, k = list(map(int, input().split()))

array = []
for i in range(n):
    array.append(int(input()))

array.sort(reverse=True)

count = 0
for i in array:
    count += k // i
    k %= i

print(count)


