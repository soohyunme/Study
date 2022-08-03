from collections import Counter
for _ in range(1, int(input()) + 1):
    n = int(input())
    arr = list(map(int, input().split()))
    print('#'+str(n), Counter(arr).most_common(1)[0][0])