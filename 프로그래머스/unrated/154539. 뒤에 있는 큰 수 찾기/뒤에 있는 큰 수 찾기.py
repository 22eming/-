from heapq import heappush, heappop

def solution(numbers):
    answer = [-1]*len(numbers)
    heap = []
    
    for idx, number in enumerate(numbers):
        heappush(heap, [number,idx])
        
        while heap[0][0] < number:
            answer[heappop(heap)[1]] = number
        
    return answer