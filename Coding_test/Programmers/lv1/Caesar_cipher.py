def solution(s, n):
    answer = ''
    for i in s:
        if i == ' ':
            answer += ' '
        elif i >= 'A' and i <= 'Z':
            j = ord(i)+n
            if j < ord('A') or j > ord('Z'):
                j -= 26
            answer += chr(j)
        elif i >= 'a' and i <= 'z':
            j = ord(i)+n
            if j < ord('a') or j > ord('z'):
                j -= 26
            answer += chr(j)
    return answer