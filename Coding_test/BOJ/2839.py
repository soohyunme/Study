n = int(input())
answer = -1
i = j = 0
for i in range(n//5+1):
    for j in range(n//3+1):
        weight = 5 * i + 3 * j
        if weight == n:
            answer = i + j

print(answer)
