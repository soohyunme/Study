n = int(input())
road = [0] + list(map(int, input().split()))
gas = list(map(int, input().split()))
mm = max(gas)
length = 0
answer = 0
for i in range(n):
    length += road[i]
    if gas[i] < mm:
        answer += mm * length
        mm = gas[i]
        length = 0
answer += mm * length
print(answer)

# 다른 풀이
n = int(input())
dist = list(map(int, input().split()))
cost = list(map(int, input().split()))

answer = dist[0] * cost[0]
min_cost = cost[0]
for i in range(1, n-1):
    if min_cost > cost[i]:
        min_cost = cost[i]
    answer += min_cost * dist[i]
print(answer)