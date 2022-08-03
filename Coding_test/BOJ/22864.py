a, b, c, m = map(int, input().split())
h = 24
power = answer = 0
while h > 0:
    h -= 1
    if power + a > m:
        power = max(power-c, 0)
    else:
        power += a
        answer += b
print(answer)