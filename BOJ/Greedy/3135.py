start, target = map(int, input().split())
n = int(input())
star = []
for i in range(n):
    star.append(int(input()))

answer = max(start, target) - min(start, target)

for idx in range(len(star)):
    btn = idx + 1
    star_diff = max(star[idx], target) - min(star[idx], target) + 1
    if star_diff < answer:
        answer = star_diff

print(answer)

