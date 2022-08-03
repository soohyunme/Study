i, j, k = map(int, input().split())

num = 0

while True:
    num += 1
    if num % i == 0 and num % j == 0 and num % k == 0:
        break

print(num)

