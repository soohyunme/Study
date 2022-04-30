def solution(participant, completion):
    participant.sort()
    completion.sort()
    for i in range(len(completion)):
        if participant[i] != completion[i]:
            return participant[i]
    return participant[-1]

# Counter를 이용한 풀이
from collections import Counter


def solution(participant, completion):
    answer = list(Counter(participant) - Counter(completion))[0]
    return answer
