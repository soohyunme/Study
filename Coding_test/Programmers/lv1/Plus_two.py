from itertools import combinations
def solution(numbers):
    return sorted({sum(i) for i in combinations(numbers, 2)})