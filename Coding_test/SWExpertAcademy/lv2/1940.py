for _ in range(1, int(input()) + 1):
    n = int(input())
    speed = answer = 0
    for i in range(n):
        command = input().split()
        if command[0] == '1':
            speed += int(command[1])
        elif command[0] == '2':
            speed -= speed if speed - int(command[1]) < 0 else int(command[1])
        answer += speed
    print('#'+str(_), answer)
