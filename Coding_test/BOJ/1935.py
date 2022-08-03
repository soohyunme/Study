n = int(input())
exp = input()
arr = [int(input()) for _ in range(n)]
op = ['+', '-', '*', '/']
arr_dict = dict(zip([chr(x) for x in range(ord('A'), ord('A') + n)], arr))
convert_exp = list(map(lambda x: x if x in op else arr_dict[x], exp))
ops = []
nums = []
for x in convert_exp:
    if x in op:
        n1 = nums.pop()
        n2 = nums.pop()
        if x == '+':
            nums.append(n2 + n1)
        if x == '-':
            nums.append(n2 - n1)
        if x == '*':
            nums.append(n2 * n1)
        if x == '/':
            nums.append(n2 / n1)
    else:
         nums.append(x)
print('{:.2f}'.format(nums[0]))
