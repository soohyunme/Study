n = int(input())
n_list = list(map(int, input().split()))


for i in range(1, len(n_list)+1):
    print(n_list[-i], end=' ')
