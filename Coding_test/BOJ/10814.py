import sys
In = sys.stdin.readline

n = int(In())

user = []
for i in range(n):
    age, name = In().split()
    user.append((int(age), i,  name))
user.sort()
for i in range(n):
    print(user[i][0], user[i][2])

