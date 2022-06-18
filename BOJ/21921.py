import sys
n, x = map(int, input().split())
arr = list(map(int, input().split()))
answer = sum(arr[:x])
tmp = sum(arr[:x])
cnt = 1
for i in range(n-x):
    tmp = tmp - arr[i] + arr[i+x]
    if answer < tmp:
        answer = tmp
        cnt = 1
    elif answer == tmp:
        cnt += 1
if answer == 0:
    print('SAD')
else:
    print(answer)
    print(cnt)