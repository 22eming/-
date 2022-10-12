t = int(input())
for _ in range(t):
    n = int(input())
    v = list(map(int, input().split()))

    avg_v = sum(v) / n
    pass_n = sum([1 for i in v if i >= avg_v])
    print('{}/{}'.format(pass_n, n))
