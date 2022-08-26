import heapq

def solution(scoville, K):
    answer = 0
    heapq.heapify(scoville)
    while scoville[0] <= K:
        if (scoville[0] + scoville[1]) < K and len(scoville) <= 2:
            return -1
        first = heapq.heappop(scoville)
        second = heapq.heappop(scoville)
        res = first + second*2
        heapq.heappush(scoville, res)
        answer += 1
    return answer