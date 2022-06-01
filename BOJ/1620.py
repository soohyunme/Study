import sys
n, m = map(int, sys.stdin.readline().rstrip().split())
arr = []
for _ in range(n):
    arr.append(sys.stdin.readline().rstrip())
pokey_dict = dict(zip(arr, range(1, n+1)))
pokey_digit_dict = {v: k for k, v in pokey_dict.items()}
for _ in range(m):
    s = sys.stdin.readline().rstrip()
    print(pokey_digit_dict[int(s)] if s.isdigit() else pokey_dict[s])
