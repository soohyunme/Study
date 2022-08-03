n = int(input())

w_list = list(map(int, input().split()))
x_list = list(map(int, input().split()))

w_list.sort()
x_list.sort(reverse=True)

answer = 0
for i in range(n):
    answer += w_list[i] * x_list[i]

print(answer)



