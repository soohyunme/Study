arr = sorted(tuple(map(int, input().split())) for _ in range(int(input())))
start = 24
end = 0
answer = 0
for s, e in arr:
    if s < end and e <= end:
        end = e
    elif s >= end:
        answer += 1
        start = s
        end = e
print(answer)
