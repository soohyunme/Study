# 첫 번째 코드 - 효율성 실패
def solution(s):
    string = ' '
    for i in range(len(s)):
        if string[-1] == s[i]:
            string = string[:-1]
        else:
            string += s[i]

    return 1 if len(string) == 1 else 0

# 스택 사용 수정 코드
def solution(s):
    stack = [s[0]]
    for v in s[1:]:
        if stack and stack[-1] == v:
            stack.pop()
        else:
            stack.append(v)
    return 0 if stack else 1