n = int(input())
arr1 = set(map(int, input().split()))
m = int(input())
arr2 = list(map(int, input().split()))
answer = []
for x in arr2:
    answer.append(1 if x in arr1 else 0)
print(*answer)
