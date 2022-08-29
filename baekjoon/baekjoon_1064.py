xa, ya, xb, yb, xc, yc = map(int, input().split())
# 기울기 비교
if (ya-yb)*(xa-xc) == (xa-xb)*(ya-yc):
    print(-1.0)
# 선분 길이 최대 최소 구하기
else:
    def return_len(x1, y1, x2, y2):
        return ((x1 - x2)**2 + (y1 - y2)**2)**0.5

    ab = return_len(xa, ya, xb, yb)
    ac = return_len(xa, ya, xc, yc)
    bc = return_len(xb, yb, xc, yc)

    length = [ab+ac, ab+bc, ac+bc]
    print((max(length) - min(length)) * 2 )