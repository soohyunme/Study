import re
def solution(dartResult):
    numbers = re.findall(r'\d+', dartResult)
    string = re.findall(r'[S,D,T,*,#]',dartResult)
    answer = [0] + list(map(int, numbers))
    count = 0
    for s in string:
        count += 1
        if s == 'D':
            answer[count] **= 2
        elif s == 'T':
            answer[count] **= 3
        elif s == '*':
            count -= 1
            answer[count-1] *= 2
            answer[count] *= 2
        elif s == '#':
            count -= 1
            answer[count] *= -1
    return sum(answer)