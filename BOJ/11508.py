arr = [int(input()) for _ in range(int(input()))]
arr.sort(reverse=True)
answer = sum(x if (i+1)%3 != 0 else 0 for i, x in enumerate(arr))
print(answer)