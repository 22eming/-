L, S, n = int(input()), list(map(int, input().split())), int(input())

if n in S:
    print(0)

else:
    S.append(n)
    S = sorted(S)
    n_idx = S.index(n)
    if n_idx == 0:
        start = [i for i in range(1, n+1)]
    else:
        start = [i for i in range(S[n_idx-1]+1, n+1)]
    end = [i for i in range(n, S[n_idx+1])]

    print(len(start)*len(end)-1)