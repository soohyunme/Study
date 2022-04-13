array = input().split('-')
nums = []

for i in array:
    tmp = 0
    s = i.split('+')
    for j in s:
        tmp += int(j)
    nums.append(tmp)
answer = nums[0]
for i in range(1, len(nums)):
    answer -= nums[i]

print(answer)

