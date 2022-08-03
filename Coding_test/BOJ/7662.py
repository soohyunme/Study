import sys
import heapq
input = sys.stdin.readline

for T in range(int(input())):
    max_heap, min_heap = [], []
    visited = [False] * 1000001  # visited를 이용하여 해당 값이 힙에 존재하는지 표시
    for i in range(int(input())):
        s = input().split()
        c, num = s[0], int(s[1])
        if c == 'I':
            # heapq는 최소힙 따라서, -num을 이용해 최대 힙 구현
            heapq.heappush(max_heap, (-num, i))  # 최대 힙에 인덱스와 같이 추가
            heapq.heappush(min_heap, (num, i))  # 최소 힙에 인덱스와 같이 추가
            visited[i] = True  # 해당 인덱스를 방문처리 함
        elif num == 1:  # 최대 힙에서 꺼내기
            # 먼저 최대 힙을 조회하여 최소 힙에서 삭제된 항목이 있는지 조사
            # 최대 힙의 최대 값이 최소 힙에서 삭제된 항목이라면 최대 힙에서도 삭제
            # 즉, 최소힙과 최대힙을 동기화
            while max_heap and not visited[max_heap[0][1]]:
                heapq.heappop(max_heap)
            if max_heap:  # 이후 최대 힙에 값이 존재하면 최대값 pop
                visited[max_heap[0][1]] = False  # visited를 이용해 해당 값 삭제 표시
                heapq.heappop(max_heap)
        elif num == -1:  # 최소 힙에서 꺼내기
            while min_heap and not visited[min_heap[0][1]]:
                heapq.heappop(min_heap)
            if min_heap:
                visited[min_heap[0][1]] = False
                heapq.heappop(min_heap)

    # for문의 마지막 단계가 삭제라면 동기화가 되어있지 않으므로 동기화
    while max_heap and not visited[max_heap[0][1]]:
        heapq.heappop(max_heap)
    while min_heap and not visited[min_heap[0][1]]:
        heapq.heappop(min_heap)

    if max_heap:
        print(-max_heap[0][0], min_heap[0][0])
    else:
        print('EMPTY')

