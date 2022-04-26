def solution(s):
    nums = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']

    for i, c in enumerate(nums):
        s = s.replace(nums[i], str(i))

    return int(s)