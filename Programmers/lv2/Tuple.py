def solution(s):
    _s = s.lstrip('{').rstrip('}').split('},{')
    arr = [list(map(int, i.split(','))) for i in _s]
    arr.sort(key=len)
    answer = []

    for i, sub in enumerate(arr):
        for j in sub:
            if j not in answer:
                answer.append(j)

    return answer