def solution(prices):
    answer = [0 for i in range(len(prices))]
    for i in range(len(prices)):
        time = 0
        for j in range(i+1, len(prices)):
            time += 1
            if prices[j] < prices[i]:
                answer[i] = time
                break
        else:
            answer[i] = time
    return answer