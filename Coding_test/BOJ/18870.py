import sys
In = sys.stdin.readline

n = int(In())
array = list(map(int, In().split()))
array_c = array.copy()
array_c.sort()
nums = {}
count = 0
for i in range(n):
    if array_c[i] not in nums:
        nums.update({array_c[i]: count})
        count += 1

for i in range(n):
    print(nums[array[i]], end=' ')
