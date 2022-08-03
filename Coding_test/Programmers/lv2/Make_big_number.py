def solution(number, k):
    arr = list(number)
    answer = list(arr[0])
    for i in range(1, len(arr)):
        if not k:
            answer.extend(arr[i:])
            break
        if int(arr[i]) > int(answer[-1]):
            k -= 1
            answer.pop()
            while answer:
                if not k:
                    break
                if int(answer[-1]) >= int(arr[i]):
                    break
                else:
                    answer.pop()
                    k -= 1
        answer.append(arr[i])
    if k:
        answer = answer[:-k]
    return ''.join(answer)