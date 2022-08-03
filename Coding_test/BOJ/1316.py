n = int(input())

answer = 0
for i in range(n):
    word = input()
    group = ''
    for j in range(len(word)):
        if word[j] not in group:
            group += word[j]
        elif word[j] != group[-1]:
            break
        if j == len(word)-1:
            answer += 1
print(answer)
