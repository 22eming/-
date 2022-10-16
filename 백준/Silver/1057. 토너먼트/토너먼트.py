from math import ceil
N, kim, im = map(int, input().split())

cnt = 0
while True:
    cnt += 1
    k, i = ceil(kim/2), ceil(im/2)
    if k == i:
        print(cnt)
        break
    kim, im = k, i