for _ in range(1, int(input()) + 1):
    p, q, r, s, w = map(int, input().split())
    a = w * p
    b = q if w <= r else q + (w - r) * s
    print('#'+str(_), min(a, b))