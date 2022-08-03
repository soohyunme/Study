n = int(input())

total = 0
answer = 1
while n >= total + answer:
    total += answer
    answer += 1
    print(total, answer)

print(answer-1)
