def solution(left, right):
    answer = 0
    for x in range(left, right+1):
        cnt = 0
        for k in range(1, x):
            cnt += 1 if not x % k else 0
        answer += x if cnt % 2 else -x
    return answer