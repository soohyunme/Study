import sys
n = int(sys.stdin.read())

time_list = [300, 60, 10]

array = []
for time in time_list:
    array.append(n // time)
    n %= time
if n != 0:
    print(-1)
else:
    [print(answer, end=' ') for answer in array]

