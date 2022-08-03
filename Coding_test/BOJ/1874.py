import sys

n = int(sys.stdin.readline())
nums = []
for i in range(n):
    nums.append(int(sys.stdin.readline()))

array = []
count = 1
answer = []
for num in nums:
    if count <= num:
        array.extend(list(range(count, num + 1)))
        answer.append('+\n' * (num + 1 - count))
        count = num + 1
    if array[-1] == num:
        array.pop()
        answer.append('-\n')
    else:
        print('NO')
        exit()
sys.stdout.write(''.join(answer))
