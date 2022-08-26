n, m = map(int, input().split())

# padding
board = [ [2]+list(map(int,input().split()))+[2] for i in range(n) ]
board = [[2]*(m+2)] + board + [[2]*(m+2)]

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

ddx = [1, 1, -1, -1]
ddy = [1, -1, -1, 1]

visited = set()

for y in range(1, n+1):
	for x in range(1, m+1):
		# 1이며 주변 4방향이 1
		if board[y][x] == 1:
			
			for d in zip(dy, dx):
				yy, xx = [y+d[0], x+d[1]]
				if board[yy][xx] == 1:
					visited.add(f"{y}_{x}")
					visited.add(f"{yy}_{xx}")
			
			for d in zip(ddy, ddx):
				yy, xx = [y+d[0], x+d[1]]
				if board[yy][xx] == 1:
					if board[y][xx] != 2 or board[yy][x] != 2:
						visited.add(f"{y}_{x}")
						visited.add(f"{yy}_{xx}")

print(len(visited))