n = int(input())
counter = 0

for i in range(n+1):
    if '3' in str(i):
        counter += 1

result = (1575 * (n + 1 - counter)) + (counter * 3600)

print(result)

####################################################

h = int(input())

count = 0
for i in range(h+1):
    for j in range(60):
        for k in range(60):
            if '3' in str(i) + str(j) + str(k):
                count += 1

print(count)