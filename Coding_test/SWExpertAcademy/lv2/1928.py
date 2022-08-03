for _ in range(1, int(input()) + 1):
    s = input()
    arr = list(map(lambda x: chr(x), range(ord('A'), ord('Z')+1)))
    arr.extend(list(map(lambda x: chr(x), range(ord('a'), ord('z')+1))))
    arr.extend(list(map(lambda x: chr(x), range(ord('0'), ord('9') + 1))) + ['+', '/'])
    encoding = [arr.index(x) for x in s]
    decoding = [bin(x)[2:].zfill(6) for x in encoding]
    dec = ''.join(decoding)
    answer = ''
    for i in range(len(dec)//8):
        answer += chr(int(dec[i*8:(i+1)*8], 2))
    print('#'+str(_), answer)
