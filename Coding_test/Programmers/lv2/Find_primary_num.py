from itertools import permutations
def solution(numbers):
    answer = 0
    arr = []
    for i in range(1, len(numbers)+1):
        arr.extend(permutations(numbers,i))
    arr2 = set(map(lambda x : int(''.join(x)),arr)) - set({0, 1})
    for i in arr2:
        for j in range(2,i):
            if i % j == 0:
                break
        else:
            answer += 1
    return answer


# set과 소수 공식을 통한 효율성 개선
from itertools import permutations
def solution(numbers):
    arr = set()
    for i in range(1, len(numbers)+1):
        arr |= set(map(lambda x : int(''.join(x)), permutations(numbers, i)))
    arr -= set(range(0,2))
    for i in range(2, int(max(arr) ** 0.5) + 1):
        arr -= set(range(i * 2, max(arr) + 1, i))
    return len(arr)
