# y1, m1, d1 = map(int, input().split())
# y2, m2, d2 = map(int, input().split())
y1, m1, d1 = [2008, 1, 2]
y2, m2, d2 = [3008, 1, 1]
        
import datetime as dt
d_day = str(dt.date(y2, m2, d2) - dt.date(y1, m1, d1)).split()[0]

if y2-y1 == 1000:
    if m2 > m1: print('gg')
    elif m2 == m1:
        if d2 >= d1: print('gg')
elif y2-y1 > 1000:
    print('gg')
else:
    print(f'D-{d_day}')
