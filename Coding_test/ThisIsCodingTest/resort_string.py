s = input()
result = []
sum_ = 0

for i in s:
    if i.isalpha():
        result.append(i)
    else:
        sum_ += int(i)

result.sort()

if sum_ != 0:
    result.append(str(sum_))
print(''.join(result))

