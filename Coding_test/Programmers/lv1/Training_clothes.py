def solution(n, lost, reserve):
    have = [0] + [1 if i not in lost else 0 for i in range(1, n+1) ]
    for i, h in enumerate(have):
        if h == 0 and i in reserve:
            have[i] = 1
            reserve.remove(i)
    for index, h in enumerate(have):
        if h == 1 and (index in reserve):
            if index-1 in lost:
                have[index-1] = 1
                reserve.remove(index)
                lost.remove(index-1)
            elif index+1 in lost:
                have[index+1] = 1
                reserve.remove(index)
                lost.remove(index+1)

    return sum(have)

# set을 이용한 풀이
def solution(n, lost, reserve):
    _reserve = set(reserve) - set(lost)
    _lost = set(lost) - set(reserve)
    answer = set(reserve)
    for i in _reserve:
        f = i - 1
        b = i + 1
        if f in _lost:
            answer.add(f)
            _lost.remove(f)
        elif b in _lost:
            answer.add(b)
            _lost.remove(b)
    return n - len(_lost)