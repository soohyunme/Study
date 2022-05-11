def solution(s):
    return ' '.join(map(lambda x : ''.join(c.upper() if i % 2 == 0 else c.lower() for i, c in enumerate(x)), s.split(' ')))