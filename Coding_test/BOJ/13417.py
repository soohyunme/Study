import sys

In = sys.stdin.readline

n = int(In())

for i in range(n):
    _ = int(In())
    array = In().split()
    answer = ''
    for str_ in array:
        answer = min(answer+str_, str_+answer)
    print(answer)

