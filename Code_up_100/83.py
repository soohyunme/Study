r, g, b = map(int, input().split(' '))
rgb = int(r) * int(g) * int(b)

for red in range(r):
    for green in range(g):
        for blue in range(b):
            print(red, green, blue)
print(rgb)