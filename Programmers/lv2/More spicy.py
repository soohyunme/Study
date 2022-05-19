import heapq
def solution(scoville, K):
    heapq.heapify(scoville)
    answer = 0
    while len(scoville) > 1:
        if scoville[0] >= K:
            break
        answer += 1
        mix = heapq.heappop(scoville) + (heapq.heappop(scoville) * 2)
        heapq.heappush(scoville, mix)
    return answer if min(scoville) >= K else -1