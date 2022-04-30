def solution(array, commands):
    answer = []
    for i, j, k in commands:
        tmp = array[i-1:j]
        tmp.sort()
        answer.append(tmp[k-1])
    return answer

# lambda 쓰기
def solution(array, commands):
    return list(map(lambda x: sorted(array[x[0]-1:x[1]])[x[2]-1], commands))
