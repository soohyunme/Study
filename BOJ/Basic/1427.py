n = input()
array = []
for i in n:
    array.append(int(i))
array.sort(reverse=True)
for i in array:
    print(i, end='')