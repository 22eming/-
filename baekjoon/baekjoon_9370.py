# s지점 출발 #목저지 후보 중 하나에 도착 # 최단거리
# g, h 교차로 사이에 있는 도로 지나감
from collections import defaultdict
import heapq


def dijk(start):
    road_time = [int(1e9)]*(n+1)  # inf로하면 검증시 inf == inf 가 됨
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


# 출발점에서 h까지 최단거리 -> g에서 목적지까지 최단거리

# 출력 -> 도착까지 거리가 최단거리인 목적지 리스트
# 방법 dijkstra로 전체 최단거리 구하고 s->g->e or s->h->e 까지의 거리가 최단거리인 경우
