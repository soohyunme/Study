import sys
In = sys.stdin.readline

n = int(In())
words = {}
for i in range(n):
    tmp = In().strip()
    words.update({tmp: len(tmp)})

word_list = list(zip(words.values(), words))
word_list.sort()
for l, word in word_list:
    print(word)


