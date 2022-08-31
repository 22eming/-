N = int(input())
cost = [ list(map(int, input().split())) for _ in range(N)]

for i in range(1, N):
    for j in range(3):
        cost[i][j] += min(cost[i-1][(j+1)%3], cost[i-1][(j+2)%3])
    
print(min(cost[-1]))
    