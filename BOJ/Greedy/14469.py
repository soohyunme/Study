import sys

In = sys.stdin.readline

n = int(In())
in_time = []
spent_time = []
for i in range(n):
    come, spent = map(int, In().split())
    in_time.append(come)
    spent_time.append(spent)
array = list(zip(in_time, spent_time))
array.sort()

answer = 0
for come, spent in array:
    if answer <= come:
        answer = come + spent
    else:
        answer += spent
print(answer)

