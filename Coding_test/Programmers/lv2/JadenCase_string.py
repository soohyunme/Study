def solution(s):
    ans = ''
    for i, x in enumerate(s):
        ans += str.lower(x) if s[i-1] != ' ' and i != 0 else str.upper(x)
    return ans