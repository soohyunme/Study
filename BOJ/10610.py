s = ''.join(sorted(input(), reverse=True))
answer = -1
if s[-1] == '0' and int(s[:-1]) % 3 == 0:
    answer = int(s)
print(answer)