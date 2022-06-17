h1, m1, s1 = map(int, input().split(':'))
h2, m2, s2 = map(int, input().split(':'))
h = m = s = 0
if s2 - s1 < 0:
    m -= 1
    s += 60
s += s2 - s1
if m2 - m1 + m < 0:
    h -= 1
    m += 60
m += m2 - m1
if h2 - h1 + h < 0:
    h += 24
h += h2 - h1
print('{0:02d}:{1:02d}:{2:02d}'.format(h, m, s) if h or m or s else '24:00:00')
