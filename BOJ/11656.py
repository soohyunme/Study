s = input()
arr = [s[i:] for i in range(len(s))]
[print(x) for x in sorted(arr)]
