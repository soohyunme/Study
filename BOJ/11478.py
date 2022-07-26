from itertools import combinations
s = input()
ans = []
for i in range(len(s)):
    for j in range(i+1, len(s)+1):
        ans.append(s[i:j])
print(len(set(ans)))