for _ in range(1, int(input()) + 1):
    n = int(input())
    answer = ''
    for i in range(n):
        s, num = input().split()
        answer += s * int(num)
    print('#'+str(_))
    for i in range(len(answer)//10+1):
        print(answer[i*10:i*10+10])

