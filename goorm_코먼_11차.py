# N, S, E = map(int, input().split())

# board = [ list(map(int, input().split())) for _ in range(N) ]

l_y, l_x = len(board), len(board[0])
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

share = set()
for y in range(l_y):
    for x in range(l_x):
        for d in zip(dy, dx):
            yy, xx = [y+d[0], x+d[1]]
            if 0 <= yy < l_y and 0 <= xx < l_x:
                if S <= abs(board[yy][xx] - board[y][x]) <= E:
                    share.add(f"{yy}_{xx}")
                    share.add(f"{y}_{x}")

mil = 0
for s in share:
    y, x = map(int, s.split("_"))
    mil += board[y][x]

mil = mil // len(share)
print(mil)

    
