def solution(answers):
    answer = []
    count = [0] * 3
    pattern1 = [1, 2, 3, 4, 5]
    pattern2 = [2, 1, 2, 3, 2, 4, 2, 5]
    pattern3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    for index, num in enumerate(answers):
        if num == pattern1[index % len(pattern1)]:
            count[0] += 1
        if num == pattern2[index % len(pattern2)]:
            count[1] += 1
        if num == pattern3[index % len(pattern3)]:
            count[2] += 1

    for index, num in enumerate(count):
        if num == max(count):
            answer.append(index + 1)
    return answer
