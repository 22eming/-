def reverse(y, x):
    for i in range(y, y+3):
        for j in range(x, x+3):
            a[i][j] = 1 - a[i][j]


def check():
    for i in range(A):
        for j in range(B):
            if a[i][j] != b[i][j]:
                return False
    return True


A, B = map(int, input().split())
a = [list(map(int, list(input()))) for _ in range(A)]
b = [list(map(int, list(input()))) for _ in range(A)]

cnt = 0
for y in range(A - 2):
    for x in range(B - 2):
        if a[y][x] != b[y][x]:
            reverse(y, x)
            cnt += 1

if check():
    print(cnt)
else:
    print(-1)
