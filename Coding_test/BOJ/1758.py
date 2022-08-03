n = int(input())
arr = [int(input()) for _ in range(n)]
arr.sort(reverse=True)
answer = 0
for i in range(n):
    answer += arr[i] - i if arr[i] - i > 0 else 0
print(answer)