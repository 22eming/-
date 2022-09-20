# 문제
# 전쟁은 어느덧 전면전이 시작되었다. 결국 전투는 난전이 되었고, 우리 병사와 적국 병사가 섞여 싸우게 되었다.
# 그러나 당신의 병사들은 흰색 옷을 입고, 적국의 병사들은 파란색 옷을 입었기 때문에 서로가 적인지 아군인지는 구분할 수 있다.
# 문제는 같은 팀의 병사들은 모이면 모일수록 강해진다는 사실이다.

# N명이 뭉쳐있을 때는 N2의 위력을 낼 수 있다. 과연 지금 난전의 상황에서는 누가 승리할 것인가? 
# 단, 같은 팀의 병사들이 대각선으로만 인접한 경우는 뭉쳐 있다고 보지 않는다.

# 입력
# 첫째 줄에는 전쟁터의 가로 크기 N, 세로 크기 M(1 ≤ N, M ≤ 100)이 주어진다. 
# 그 다음 두 번째 줄에서 M+1번째 줄에는 각각 (X, Y)에 있는 병사들의 옷색이 띄어쓰기 없이 주어진다. 
# 모든 자리에는 병사가 한 명 있다. B는 파란색, W는 흰색이다. 당신의 병사와 적국의 병사는 한 명 이상 존재한다.

# 출력
# 첫 번째 줄에 당신의 병사의 위력의 합과 적국의 병사의 위력의 합을 출력한다.

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