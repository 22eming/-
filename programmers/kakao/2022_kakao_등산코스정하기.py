from collections import defaultdict
import heapq

def solution(n, paths, gates, summits, result):
    answer = []
    gates, summits= set(gates), set(summits)
    graph = defaultdict(dict)
    heap = []
    intensity = [float('inf')] * (n+1)
    
    for g in gates:
        heapq.heappush(heap, (0, g))
        intensity[g] = 0
        
    for path in paths:
        s, e, t = path
        if s in gates:
            graph[s][e] = t
        elif e in gates:
            graph[e][s] = t
        else:
            graph[s][e] = t
            graph[e][s] = t

    for summit in summits:
        if graph.get(summit):
            del(graph[summit])

    while heap:
        inten, loc = heapq.heappop(heap)
        if inten > intensity[loc]:
            continue
        for next_loc in graph[loc]:
            next_inten = graph[loc][next_loc]
            intens = max(inten, next_inten)
            if intensity[next_loc] > intens:
                intensity[next_loc] = intens
                heapq.heappush(heap, (intens, next_loc))
                
    for summit in summits:
        answer.append([intensity[summit], summit])
    return sorted(answer)[0][::-1]


data = [
    [6,	[[1, 2, 3], [2, 3, 5], [2, 4, 2], [2, 5, 4], [3, 4, 4], [4, 5, 3], [4, 6, 1], [5, 6, 1]],	[1, 3],	[5],	[5, 3]],
    [7,	[[1, 4, 4], [1, 6, 1], [1, 7, 3], [2, 5, 2], [3, 7, 4], [5, 6, 6]],	[1],	[2, 3, 4],	[3, 4]],
    [7,	[[1, 2, 5], [1, 4, 1], [2, 3, 1], [2, 6, 7], [4, 5, 1], [5, 6, 1], [6, 7, 1]],	[3, 7],	[1, 5],	[5, 1]],
    [5,	[[1, 3, 10], [1, 4, 20], [2, 3, 4], [2, 4, 6], [3, 5, 20], [4, 5, 6]],	[1, 2],	[5],	[5, 6]]
]
for d in data:
    print(solution(*d))