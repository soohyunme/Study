s = input()

array = [s[0]]
for i in range(1, len(s)):
    if s[i-1] != s[i]:
        array.append(s[i])
print(min(array.count('0'), array.count('1')))

