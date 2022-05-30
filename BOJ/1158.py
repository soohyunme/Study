n, k = map(int, input().split())
arr = [x for x in range(1, n + 1)]
answer = []
idx = k - 1
while arr:
    if idx >= len(arr):
        idx %= len(arr)
    answer.append(arr[idx])
    arr.remove(arr[idx])
    idx += k - 1
print('<'+', '.join(map(lambda x: str(x), answer))+'>')