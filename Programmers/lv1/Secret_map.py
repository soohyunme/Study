def solution(n, arr1, arr2):
    _arr1 = [bin(x)[2:].zfill(n) for x in arr1]
    _arr2 = [bin(x)[2:].zfill(n) for x in arr2]
    return [''.join(['#' if int(a) or int(b) else ' ' for a, b in zip(i, j)]) for i, j in zip(_arr1,_arr2)]

# 효율성을 생각한 코드
def solution(n, arr1, arr2):
    answer = []
    for i in range(n):
        tmp = ''
        for j in str(bin(arr1[i] | arr2[i]))[2:].zfill(n):
            if j == '1':
                tmp += '#'
            else:
                tmp += ' '
        answer.append(tmp)
    return answer
