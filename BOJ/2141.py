import sys
input = sys.stdin.readline
n = int(input())
arr = []
arr_sum = 0
for i in range(n):
    pos, people = list(map(int, input().split()))
    arr.append([pos, people])
    arr_sum += people
arr.sort()
tmp = 0
for i in range(n):
    tmp += arr[i][1]
    if tmp >= arr_sum / 2:
        print(arr[i][0])
        break

