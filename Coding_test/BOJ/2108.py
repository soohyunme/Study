import sys
from collections import Counter
In = sys.stdin.readline

n = int(In())
array = []
for i in range(n):
    array.append(int(In()))
array.sort()

nums = Counter(array).most_common()
print(int(round(sum(array) / n, 0)))
print(array[int(n/2)])
if len(nums) > 1:
    if nums[0][1] == nums[1][1]:
        print(nums[1][0])
    else:
        print(nums[0][0])
else:
    print(nums[0][0])
print(max(array)-min(array))
