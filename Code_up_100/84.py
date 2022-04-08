h, b, c, s = map(int, input().split(' '))
bit = h*b*c*s / 8 / 1024 / 1024

print(round(bit, 1), 'MB')


