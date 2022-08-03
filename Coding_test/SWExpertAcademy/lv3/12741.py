answer = []
for _ in range(1, int(input()) + 1):
    a, b, c, d = map(int, input().split())
    tmp = min(b, d) - max(a, c)
    answer.append(tmp)
for i, x in enumerate(answer):
    print('#'+str(i+1), 0 if x < 0 else x)
