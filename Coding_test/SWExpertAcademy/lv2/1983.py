import math
score = ['A+', 'A0', 'A-', 'B+', 'B0', 'B-', 'C+', 'C0', 'C-', 'D0']
for _ in range(1, int(input()) + 1):
    n, k = map(int, input().split())
    total = []
    for i in range(n):
        mid, fin, ex = map(int, input().split())

        total.append(sum([mid*0.35, fin*0.45, ex*0.2]))
    target = total[k-1]
    total.sort()
    answer = 0

    while total:
        if total[0] == target:
            break
        total.pop(0)

    print('#' + str(_), score[math.ceil(len(total)/n*10)-1])
'''
75 95 98
#1 10 3 3 A-
#2 20 17 8 C0
#3 30 24 8 C0
#4 40 9 2 A0
#5 50 36 7 C+
#6 60 16 2 A0
#7 70 45 6 B-
#8 80 52 6 B-
#9 90 41 4 B+
#10 100 15 1 A+
'''