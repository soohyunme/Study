def solution(n):
    return [*map(int, str(n)[::-1])]

# 다른 풀이

def solution(n):
    return list(map(int, reversed(str(n))))
