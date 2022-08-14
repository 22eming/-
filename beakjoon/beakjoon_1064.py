xa, ya, xb, yb, xc, yc = map(int, input().split())

if (xa-xb)/(ya-yb) == (xa-xc)/(ya-yc):
    print(-1.0)

else:
    def return_len(x1, y1, x2, y2):
        return ((x1 - x2)**2 + (y1 - y2)**2)**0.5

    ab = return_len(xa, ya, xb, yb)
    ac = return_len(xa, ya, xc, yc)
    bc = return_len(xb, yb, xc, yc)

    length = [ab+ac, ab+bc, ac+bc]
    print((max(length) - min(length)) * 2 )