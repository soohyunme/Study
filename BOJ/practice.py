# 입력 나누어 받기
a, b = map(int, input().split())

# 입출력 가속
import sys

In = sys.stdin.readline
Out = sys.stdout.write

# 배열 입력
MAP = [list(map(int, input().split())) for _ in range(int(input()))]

# 정수, 배열 입력
n, *arr = map(int, input().split())

# 문자열을 한 글자씩 배열에 저장
# input = 3 \n AAAA \n BBBB \n CCCC
arr = [list(input()) for _ in range(n)]

배열 출력 (Custom)
arr = [1, 2, 3, 4]
arr = [1, 2, 3, 4]
print(''.join(map(str, arr)))

# 배열 출력 2 (공백 구분)
print(*arr)

# DFS에서 재귀 오류 시
import sys
sys.setrecursionlimit(15000)
