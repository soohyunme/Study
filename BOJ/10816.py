from collections import Counter
import sys
input = sys.stdin.readline
n = int(input())
arr1 = list(map(int, input().split()))
c = Counter(arr1)
m = int(input())
arr2 = list(map(lambda x: c[x], list(map(int, input().split()))))
print(*arr2)
