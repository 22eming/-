from collections import defaultdict, deque
N, M, V = map(int, input().split())

graph = defaultdict(list)
for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

def dfs():
    answer = []
    stack = [V]
    visited = set()
    while stack:
        s = stack.pop()
        if s not in visited:
            answer.append(s)
            visited.add(s)
            stack.extend(sorted(graph[s], reverse=True))
    return answer

def bfs():
    answer = []
    visited = set()
    que = deque([V])
    while que:
        q = que.popleft()
        if q not in visited:
            answer.append(q)
            visited.add(q)
            que.extend(sorted(graph[q]))
    return answer

print( ' '.join( map(str, dfs())) )
print( ' '.join( map(str, bfs())) )