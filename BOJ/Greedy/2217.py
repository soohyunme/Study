n = int(input())

rope_list = []
for i in range(n):
    rope_list.append(int(input()))

rope_list.sort()
answer = rope_list[0] * n
for i in range(len(rope_list)-1):
    if rope_list[i] == rope_list[i+1]:
        continue
    tmp = rope_list[i + 1] * (n-(i+1))
    if answer < tmp:
        answer = tmp

print(answer)
