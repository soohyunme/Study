import sys
n = int(input())
arr = list(map(int, input().split()))
arr.sort()
l = 0
r = n-1
mix = sys.maxsize
answer = [0, 0]
while l != r:
    if mix > abs(arr[l] + arr[r]):
        mix = abs(arr[l] + arr[r])
        answer = [arr[l], arr[r]]
    if arr[l] + arr[r] < 0:
        l += 1
    else:
        r -= 1
print(*answer)