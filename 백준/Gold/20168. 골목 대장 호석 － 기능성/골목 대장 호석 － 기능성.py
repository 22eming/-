N, M, A, B, C = map(int, input().split())
graph = {i: {} for i in range(1, N + 1)}
for i in range(M):
    s, e, cost = map(int, input().split())
    graph[s].update({e: cost})
    graph[e].update({s: cost})


def dfs(s, visited, max_cost, now_cost):
    if s == B:
        return max_cost
    answer = float("inf")
    for key, cost in graph[s].items():
        if key not in visited and now_cost + cost <= C:
            answer = min(
                answer, dfs(key, visited + [key], max(max_cost, cost), now_cost + cost)
            )
    return answer


print(dfs(A, [A], 0, 0))
