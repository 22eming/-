X, Y = map(int, input().split())

Z = Y * 100 // X
s, e = 0, 1000000000

if Z >= 99: 
    print(-1); exit(0)
while s <= e:
    m = (s+e) // 2
    z =  (Y+m) * 100 // (X+m)
    if Z < z:
        e = m-1
    else:
        s = m+1

print(e+1)