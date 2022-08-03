def solution(n):
    return sum(int(i) for i in str(n))

# 다른 풀이

def solution(n):
    return sum(map(int, str(n)))