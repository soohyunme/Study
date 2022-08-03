s = input()

cro_list = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']

for cro_alpha in cro_list:
    s = s.replace(cro_alpha, '0')
print(len(s))

