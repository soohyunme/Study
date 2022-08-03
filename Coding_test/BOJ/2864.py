import sys
In = sys.stdin.readline

array = In().split()

max_answer = 0
min_answer = 0

for num in array:
    max_answer += max(int(num), int(num.replace('5', '6')))
    min_answer += min(int(num), int(num.replace('6', '5')))

print(min_answer, max_answer)

