from collections import deque

def bfs(maps, start, visited):
    """_summary_

    Args:
        maps (list): 전체 무인도의 식량 지도
        start (int): 시작 index [y,x]
        visited (list): 방문했던 무인도 

    Returns:
        int: 최대 머물 수 있는 날짜
        list: 지금까지 들른 위치
    """
    que = deque([start])
    max_y, max_x = len(maps), len(maps[0])
    answer = 0

    while que:
        y,x = que.popleft()
        if not visited[y][x]:
            answer += int(maps[y][x])
            visited[y][x] = 1
            for dy, dx in [[-1,0],[0,1],[1,0],[0,-1]]:
                if 0<=y+dy<max_y and 0<=x+dx<max_x and maps[y+dy][x+dx] !="X":
                    que.append([y+dy,x+dx])
                    
    return answer, visited   
    
def solution(maps):
    answer = []
    maps = [list(m) for m in maps]
    visited = [[0]*len(maps[0]) for _ in range(len(maps))]

    for y in range(len(maps)):
        for x in range(len(maps[0])):
            if not visited[y][x] and maps[y][x] != 'X':
                ans, visited = bfs(maps, [y,x], visited)
                answer.append(ans)
        
    if answer == []:
        return [-1]
    else:
        return sorted(answer)