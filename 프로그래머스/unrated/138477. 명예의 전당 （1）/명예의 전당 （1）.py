import heapq
def solution(k, score):
    answer = []
    heap = []
    for i, s in enumerate(score):
        if i < k:
            heapq.heappush(heap, s)
        else:
            heapq.heappush(heap, s)
            min_honor = heapq.heappop(heap)
        answer.append(heap[0])
    return answer