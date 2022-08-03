def hanoi(length, a, b, c):
    if length == 1:
        return [f'{a} {c}']
    else:
        array = hanoi(length - 1, a, c, b)
        array.append(f'{a} {c}')
        array.extend(hanoi(length - 1, b, a, c))
        return array
    array = hanoi(length-1, a, b, c)
    return array


n = int(input())
tower = hanoi(n, 1, 2, 3)
print(len(tower))
for i in tower:
    print(i)

