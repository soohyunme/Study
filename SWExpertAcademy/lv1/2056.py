month = range(1, 13)
days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

for i in range(int(input())):
    s = input()
    y = s[:4]
    m = s[4:6]
    d = s[6:]
    if int(m) not in month or int(d) not in range(days[int(m)-1]+1) or not int(y):
        print('#'+str(i+1), str(-1))
        continue
    print('#'+str(i+1), y+'/'+m+'/'+d)
