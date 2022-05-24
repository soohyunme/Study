b, n = input().split()
t = []
for x in reversed(b):
    t.append(int(x) if x.isdigit() else ord(x) - 55)
print(sum((x * (int(n) ** i)) for i, x in enumerate(t)))

# 다른 코드
b, n = input().split()
print(int(b, int(n)))