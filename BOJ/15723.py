from collections import defaultdict
dic = defaultdict()
for _ in range(int(input())):
    a, b = input().split(' is ')
    dic[a] = b

for _ in range(int(input())):
    a, b = input().split(' is ')
    while a in dic:
        if dic[a] == b:
            print('T')
            break
        else:
            a = dic[a]
    else:
        print('F')
