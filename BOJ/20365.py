import sys
n = int(input())
s = input()

while 'BB' in s or 'RR' in s:
    s = s.replace('BB', 'B')
    s = s.replace('RR', 'R')
if len(s) == 1:
    print(1)
    sys.exit()
print(min(len(s.strip('R').split('R')), len(s.strip('B').split('B')))+1)