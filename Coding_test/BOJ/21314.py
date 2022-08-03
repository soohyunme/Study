s = input()
tmp = 0
minimum = ''
maximum = ''
for x in s:
    if x == 'M':
        tmp += 1
    else:
        maximum += str(10**tmp * 5 if tmp else 5)
        minimum += str(10**tmp + 5 if tmp else 5)
        tmp = 0
minimum += str(10**(tmp-1)) if tmp else ''
maximum += '1'*tmp if tmp else ''

print(maximum)
print(minimum)