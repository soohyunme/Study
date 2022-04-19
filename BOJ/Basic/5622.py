s = input()
array = ['ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQRS', 'TUV', 'WXYZ']

answer = 0
for i in range(len(s)):
    for j in range(len(array)):
        if s[i] in array[j]:
            answer += (j+3)

print(answer)