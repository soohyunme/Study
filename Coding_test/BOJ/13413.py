import sys

In = sys.stdin.readline

t = int(In())

for _ in range(t):
    answer = 0
    n = int(In())
    init = list(In().strip())
    target = list(In().strip())
    if init.count('B') == target.count('B') and init.count('W') == target.count('W'):
        answer = int(sum([1 for i in range(len(target)) if target[i] != init[i]]) / 2)
    else:
        BW = sum([1 for i in range(len(target)) if init[i] == 'B' and target[i] == 'W'])
        WB = sum([1 for i in range(len(target)) if init[i] == 'W' and target[i] == 'B'])
        answer = max(BW, WB) - min(BW, WB) + round(min(BW, WB))
    print(answer)


