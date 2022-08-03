def solution(d, budget):
    answer = 0
    d.sort()
    for i in d:
        if i > budget:
            break
        budget -= i
        answer += 1
    return answer