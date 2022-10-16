from collections import deque

def bfs(y, x, team):
    d = [[-1, 0], [0,1], [1,0], [0,-1] ]
    que = deque([[y,x]])    
    cnt = 1
    while que:
        q = que.popleft()
        for yy, xx in d:
            dy, dx = q[0]+yy, q[1]+xx
            if dy < 0 or dy >= M or dx < 0 or dx >= N:
                continue
            if not visited[dy][dx] and war[dy][dx] == team:
                que.append([dy, dx])
                cnt += 1
                visited[dy][dx] = True
    return cnt**2
                

N, M = map(int, input().split())

war = [ list(input()) for _ in range(M) ]

visited = [[False]*N  for _ in range(M)]
blue, white = 0, 0
for y in range(M):
    for x in range(N):
        if not visited[y][x]:
            visited[y][x] = True
            if war[y][x] == "B":
                blue += bfs(y,x,'B')
            else:
                white += bfs(y, x, 'W')

print(white, blue)