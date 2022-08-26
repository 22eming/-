from collections import deque
def solution(maps):
    visited = []
    way = [(0,1),(1,0),(-1,0),(0,-1)]
    q = deque([[0,0,1]])
    while q:
        x, y, answer = q.popleft()
        visited.append([x,y])
        for i in range(4):
            way_x, way_y = x + way[i][0], y + way[i][1]
            if way_x == len(maps[0])-1 and way_y == len(maps) -1:
                return answer + 1
            elif 0 <= way_x < len(maps[0]) and 0 <= way_y < len(maps) and maps[way_y][way_x] and [way_x,way_y] not in visited:
                q.append( [way_x,way_y,answer+1] )
    else:
        return -1

print(solution(	[[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,1],[0,0,0,0,1]] ))