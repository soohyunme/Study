w, h, b = map(int, input().split(' '))
bit = w * h * b / 8 / 1024 / 1024

print('{:.2f}'.format(bit), 'MB')

