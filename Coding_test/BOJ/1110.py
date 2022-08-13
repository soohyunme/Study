n = int(input())
ans = n
cnt = 0
while True:
    cnt += 1
    add = sum(map(lambda x: int(x), str(n)))
    n = int(str(n)[-1] + str(add)[-1])
    if ans == n:
        break
print(cnt)