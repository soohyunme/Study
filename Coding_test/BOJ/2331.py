A, P = map(int, input().split())
arr = [A]
while True:
    tmp = 0
    for x in str(arr[-1]):
        tmp += int(x)**P
    if tmp in arr:
        break
    arr.append(tmp)
print(len(arr[:arr.index(tmp)]))