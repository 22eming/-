T = int(input())
for _ in range(T):
    N = int(input())
    H = sorted(list(map(int, input().split())))
    l, r = [], []
    for i, h in enumerate(H):
        if i % 2:
            r.append(h)
        else:
            l.append(h)
    h = l + r[::-1]

    answer = 0
    for i in range(N):
        answer = max(abs(h[i-1] - h[i]), answer)
    print(answer)
