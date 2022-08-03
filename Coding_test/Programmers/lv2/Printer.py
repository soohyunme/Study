def solution(priorities, location):
    answer = 0
    while max(priorities) != -1:
        for i, num in enumerate(priorities):
            if num == max(priorities):
                priorities[i] = -1
                answer += 1
                if i == location:
                    return answer