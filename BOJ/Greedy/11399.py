n = int(input())

array = list(map(int, input().split()))

array.sort()

answer = 0
wait = 0
for i in array:
    answer = wait + i + answer
    wait += i

print(answer)

