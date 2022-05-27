for _ in range(1, int(input())+1):
    h1, m1, h2, m2 = map(int, input().split())
    h = h1 + h2
    m = m1 + m2
    if m >= 60:
        m -= 60
        h += 1
    h = h-12 if h >= 13 else h
    print('#'+str(_), h % 13 if h % 13 else 1, m)