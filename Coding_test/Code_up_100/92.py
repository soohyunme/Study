from collections import Counter

n = int(input())
n_list = list(map(int, input().split()))

counter = Counter(n_list)


for i in range(1, 24):
    print(counter[i], end=' ')
