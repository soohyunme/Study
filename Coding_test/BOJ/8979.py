n, k = map(int, input().split())
arr = sorted([list(map(int, input().split())) for _ in range(n)], key=lambda x: (x[1], x[2], x[3]), reverse=True)
tmp = []
answer = same = 0
for i in range(n):
    if tmp[1:] == arr[i][1:]:
        same += 1
    else:
        answer += same + 1
        same = 0
    if k == arr[i][0]:
        print(answer)
        break
    tmp = arr[i]

