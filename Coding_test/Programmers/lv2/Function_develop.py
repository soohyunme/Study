from math import ceil


def solution(progresses, speeds):
    answer = []
    i = 0
    day = 0
    count = 0
    while i < len(progresses):
        need = ceil((100 - progresses[i]) / speeds[i])
        if day >= need:
            count += 1
        else:
            answer.append(count)
            day += need - day
            count = 1
        i += 1
    answer.append(count)

    return answer[1:]


# 좀 더 직관성 있는 코드

def solution(progresses, speeds):
    print(progresses)
    print(speeds)
    answer = []
    time = 0
    count = 0
    while len(progresses)> 0:
        if (progresses[0] + time*speeds[0]) >= 100:
            progresses.pop(0)
            speeds.pop(0)
            count += 1
        else:
            if count > 0:
                answer.append(count)
                count = 0
            time += 1
    answer.append(count)
    return answer