N = int(input())
meeting = sorted([tuple(map(int, input().split()))
                 for _ in range(N)], key=lambda x: [x[1], x[0]])

cnt = end = 0
for s, e in meeting:
    if s >= end:
        end = e
        cnt += 1

print(cnt)