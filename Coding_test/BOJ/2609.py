a, b = map(int, input().split())

mul = 0
for i in range(1, max(a, b)+1):
    if a % i == 0 and b % i == 0:
       mul = i
div = int(a * b / mul)
print(div)
