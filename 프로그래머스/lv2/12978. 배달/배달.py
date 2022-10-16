from collections import deque

def solution(N, road, K):
    cost = [10e6]*(N+1)
    cost[1] = 0
    stack = deque([1])
    while stack:
        start = stack.popleft()
        for city_a, city_b, time in road:
            if city_a == start or city_b == start:
                arrive = city_b if city_a == start else city_a
                if cost[arrive] > cost[start]+time:
                    cost[arrive] = cost[start]+time
                    stack.append(arrive)
    return len([1 for i in cost if i <= K ])