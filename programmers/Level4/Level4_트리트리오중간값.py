from collections import defaultdict, deque


def dfs(node, edge):
    visit = {node}
    dist = {node: 0}
    max_node = [0, node]
    que = deque([node])
    while que:
        q = que.popleft()
        for i in edge[q]:
            if i not in visit:
                visit.add(i)
                que.append(i)
                dist[i] = dist[q] + 1
                if dist[i] >= max_node[0]:
                    if dist[i] == max_node[0]:
                        max_node.append(i)
                    else:
                        max_node = [dist[i], i]

    return max_node


def solution(n, edges):
    edge = defaultdict(list)
    for p, c in edges:
        edge[p].append(c)
        edge[c].append(p)

    max_dist = dfs(1, edge)
    max_dist = dfs(max_dist[1], edge)
    if len(max_dist) > 2:
        return max_dist[0]

    max_dist = dfs(max_dist[1], edge)
    if len(max_dist) > 2:
        return max_dist[0]
    else:
        return max_dist[0]-1


print(solution(5,	[[1, 5], [2, 5], [3, 5], [4, 5]]))

# 임의의 노드 1로부터 가장 먼 노드 A를 찾는다.
# A로부터 각 노드까지의 거리를 찾는다
# 이 때 가장 먼 거리의 노드가 여러개라면 A노드와 먼 노드 중 2개를 선택하면 되므로 가장 먼 거리 리턴
# 가장 먼 거리의 노드가 B 하나라면 다시 B 를 기준으로 탐색
# B로부터 각 노드까지의 거리를 찾는다
# 이 때 역시 가장 먼 거리의 노드가 여러개라면 B노드와 먼 노드 중 2개를 선택하면 되므로 가장 먼 거리 리턴
# 가장 먼 거리의 노드가 A 하나라면 A와 B의 거리(트리의 지름)-1을 리턴
