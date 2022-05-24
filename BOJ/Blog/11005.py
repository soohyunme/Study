n, b = map(int, input().split())
answer = ''

while n:
    n, mod = divmod(n, b)
    answer += str(mod) if mod < 10 else chr(ord('A') - 10 + mod)
print(answer[::-1])

# 더 효율적인 방법
n, b = map(int, input().split(' '))
t = []
while n:
    t.append(n % b)
    n //= b
t.reverse()
l = ''.join(chr(i - 10 + ord('A')) if i >= 10 else str(i) for i in t)
print(l)
