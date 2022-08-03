n = int(input())
nums = int(input())
answer = 0
for i in range(n):
    answer += nums % 10
    nums //= 10
print(answer)