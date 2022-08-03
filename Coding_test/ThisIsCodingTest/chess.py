n = input()

row = int(n[1])
column = ['', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h'].index(n[0][0])

dx = [-2, -2, 2, 2, -1, 1, -1, 1]
dy = [-1, 1, -1, 1, -2, -2, 2, 2]

result = 0
for i in range(1, 9):
    nx = row + dx[i - 1]
    ny = column + dy[i - 1]
    if nx < 1 or ny < 1 or nx > 9 or ny > 9:
        continue
    result += 1

print(result)

####################################################






