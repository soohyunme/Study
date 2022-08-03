import sys
trees = {}
n = 0

for line in sys.stdin:
    if line == '\n':
        break
    n += 1
    name = line.strip()
    try:
        trees.update({name: trees[name]+1})
    except:
        trees.update({name: 1})
arr = zip(trees.keys(), trees.values())
for name, v in sorted(arr):
    print('%s %.4f' % (name, v/n*100))

