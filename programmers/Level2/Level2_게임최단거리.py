from collections import deque
def vis(N,M,y,x,maps):
    return 0 <= y < N and 0 <= x < M and maps[y][x] == 1

def solution(maps):
    
    N, M, Y, X, cnt = len(maps), len(maps[0]), 0, 1, 2
    q, visit = deque([ (0,0,1) ]), set((0,0,1))
    way = ( (0,1), (1,0), (0,-1), (-1,0) )

    while q:
        now = q.popleft()
        maps[now[Y]][now[X]] = 0

        if now[Y] == N-1 and now[X] == M-1:
            return now[cnt]

        for dx, dy in way:
            next_p = ( now[Y]+dy, now[X]+dx, now[cnt]+1 )
            if vis(N,M, next_p[Y], next_p[X], maps) and next_p not in visit:
                q.append(next_p)
                visit.add(next_p)
            
    return -1
print(solution([[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,1],[0,0,0,0,1]]))
