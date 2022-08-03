n = int(input())
arr = list(map(int, input().split()))
total = sum(arr)
max_val = 0
tmp = arr[0]
for i in range(1, n-1):
    tmp += arr[i]
    max_val = max(total - arr[0] - arr[i] + total - tmp, max_val)
tmp = arr[-1]
for i in range(2, n+1):
    tmp += arr[-i]
    max_val = max(total - arr[-1] - arr[-i] + total - tmp, max_val)
for i in range(1, n-1):
    max_val = max(total - arr[0] - arr[-1] + arr[i], max_val)
print(max_val)

'''
# 부분 점수 코드
n = int(input())
arr = list(map(int, input().split()))
max_val = 0
for i in range(1, n):
    max_val = max(sum(arr[1:i]) + sum(arr[i+1:]) * 2, max_val)
for i in range(1, n):
    max_val = max(sum(arr[:-i-1]) * 2 + sum(arr[n-i:-1]), max_val)
for i in range(1, n-1):
    max_val = max(sum(arr[1:i+1]) + sum(arr[i:-1]), max_val)
print(max_val)
'''