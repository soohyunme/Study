def star(length):
    if length == 1:
        return ['*']

    stars = star(length//3)
    array = []
    for s in stars:
        array.append(s * 3)
    for s in stars:
        array.append(s + ' ' * (length // 3) + s)
    for s in stars:
        array.append(s * 3)
    return array


n = int(input())
print('\n'.join(star(n)))
