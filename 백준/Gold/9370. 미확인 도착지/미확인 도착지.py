from collections import defaultdict
import heapq

def dijk(start):
    road_time = [int(1e9)]*(n+1)
    road_time[start] = 0
    heap = []
    heapq.heappush(heap, (0, start))
    while heap:
        dist, now_loc = heapq.heappop(heap)
        if road_time[now_loc] < dist:
            continue

        for key, val in road[now_loc].items():
            temp_dist = val + dist
            if road_time[key] > temp_dist:
                road_time[key] = temp_dist
                heapq.heappush(heap, (temp_dist, key))

    return road_time


T = int(input())
for _ in range(T):
    answer = []
    n, m, t = map(int, input().split())  # n=교차로. m=도로, t=목적지후보개수
    s, g, h = map(int, input().split())  # s=출발지, g,h

    road = defaultdict(dict)
    for _ in range(m):
        a, b, d = map(int, input().split())
        road[a][b] = d
        road[b][a] = d

    candi = [int(input()) for _ in range(t)]

    road_time_s = dijk(s)
    road_time_g = dijk(g)
    road_time_h = dijk(h)

    for c in candi:
        if road_time_s[c] == road_time_s[g] + road[g][h] + road_time_h[c]:
            answer.append(c)
        elif road_time_s[c] == road_time_s[h] + road[h][g] + road_time_g[c]:
            answer.append(c)

    print(*sorted(answer))