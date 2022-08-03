import sys
In = sys.stdin.readline

n = int(In())

for i in range(n):
    log_num = int(In())
    answer = 0
    log_list = list(map(int, In().split()))
    log_list.sort()
    array = [log_list[i] for i in range(len(log_list)) if i % 2 == 0]
    array.extend([log_list[i] for i in range(len(log_list)) if i % 2 != 0][::-1])
    answer = max(array[0]-array[-1], array[-1]-array[0])
    for k in range(len(array)-1):
        if answer < max(array[k]-array[k+1], array[k+1]-array[k]):
            answer = max(array[k]-array[k+1], array[k+1]-array[k])
    print(answer)

