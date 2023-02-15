import sys
from collections import deque

def bfs():
    que = deque([1])
    while que:
        now =  que.popleft()            
        for point in link[now]:
            if not parent[point] and point != 1:
                parent[point] = now
                que.append(point)
            
N = int(sys.stdin.readline())
link = [ [] for i in range(N+1)]
parent = [0] * (N+1)

for i in range(N - 1):
    a, b = map(int, sys.stdin.readline().split())
    link[a].append(b)
    link[b].append(a)
    
bfs()
print(*parent[2:], sep='\n')