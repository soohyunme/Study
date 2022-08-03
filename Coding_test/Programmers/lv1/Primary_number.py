from itertools import combinations
def solution(nums):
    array = [sum(i) for i in combinations(nums,3)]
    primary = [1]
    for i in range(1,max(array)+1):
        for j in range(2,i+1):
            if i == j:
                primary.append(i)
            elif i % j == 0:
                break
    return sum([1 for i in array if i in primary])