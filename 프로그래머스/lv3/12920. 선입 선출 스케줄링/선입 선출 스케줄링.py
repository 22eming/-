import heapq

def solution(n, cores):
    heap = []
    for i in range(len(cores)):
        heapq.heappush(heap, [0, i])
    while n > 0 :
        h = heapq.heappop(heap)
        heapq.heappush(heap, [h[0]+cores[h[1]], h[1]])
        n -= 1

    return h[1]+1