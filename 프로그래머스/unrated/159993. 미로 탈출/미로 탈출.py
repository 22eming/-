from collections import deque

def bfs(start, end, maps):
    max_y, max_x = len(maps), len(maps[0])
    visited = [[0]*len(maps[0]) for _ in range(len(maps))]
    que = deque([[start,0]])
    while que:
        q, cnt = que.popleft()
        y, x = q
        
        if end == [y,x]:
            return cnt
        
        if not visited[y][x]:
            visited[y][x] = 1
        else:
            continue
        
        for dy,dx in ([-1,0],[0,1],[1,0],[0,-1]):
            if  0<=y+dy<max_y and \
                0<=x+dx<max_x and \
                maps[y+dy][x+dx] != "X":
                que.append([[y+dy,x+dx], cnt+1])

    
def solution(maps):
    maps = [list(m) for m in maps]
    for y in range(len(maps)):
        for x in range(len(maps[0])):
            if maps[y][x] == "S":
                start = [y,x]
            elif maps[y][x] == "L":
                lever = [y,x]
            elif maps[y][x] == "E":
                end = [y,x]
    
    start2lever = bfs(start, lever, maps)
    lever2end = bfs(lever, end, maps)
    
    if start2lever == None or lever2end == None:
        return -1
    else:
        return start2lever + lever2end