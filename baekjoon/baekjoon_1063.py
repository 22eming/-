K, S, N = input().split()

K, S = [ord(K[0])-65, 8-int(K[1])], [ord(S[0])-65, 8-int(S[1])]

d = {'R': [0, 1], 'L': [0, -1], 'B': [0, 1], 'T': [0, -1]}

for _ in range(int(N)):
    move = list(input())
    kx, ky = K
    sx, sy = S
    for m in move:
        dy, dx = d[m]
        kx, ky = [kx+dx, ky+dy]
        if S == [kx, ky]:
            sx, sy = [sx+dx, sy+dy]

    if all([0 <= i < 8 for i in [kx, ky, sx, sy]]):
        K, S = [kx, ky], [sx, sy]

print(f'{chr(K[0]+65)}{8-int(K[1])}')
print(f'{chr(S[0]+65)}{8-int(S[1])}')
