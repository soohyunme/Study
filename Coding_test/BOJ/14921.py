import sys
n = int(input())
arr = list(map(int, input().split()))
arr.sort()
l = 0
r = len(arr) - 1
answer = sys.maxsize
while l != r:
    tmp = arr[l] + arr[r]
    if tmp == 0:
        answer = 0
        break
    elif tmp < 0:
        l += 1
    else:
        r -= 1
    answer = answer if abs(answer) < abs(tmp) else tmp
print(answer)



