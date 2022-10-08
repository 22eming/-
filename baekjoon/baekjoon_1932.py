n = int(input())
tri = [list(map(int, input().split())) for _ in range(n)]
max_tri = [[0]*i for i in range(1, (n+1))]
max_tri[0] = tri[0]

for y in range(1, n):
    for x in range(y+1):
        x1, x2 = 0, 0
        if x != 0:
            x1 = max_tri[y-1][x-1] + tri[y][x]
        if x+1 != len(tri[y]):
            x2 = max_tri[y-1][x] + tri[y][x]
        max_tri[y][x] = max(x1, x2)

print(max(max_tri[-1]))
