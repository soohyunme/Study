n = int(input())
maps = [input() for _ in range(n)]
x = y = 0
for i in range(len(maps)):
    x += sum([1 for k in maps[i].split('X') if len(k) >= 2])
    y += sum(1 for k in ''.join([maps[j][i] for j in range(n)]).split('X') if len(k) >= 2)
print(x, y)