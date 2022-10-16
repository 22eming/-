from collections import defaultdict
import heapq

def solution(n, paths, gates, summits):
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
            if intens < intensity[next_loc]:
                intensity[next_loc] = intens
                heapq.heappush(heap, (intens, next_loc))
                
    for summit in summits:
        answer.append([intensity[summit], summit])
        
    return sorted(answer)[0][::-1]