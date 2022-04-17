import sys
In = sys.stdin.readline

s = In().strip()
target = In().strip()
answer = 0
for i in range(len(s)):
    print(s[i:i+len(target)], target)
    if s[i:i+len(target)] == target:
        answer += 1
print(answer)
